from core.agent_group import AgentGroup
from core.model import Model


class Program:
    
    def __init__(self, program: list[tuple[str, AgentGroup]]) -> None:
        self.program = program

    def __getitem__(self, idx):
        return self.program[idx]
    
    def __len__(self):
        return len(self.program)
    

class TransitionNode:
    
    def __init__(self, state, children = None) -> None:
        self.state = state
        self.children = children

    def run_program(self, program: Program, model: Model, force_execution: bool = False):
        if len(program) == 0:
            return
        
        # get next states using res and transform them into transition nodes
        self.action = program[0][0]
        self.agents = program[0][1]
        self.children = [TransitionNode(s) for s in model.res(self.action, self.agents, self.state, force_execution)]
        for child in self.children:
            child.run_program(program[1:], model, force_execution)