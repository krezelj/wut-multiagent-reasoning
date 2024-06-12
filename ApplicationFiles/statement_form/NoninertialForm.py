from ApplicationFiles.statement_form.Form import Form
from tkinter import *

from core.statements import Specification


class NoninertialForm(Form):
    def __init__(self, root, statements_listbox):
        super().__init__(root, statements_listbox)
        self.statement_form_frame = LabelFrame(root, text="Noninertial statement", width=500,font=(15))
        self.statement_form_frame.pack_propagate(False)
        self.noninertial_label = Label(self.statement_form_frame, text="noninertial")
        self.noninertial_entry = Entry(self.statement_form_frame)
        self.add_noninertial_button = Button(self.statement_form_frame, text="Add", command=self.add_noninertial)

        self.noninertial_label.grid(row=0, column=1)
        self.noninertial_entry.grid(row=0, column=2)
        self.add_noninertial_button.pack(side='right')

    def show(self):
        self.statement_form_frame.grid(row=4, columnspan=1, sticky='new')

    def hide(self):
        self.statement_form_frame.grid_remove()

    def add_noninertial(self):
        noninertial = self.noninertial_entry.get()
        obj = Specification(noninertial)
        self.statements_listbox.insert(END, f"noninertial {noninertial}")
        self.statements_listbox.objects.append(obj)
        print(self.statements_listbox.objects)
        self.noninertial_entry.delete(0, END)