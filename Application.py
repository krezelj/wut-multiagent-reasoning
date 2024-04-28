import tkinter
from tkinter import *
from tkinter.font import Font

from ApplicationFiles.properties import *
from ApplicationFiles.actions import *
from tkinter import *
import tkinter as tk

from ApplicationFiles.statement_forms import StatementForms


class Signature:
    def __init__(self) -> None:
        self.fluents = None
        self.actions = None
        self.agents = None
        pass

root = Tk()
# Define the default font
default_font = Font(size=10)

# Set the default font for labels and inputs
root.option_add("*Label.font", default_font)
root.option_add("*Entry.font", default_font)
setProperties(root = root)

FluentInput, ActionsInput, AgentsInput, SignatureWarningLabel = signatureSection(root = root)
signature = Signature()

# Create a frame for the listbox
listbox_frame = LabelFrame(root, text="Statements", width=500, font=(15))  # Set a fixed width
listbox_frame.grid(row=2, column=0, sticky='nsew')
listbox_frame.grid_propagate(False)  # Disable propagation of the size of its children

# Create a listbox for the statements
statements_listbox = Listbox(listbox_frame, width=50, height=7)  # Adjust the height as needed
statements_listbox.pack(fill='both', expand=True)
statements_listbox.objects = []

# Create an instance of StatementForms
statement_forms = StatementForms(root, statements_listbox)


def signatureAction():
    SignatureWarningLabel.config(foreground="red")
    try:
         readSignature(signature, FluentInput, ActionsInput, AgentsInput)
    except Exception as e:
        SignatureWarningLabel.config(text=e.args[0])
        return
    SignatureWarningLabel.config(text="Correct Signature",foreground="green")
    

signatureButton = Button(root, text="Apply Signature", command = signatureAction)
signatureButton.config(width=15)
signatureButton.grid(row=1, column=1)

root.mainloop()