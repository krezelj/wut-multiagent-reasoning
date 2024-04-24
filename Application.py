from tkinter import *
from ApplicationFiles.properties import *
from ApplicationFiles.actions import *

class Signature:
    def __init__(self) -> None:
        self.fluents = None
        self.actions = None
        self.agents = None
        pass
    
root = Tk()
setProperties(root = root)
FluentInput, ActionsInput, AgentsInput = signatureSection(root = root)
signature = Signature()
signatureButton = Button(root,text="Apply Signature",command = lambda:readSignature(signature, FluentInput, ActionsInput, AgentsInput))
signatureButton.grid(row=1, column=1)
root.mainloop()