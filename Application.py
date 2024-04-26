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

FluentInput, ActionsInput, AgentsInput, SignatureWarningLabel = signatureSection(root = root)
signature = Signature()
def signatureAction():
    SignatureWarningLabel.config(foreground="red")
    try:
         readSignature(signature, FluentInput, ActionsInput, AgentsInput)
    except Exception as e:
        SignatureWarningLabel.config(text=e.args[0])
        return
    SignatureWarningLabel.config(text="Correct Signature",foreground="green")
    

signatureButton = Button(root, text="Apply Signature", command = signatureAction)
signatureButton.grid(row=1, column=1)


root.mainloop()