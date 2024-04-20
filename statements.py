from expressions import parse_expression


class InitialisationStatement:
    # initially alpha

    def __init__(self, condition: str) -> None:
        self.condition = parse_expression(condition)


class EffectStatement:
    # A by phi causes alpha if pi
    # impossible A by phi if pi
    

    def __init__(self, action: str, agent_condition: str, post_condition: str, pre_condition: str):
        self.action = action
        self.agent_condition = parse_expression(agent_condition)
        self.post_condition = parse_expression(post_condition)
        self.pre_condition = parse_expression(pre_condition)


class ReleaseStatement:
    # A by phi releases f if pi
    
    def __init__(self, action: str, agent_condition: str, fluent: str, pre_condition: str):
        self.action = action
        self.agent_condition = parse_expression(agent_condition)
        self.fluent = fluent
        self.pre_condition = parse_expression(pre_condition)


class ConstraintStatement:
    # always alpha
    
    def __init__(self, condition: str) -> None:
        self.condition = parse_expression(condition)


class SpecificationStatement:
    # nonintertial f
    
    def __init__(self, fluent: str) -> None:
        self.fluent = fluent

