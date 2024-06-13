from ApplicationFiles.statement_form.Form import Form
from tkinter import *

from core.statements import Effect


class ImpossibleForm(Form):
    def __init__(self, root, statements_listbox):
        super().__init__(root, statements_listbox)
        self.statement_form_frame = LabelFrame(root, text="Impossible statement", width=500, font=15)  # Set the width
        self.statement_form_frame.pack_propagate(False)  # Prevent the frame from resizing to fit its contents
        self.impossible_label = Label(self.statement_form_frame, text="Impossible")
        self.impossible_entry = Entry(self.statement_form_frame)
        self.by_label = Label(self.statement_form_frame, text="by")
        self.by_entry = Entry(self.statement_form_frame)
        self.if_label = Label(self.statement_form_frame, text="if")
        self.if_entry = Entry(self.statement_form_frame)
        self.add_impossible_button = Button(self.statement_form_frame, text="Add", command=self.add_impossible)
        self.add_impossible_button.pack(side='right')
        self.impossible_label.grid(row=0, column=0)
        self.impossible_entry.grid(row=0, column=1)
        self.by_label.grid(row=1, column=0)
        self.by_entry.grid(row=1, column=1)
        self.if_label.grid(row=1, column=2)
        self.if_entry.grid(row=1, column=3)

    def show(self):
        # Show the "Impossible" form
        self.statement_form_frame.grid(row=4,columnspan=1, sticky='new')  # Make the frame span two columns and take full available width

    def hide(self):
        # Hide the "Impossible" form
        self.statement_form_frame.grid_remove()

    def add_impossible(self):
        # Add the new "Impossible" statement to the listbox
        impossible = self.impossible_entry.get()
        by = self.by_entry.get()
        if_condition = self.if_entry.get()
        obj = Effect(action=impossible, agent_condition=by,
                     post_condition='false', pre_condition=if_condition)
        self.statements_listbox.insert(END, f"Impossible {impossible} By {by} If {if_condition}")
        self.statements_listbox.objects.append(obj)
        print(self.statements_listbox.objects)

        # Clear the form
        self.impossible_entry.delete(0, END)
        self.by_entry.delete(0, END)
        self.if_entry.delete(0, END)
