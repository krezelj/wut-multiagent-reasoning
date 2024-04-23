from core.statements import *
from core.model import *

class App():

    def __init__(self):
        fluents = ['p']
        actions = ['foo']
        agents = []

        domain = [
            Initialisation('p'),
            Effect('foo', 'true', 'not(p)', 'p')
        ]

        self.model = Model(fluents, actions, agents, domain)
