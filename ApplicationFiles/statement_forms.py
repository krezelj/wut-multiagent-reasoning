from tkinter import *

from ApplicationFiles.statement_form.AlwaysForm import AlwaysForm
from ApplicationFiles.statement_form.EffectForm import EffectForm
from ApplicationFiles.statement_form.ImpossibleForm import ImpossibleForm
from ApplicationFiles.statement_form.NoninertialForm import NoninertialForm
from ApplicationFiles.statement_form.ReleaseForm import ReleaseForm
from ApplicationFiles.statement_form.InitiallyForm import InitiallyForm

class StatementForms:
    def __init__(self, root, statements_listbox):
        self.root = root
        self.statements_listbox = statements_listbox
        self.statement_types = {
            "Initially": InitiallyForm(root, statements_listbox),
            "Impossible": ImpossibleForm(root, statements_listbox),
            "Effect": EffectForm(root, statements_listbox),
            "Release": ReleaseForm(root, statements_listbox),
            "Always": AlwaysForm(root, statements_listbox),
            "Noninertial": NoninertialForm(root, statements_listbox),
        }
        self.current_form = None
        # Create a frame for the statement controls
        self.statement_controls_frame = LabelFrame(root, text="Statement Controls", font=15)
        self.statement_controls_frame.grid(row=3, column=0, sticky='new', pady=(10, 0))

        # Create a dropdown menu for the statement types
        self.statement_type_var = StringVar()
        self.statement_type_var.set("Select statement to add")  # Set the initial value to the label text
        self.statement_type_dropdown = OptionMenu(self.statement_controls_frame, self.statement_type_var, *self.statement_types.keys(), command=self.show_statement_form)
        self.statement_type_dropdown.config(width=20)
        self.statement_type_dropdown.grid(row=0, column=0, sticky='e')

        # Create a "Delete" button and initially disable it
        self.delete_button = Button(self.statement_controls_frame, text="Delete selected statement", command=self.delete_selected_item)
        self.delete_button.grid(row=0, column=1, sticky='w')
        self.delete_button.config(state=DISABLED)

        # Bind a function to the <<ListboxSelect>> event of the listbox
        self.statements_listbox.bind('<<ListboxSelect>>', self.on_listbox_select)

    def on_listbox_select(self, event):
        # Check if an item is selected
        if self.statements_listbox.curselection():
            # Show the "Delete" button
            self.delete_button.config(state=NORMAL)
        else:
            # Hide the "Delete" button
            self.delete_button.config(state=DISABLED)

    def delete_selected_item(self):
        selected_index = self.statements_listbox.curselection()

        if selected_index:
            self.statements_listbox.objects.pop(selected_index[0])
            self.statements_listbox.delete(selected_index)



    def show_statement_form(self, statement_type):
        # Hide the current form if it exists
        if self.current_form is not None:
            self.current_form.hide()

        # Show the selected form
        self.current_form = self.statement_types[statement_type]
        self.current_form.show()
        self.statement_type_var.set("Select statement to add")  # Set the initial value to the label text
