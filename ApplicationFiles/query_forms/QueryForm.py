from typing import Any


class QueryForm:
    def __init__(self, root):
        self.root = root

    def show(self):
        raise NotImplementedError

    def hide(self):
        raise NotImplementedError

    def answer_query(self, agents) -> Any:
       raise NotImplementedError
