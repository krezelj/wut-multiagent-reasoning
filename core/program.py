from core.agent_group import AgentGroup

class Program:
    
    def __init__(self, program: list[tuple[str, AgentGroup]]) -> None:
        self.program = program

    def __getitem__(self, idx):
        return self.program[idx]
    
    def __len__(self):
        return len(self.program)