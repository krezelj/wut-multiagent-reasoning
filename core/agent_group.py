from typing import Union
from core.expressions import Node
from core.utils import *


class AgentGroup:

    def __init__(self, values: Union[dict, list[str]], all_agents: list[str]) -> None:
        if isinstance(values, dict):
            self.values = values
        else:
            self.values = {a: a in values for a in all_agents}
        self.encoding = values2enc(self.values, all_agents)

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