from expressions import Node

class State:

    def __init__(self, values: dict, encoding: int) -> None:
        self.values = values
        self.encoding = encoding

    def models(self, condition: Node) -> bool:
        return condition(self.values)


class ImpossibleState(State):

    def models(self, condition: Node) -> bool:
        return False