from expressions import Node


class AgentGroup:

    def __init__(self, values: dict) -> None:
        self.values = values

    def models(self, condition: Node) -> True:
        return condition(self.values)