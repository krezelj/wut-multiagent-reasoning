from ApplicationFiles.statement_form.Form import Form
from tkinter import *

from core.statements import Initialisation


class InitiallyForm(Form):
    def __init__(self, root, statements_listbox):
        super().__init__(root, statements_listbox)
        self.statement_form_frame = LabelFrame(root, text="Initially statement", width=500,font=(15))
        self.statement_form_frame.pack_propagate(False)
        self.initially_label = Label(self.statement_form_frame, text="initially")
        self.initially_entry = Entry(self.statement_form_frame)
        self.add_initially_button = Button(self.statement_form_frame, text="Add", command=self.add_initially)

        self.initially_label.grid(row=0, column=1)
        self.initially_entry.grid(row=0, column=2)
        self.add_initially_button.pack(side='right')

    def show(self):
        self.statement_form_frame.grid(row=4, columnspan=1, sticky='ew')

    def hide(self):
        self.statement_form_frame.grid_remove()

    def add_initially(self):
        initially = self.initially_entry.get()
        obj = Initialisation(initially)
        self.statements_listbox.insert(END, f"initially {initially}")
        self.statements_listbox.objects.append(obj)
        print(self.statements_listbox.objects)
        self.initially_entry.delete(0, END)