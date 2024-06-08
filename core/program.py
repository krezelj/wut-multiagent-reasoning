from core.agent_group import AgentGroup

class Program:
    
    def __init__(self, program: list[tuple[str, AgentGroup]]) -> None:
        self.program = program

    def __getitem__(self, idx):
        return self.program[idx]
    
    def __len__(self):
        return len(self.program)
    
    @classmethod
    def parse_string(cls, expression: str, all_agents: list[str]):
        # expression should be in the following format
        # "action by a,b,c; action by a,b,c"
        # i.e. each step of the program should be separated using ';'
        # inside the step, the action and the performing agents should be separated using " by "
        # where spaces around "by" are important
        # spaces in any other place in the expression are not important and will be ignored
        # letter case is also ignored

        steps = expression.split(';')
        program = []
        for step in steps:
            if step.find(' by ') != -1:
                action, agents = step.split(' by ')
            else:
                action = step
                agents = ''
            action = action.replace(' ', '')
            agents = agents.replace(' ', '').split(',')
            agent_group = AgentGroup(agents, all_agents)
            program.append((action, agent_group))
        return Program(program)