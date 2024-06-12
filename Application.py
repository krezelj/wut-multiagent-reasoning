import tkinter
from tkinter import *
from tkinter.font import Font

from ApplicationFiles.queries_forms import QueriesForms
from core.model import *
from ApplicationFiles.properties import *
from ApplicationFiles.actions import *
from tkinter import *
import tkinter as tk

from ApplicationFiles.statement_forms import StatementForms


# Function to format and display states
def format_state(states):
    formatted_states = []
    for idx, state in enumerate(states):
        formatted_line = f"s{idx}: "
        formatted_keys = []
        for key, value in state.values.items():
            if value:
                formatted_keys.append(f"{key}")
            else:
                formatted_keys.append(f"¬{key}")
        formatted_line += ", ".join(formatted_keys)
        formatted_states.append(formatted_line)
    return formatted_states


def display_states(states):
    formatted_states = format_state(states)
    text_box.delete("1.0", tk.END)
    for state in formatted_states:
        text_box.insert(tk.END, state + "\n")


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

FluentInput, ActionsInput, AgentsInput, SignatureWarningLabel = signatureSection(root=root)
signature = Signature()
# Create a frame for the listbox
listbox_frame = LabelFrame(root, text="Statements", width=500, font=(15))  # Set a fixed width
listbox_frame.grid(row=2, column=0, sticky='nsew')
listbox_frame.grid_propagate(False)  # Disable propagation of the size of its children

# Create a listbox for the statements
statements_listbox = Listbox(listbox_frame, width=50, height=7)  # Adjust the height as needed
statements_listbox.pack(fill='both', expand=True)
statements_listbox.objects = [] # domain

# Create an instance of StatementForms
statement_forms = StatementForms(root, statements_listbox)
queries_forms = QueriesForms(root, statements_listbox)

# initialize an empty Model
model = Model([], [], [], [])


def signatureAction():
    global model
    SignatureWarningLabel.after(3000, lambda: SignatureWarningLabel.config(text=""))  # Clear the text after delay

    SignatureWarningLabel.config(foreground="red")
    try:
         readSignature(signature, FluentInput, ActionsInput, AgentsInput)
    except Exception as e:
        SignatureWarningLabel.config(text=e.args[0])
        return
    SignatureWarningLabel.config(text="Correct Signature", foreground="green")

    try:
        model = Model(
            signature.fluents,
            signature.actions,
            signature.agents,
            statements_listbox.objects
        )
        queries_forms.set_model(model)
    except Exception as e:
        SignatureWarningLabel.config(text=e.args[0])
        return

    # Update initial statements
    display_states(model.initial_states)

    SignatureWarningLabel.config(text="Model updated", foreground="green")


signatureButton = Button(root, text="Apply", command=signatureAction)
signatureButton.config(width=30)
signatureButton.grid(row=5, column=0, sticky="ew")

# Create a text box for displaying states
initial_states_frame = LabelFrame(root, text="Initial States", width=500, font=15)
initial_states_frame.grid(row=2, column=1, sticky='nsew', padx=10, pady=10)
initial_states_frame.grid_propagate(False)

# Create a text box for displaying states inside the LabelFrame
text_box = Text(initial_states_frame, wrap=tk.WORD, width=50, height=10)
text_box.pack(fill='both', expand=True)

root.mainloop()
