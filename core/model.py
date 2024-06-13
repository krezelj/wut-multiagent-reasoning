from core.utils import *
from core.state import *
from core.statements import *
from core.expressions import *
from core.agent_group import *


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    

class Model:
    def __init__(self, fluents: list[str], actions: list[str], agents: list[str], domain):
        self.set_fields(fluents, actions, agents, domain)

    def set_fields(self, fluents: list[str], actions: list[str], agents: list[str], domain):
        self.fluents = [f.lower() for f in fluents]
        self.actions = [a.lower() for a in actions]
        self.agents = [a.lower() for a in agents]
        self.domain = domain

        # Perform additional setup tasks
        self.split_statements()
        self.generate_states()
        self.set_nonintertial()
        self.set_initial_states()
        self.graph = Graph(self)

    def split_statements(self) -> None:
        self.value_statements: list[Value] = \
            [s for s in self.domain if isinstance(s, Value)]
        self.effect_statements: list[Effect] = \
            [s for s in self.domain if isinstance(s, Effect)]
        self.release_statements: list[Release] = \
            [s for s in self.domain if isinstance(s, Release)]
        self.constraint_statements: list[Constraint] = \
            [s for s in self.domain if isinstance(s, Constraint)]
        self.spec_statements: list[Specification] = \
            [s for s in self.domain if isinstance(s, Specification)]

    def generate_states(self) -> None:
        self.states: list[State] = []
        for i in range(2**len(self.fluents)):
            # ensure impossible states are marked still added to make indexing easier by using encodings
            self.states.append(ImpossibleState()) 
            state_values = enc2values(i, self.fluents)
            for s in self.constraint_statements:
                if not s.condition(state_values):
                    break
            else: # finally, if state models all constraints
                self.states[i] = State(state_values, i)

    def set_nonintertial(self) -> None:
        self.nonintertial = {f: False for f in self.fluents}
        for s in self.spec_statements:
            self.nonintertial[s.fluent] = True
        self.nonintertial_mask = values2enc(self.nonintertial, self.fluents)

    def set_initial_states(self) -> None:
        def satisfies_condition(root: TransitionNode, condition: Node, observable: bool):
            if root.children is None:
                return root.state.models(condition)
            
            for child in root.children:
                satisifies = satisfies_condition(child, condition, observable)
                if satisifies and observable:
                    return True
                if not satisifies and not observable: # necessary
                    return False
            # either all satisfy and not observable or none satisfy and observable
            return not observable

        self.initial_states = []
        for state in self.states:
            for statement in self.value_statements:
                node = TransitionNode(state)
                node.run_program(statement.program, self)
                if not satisfies_condition(node, statement.condition, statement.observable):
                    break
            else:
                self.initial_states.append(state)
        #if len(self.initial_states) == 0:
            #raise Exception("No viable initials states")

    def res(self, action: str, agents: AgentGroup, state: State, force_execution: bool = False) -> list[State]:
        # get all applicable effect and release statements
        is_statement_applicable = lambda e: (
                state.models(e.pre_condition) and
                agents.models(e.agent_condition) and
                e.action == action.lower()
        )

        effects = [e for e in self.effect_statements if is_statement_applicable(e)]
        releases = [e for e in self.release_statements if is_statement_applicable(e)]

        # get res0 set -- set of all states resulting from effects that satisfy the aggregated post condition
        # if post_conditon is empty (no effects found) the 'And' will always return true for all states
        # after the minimisation they will be reduced to only the current state (unless some releases also happen)
        post_condition = And([e.post_condition for e in effects])
        res0 = [s for s in self.states if s.models(post_condition)]
        if len(res0) == 0 and not force_execution:
            raise Exception(f"Unexecutable action {action} by {agents} in {state}")
        
        # get released fluents
        released = {f: False for f in self.fluents}
        for r in releases:
            released[r.fluent] = True
        released_mask = values2enc(released, self.fluents)
        
        # get difference between new states and the current states ('new' function)
        new = [(state.encoding ^ s.encoding) & (~self.nonintertial_mask) | released_mask for s in res0]

        # determine inclusion minimal differences
        result_states = []
        for i in range(len(res0)):
            for j in range(len(res0)):
                if i == j: continue
                if is_strict_subset(new[j], new[i]):
                    break
            else: # finally, if nothing is a strict subset of new[i]
                result_states.append(res0[i])
        return result_states
    
    def get_states_that_model(self, condition):
        return [s for s in self.states if s.models(condition)]


class TransitionNode:
    
    def __init__(self, state, children = None) -> None:
        self.state = state
        self.children = children

    def run_program(self, program: Program, model: Model, force_execution: bool = False):
        if len(program) == 0:
            return
        
        # get next states using res and transform them into transition nodes
        self.action = program[0][0]
        self.agents = program[0][1]
        self.children = [TransitionNode(s) for s in model.res(self.action, self.agents, self.state, force_execution)]
        for child in self.children:
            child.run_program(program[1:], model, force_execution)

class GraphNode:

        def __init__(self, state: State) -> None:
            self.state = state
            self.neighbours: list[tuple[str, int, GraphNode]] = []

        def find_neighbours(self, model: Model, nodes: list['GraphNode']) -> None:
            for action in model.actions:
                for i in range(2**len(model.agents)):
                    values = enc2values(i, model.agents)
                    agents = AgentGroup(values, model.agents)
                    res = model.res(action, agents, self.state, force_execution=True)
                    for state in res:
                        node = nodes[state.encoding]
                        self.neighbours.append((action, i, node))


class Graph:

    def __init__(self, model: Model) -> None:
        self.nodes: list[GraphNode] = [GraphNode(state) for state in model.states]
        for node in self.nodes:
            if isinstance(node.state, ImpossibleState):
                continue
            node.find_neighbours(model, self.nodes)
            
            
class ModelSingleton(Model, metaclass=Singleton):
    def __init__(self, fluents: list[str], actions: list[str], agents: list[str], domain):
        super().__init__(fluents, actions, agents, domain)