from expressions import Node


class AgentGroup:

    def __init__(self, agents: list[str], all_agents: list[str]) -> None:
        self.values = {a: a in agents for a in all_agents}

    def models(self, condition: Node) -> bool:
        return condition(self.values)
    
    def __repr__(self) -> str:
        return str(self.values)

class SuperGroup(AgentGroup):

    def __init__(self) -> None:
        pass

    def models(self, condition: Node) -> bool:
        return True
    
    def __repr__(self) -> str:
        return "SuperGroup"