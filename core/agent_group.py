from typing import Union
from core.expressions import Node
from core.utils import *


class AgentGroup:

    def __init__(self, values: Union[dict[str, bool], list[str]], all_agents: list[str]) -> None:
        all_agents = [a.lower() for a in all_agents]
        if isinstance(values, dict):
            self.values = {
                k.lower(): v for k, v in values.items()
            }
        else:
            values = [a.lower() for a in values]
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