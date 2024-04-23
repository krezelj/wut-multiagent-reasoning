from typing import Optional
from core.program import *
from core.model import *
from core.expressions import parse_expression
from core.state import State

class ValueQuery:
    # necessary/possibly alpha after P from pi
    
    def __init__(self, necessary: bool, post_condition: str, program: Program, pre_condition: Optional[str] = None):
        self.necessary = necessary
        self.post_condition = parse_expression(post_condition)
        self.program = program
        self.pre_condition = None if pre_condition is None else parse_expression(pre_condition)

    def answer(self, model : Model) -> bool:
        initial_states = \
            model.initial_states if self.pre_condition is None else model.get_states_that_model(self.pre_condition)
        transitions = [TransitionNode(s) for s in initial_states]
        for t in transitions:
            t.run_program(self.program, model)

        root = TransitionNode(None, children=transitions)
        stack = [root]
        while len(stack) > 0:
            current = stack.pop()
            if current.children is not None:
                stack.extend(current.children)
                if current.state is None: # root
                    continue
            else: # leaf
                # check if satisifies post_condition
                satisfies = current.state.models(self.post_condition)
                if satisfies and not self.necessary:
                    return True
                if not satisfies and self.necessary:
                    return False
                
        # either all leaves satify or no leaf satisfies post condition, depending on the value of necessary
        # so we can simply return necessary
        return self.necessary


class ExecutabilityQuery:
    # necessary/possibly executable P from pi
    
    def __init__(self, necessary: bool, program: Program, pre_condition: Optional[str] = None):
        self.necessary = necessary
        self.program = program
        self.pre_condition = None if pre_condition is None else parse_expression(pre_condition)

    def answer(self, model : Model) -> bool:
        initial_states = \
            model.initial_states if self.pre_condition is None else model.get_states_that_model(self.pre_condition)
        transitions = [TransitionNode(s) for s in initial_states]
        for t in transitions:
            t.run_program(self.program, model, force_execution=True)

        root = TransitionNode(None, children=transitions)
        stack = [root]
        while len(stack) > 0:
            current = stack.pop()
            if current.children is None:
                # leaf reached so the execution is *possible*
                if not self.necessary:
                    return True
                if self.necessary:
                    continue

            if len(current.children) == 0:
                # not a leaf but no children so the program is not neccessarily executable
                if self.necessary:
                    return False
                if not self.necessary:
                    continue
                
            # else has children
            stack.extend(current.children)
                
        # if necessary then all path were defined so True
        # if not necessary this statement shouldn't be reached assuming fininite programs
        # (at least one leaf must have been reached)
        return True


class AccessabilityQuery:
    # necessary/possibly gamma from pi

    def __init__(self, necessary: bool, post_condition: str, agents: AgentGroup, pre_condition: Optional[str] = None) -> None:
        self.necessary = necessary
        self.post_condition = parse_expression(post_condition)
        self.agents = agents
        self.pre_condition = None if pre_condition is None else parse_expression(pre_condition)

    def answer(self, model: Model) -> bool:
        initial_states = \
            model.initial_states if self.pre_condition is None else model.get_states_that_model(self.pre_condition)
        self.__generate_valid_combinations(model)

        for s in initial_states:
            visited = [False] * len(model.states)
            if not self.__can_access(s, model, visited):
                break
        else: # finally if accessible from every initial state
            return True
        return False
    
    def __generate_valid_combinations(self, model: Model):
        self.valid_combinations = []
        for action in model.actions:
            for agents_encoding in range(2**len(model.agents)):
                if not is_subset(agents_encoding, self.agents.encoding):
                    continue
                values = enc2values(agents_encoding, model.agents)
                agents = AgentGroup(values, model.agents)
                self.valid_combinations.append((action, agents))

    def __can_access(self, state: State, model: Model, visited: list[bool]) -> bool:
        visited = visited.copy()
        if visited[state.encoding]:
            return False
        visited[state.encoding] = True
        if state.models(self.post_condition):
            return True
        
        # for each combination
        for combination in self.valid_combinations:
            res = model.res(combination[0], combination[1], state, force_execution=True)
            if len(res) == 0:
                continue
            for s in res:
                accessible = self.__can_access(s, model, visited)
                if not accessible and self.necessary:
                    break
                if accessible and not self.necessary:
                    return True
            else: # finally
                if self.necessary:
                    return True
        return False
    

class SufficiencyQuery:
    # G sufficient for pi
    
    def __init__(self, agents: AgentGroup, program: Program, pre_condition: Optional[str] = None):
        self.agents = agents
        self.program = program
        self.exQ = ExecutabilityQuery(True, program, pre_condition)

    def answer(self, model: Model) -> bool:
        # if not necessarily executable return False
        if not self.exQ.answer(model):
            return False
        
        for step in self.program.program:
            if not is_subset(self.agents.encoding, step[1].encoding):
                return False
        return True