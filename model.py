from utils import *
from state import *
from statements import *
from expressions import *
from agent_group import *


class Model:

    def __init__(self, fluents: list[str], domain) -> None:
        self.fluents = [f.lower() for f in fluents]
        self.domain = domain
        self.split_statements()
        self.generate_states()
        self.set_nonintertial()
        self.set_initial_states()

    def split_statements(self) -> None:
        self.initialisation_statements: list[InitialisationStatement] = \
            [s for s in self.domain if type(s) is InitialisationStatement]
        self.effect_statements: list[EffectStatement] = \
            [s for s in self.domain if type(s) is EffectStatement]
        self.release_statements: list[ReleaseStatement] = \
            [s for s in self.domain if type(s) is ReleaseStatement]
        self.constraint_statements: list[ConstraintStatement] = \
            [s for s in self.domain if type(s) is ConstraintStatement]
        self.spec_statements: list[SpecificationStatement] = \
            [s for s in self.domain if type(s) is SpecificationStatement]

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
        self.initial_states = []
        condition = And([s.condition for s in self.initialisation_statements])
        for s in self.states:
            if s.models(condition):
                self.initial_states.append(s)
        if len(self.initial_states) == 0:
            raise Exception("No viable initials states")

    def res(self, action: str, agents: AgentGroup, state: State) -> list[State]:
        # get res0 set --> set of all states which satisfy the AND of all post conditions of effect statements
        # using XOR determine the fluents that changed
        # set bits corresponding to nonintertial fluents to 0 using mask
        # set all bits corresponding to released fluents to 1
        # determine inclusion minimal new states
        # return them

        # get all applicable effect and release statements
        is_statement_applicable = \
            lambda e : state.models(e.pre_condition) and agents.models(e.agent_condition) and e.action == action.lower()
        effects = [e for e in self.effect_statements if is_statement_applicable(e)]
        releases = [e for e in self.release_statements if is_statement_applicable(e)]

        # get res0 set -- set of all states resulting from effects that satisfy the aggregated post condition
        # if post_conditon is empty (no effects found) the And will always return true for all states
        # after the minimisation they will be reduced to only the current state (unless some releases also happen)
        post_condition = And([e.post_condition for e in effects])
        res0 = [s for s in self.states if s.models(post_condition)]
        if len(res0) == 0:
            raise Exception(f"Unexecutable action {action} by {agents} in {state}")
        
        # get released fluents
        released = {f: False for f in self.fluents}
        for r in releases:
            released[r.fluent] = True
        released_mask = values2enc(released, self.fluents)
        
        # get difference between new states and the current states
        new = [(state.encoding ^ s.encoding) & (~self.nonintertial_mask) | released_mask for s in res0]

        # determine inclusion minimal
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
    