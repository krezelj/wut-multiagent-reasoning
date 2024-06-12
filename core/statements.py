from typing import Optional
from core.expressions import parse_expression
from core.program import Program


class Value:
    # (Observable) alpha after A1 by phi1, ..., An by phin
    #
    # A1 by phi1, ..., An by phin - A program

    def __init__(self, observable: bool, condition: str, program: Program):
        self.observable = observable
        self.condition = parse_expression(condition)
        self.program = program


class Initialisation(Value):
    # initially alpha

    def __init__(self, condition: str) -> None:
        super().__init__(False, condition, Program([]))
        # self.condition = parse_expression(condition)


class Effect:
    # A by phi causes alpha if pi
    # impossible A by phi if pi

    def __init__(self, action: str, agent_condition: str, post_condition: str, pre_condition: Optional[str] = None):
        self.action = action.lower()
        self.agent_condition = parse_expression(agent_condition)
        self.post_condition = parse_expression(post_condition)
        self.pre_condition = parse_expression(pre_condition) if pre_condition else parse_expression('true')


class Release:
    # A by phi releases f if pi
    
    def __init__(self, action: str, agent_condition: str, fluent: str, pre_condition: Optional[str] = None):
        self.action = action.lower()
        self.agent_condition = parse_expression(agent_condition)
        self.fluent = fluent.lower()
        self.pre_condition = parse_expression(pre_condition) if pre_condition else parse_expression('true')


class Constraint:
    # always alpha
    
    def __init__(self, condition: str) -> None:
        self.condition = parse_expression(condition)


class Specification:
    # nonintertial f
    
    def __init__(self, fluent: str) -> None:
        self.fluent = fluent.lower()

