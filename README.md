# MARS - Multi-Agent Reasoning System

MARS is an application written as a part of the project for Knowledge Representation class at Warsaw University of Technology. It supports basic reasoning with actions performed by different agents.

**Example**\
Bob and Alice are in a room with a lightbulb. They are both standing next to their own light switch. If they both press it the lightbulb will turn on. However if only one of them presses their switch the light turn off.

The above description can be represented with Action Language in the following way

$initially\ \neg light$\
$useSwitch\ by\ A\wedge B\ causes\ light$\
$useSwitch\ by\ (A\vee B)\wedge\neg(A\wedge B)\ causes\ \neg light$

Using MARS it can be written as

```py
from core.statements import Initialisation, Effect
from core.model import Model

fluents = ['light']
actions = ['useSwitch']
agents = ['A', 'B']

domain = [
    Initialisation('not(light)'),
    Effect('useSwitch', 'and(A, B)', 'light'),
    Effect('useSwitch', 'and(or(A, B), not(and(A, B)))', 'not(light)'),
]

model = Model(fluents, actions, agents, domain)
```

One can then query the model

```py
from core.queries import ValueQuery, AccessibilityQuery
from core.program import Program
from core.agent_group import AgentGroup

agentA = AgentGroup(['A'], agents)
agentB = AgentGroup(['B'], agents)
agentsAandB = AgentGroup(['A', 'B'], agents)

P = Program([('useSwitch', agentsAandB)])

# necessary light after P
vQ = ValueQuery(True, 'light', P)
print(vQ.answer(model)) # prints True

# possibly accessible light with {A} (or subset of {A})
aQ = AccessibilityQuery(False, 'light', agentA)
print(aQ.answer(model)) # prints False since agent A alone cannot turn on the light
```