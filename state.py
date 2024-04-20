from expressions import Node

class State:

    def __init__(self, values: dict, encoding: int) -> None:
        self.values = values
        self.encoding = encoding

    def models(self, condition: Node) -> bool:
        return condition(self.values)
    
    def __repr__(self):
        return str(self.values)


class ImpossibleState(State):

    def __init__(self) -> None:
        pass

    def models(self, condition: Node) -> bool:
        return False