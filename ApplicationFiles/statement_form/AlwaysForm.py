from prompt_toolkit.filters import Always

from ApplicationFiles.statement_form.Form import Form
from tkinter import *

from core.statements import Constraint


class AlwaysForm(Form):
    def __init__(self, root, statements_listbox):
        super().__init__(root, statements_listbox)
        self.statement_form_frame = LabelFrame(root, text="Always statement", width=500,font=(15))
        self.statement_form_frame.pack_propagate(False)
        self.always_label = Label(self.statement_form_frame, text="Always")
        self.always_entry = Entry(self.statement_form_frame)
        self.add_always_button = Button(self.statement_form_frame, text="Add", command=self.add_always)

        self.always_label.grid(row=0, column=1)
        self.always_entry.grid(row=0, column=2)
        self.add_always_button.pack(side='right')

    def show(self):
        self.statement_form_frame.grid(row=4, columnspan=1, sticky='ew')

    def hide(self):
        self.statement_form_frame.grid_remove()

    def add_always(self):
        always = self.always_entry.get()
        obj = Constraint(always)
        self.statements_listbox.insert(END, f"Always {always}")
        self.statements_listbox.objects.append(obj)
        print(self.statements_listbox.objects)
        self.always_entry.delete(0, END)

