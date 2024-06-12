from ApplicationFiles.statement_form.Form import Form
from tkinter import *

from core.model import ModelSingleton
from core.program import Program
from core.statements import Value


class ValueForm(Form):
    def __init__(self, root, statements_listbox):
        super().__init__(root, statements_listbox)
        self.statement_form_frame = LabelFrame(root, text="Value statement", width=500, font=15)  # Set the width
        self.statement_form_frame.pack_propagate(False)  # Prevent the frame from resizing to fit its contents
        self.observable = False
        self.observable_label = Label(self.statement_form_frame, text="Observable", bg="#efefef", padx=5, pady=2,
                                      relief="solid",  bd=1, highlightbackground="black")
        self.observable_label.bind("<Button-1>", self.toggle_observable)
        self.condition_entry = Entry(self.statement_form_frame)
        self.after_label = Label(self.statement_form_frame, text="after")
        self.program_entry = Entry(self.statement_form_frame)
        self.add_value_button = Button(self.statement_form_frame, text="Add", command=self.add_effect)

        self.observable_label.grid(row=0, column=0)
        self.condition_entry.grid(row=0, column=1)
        self.after_label.grid(row=0, column=2)
        self.program_entry.grid(row=0, column=3)
        self.add_value_button.pack(side='right')

    def toggle_observable(self, event):
        self.observable = not self.observable
        current_color = self.observable_label.cget("bg")
        if current_color == "#efefef":
            self.observable_label.config(bg="#F0F0F0", fg="gray")
        else:
            self.observable_label.config(bg="#efefef", fg="black")

    def show(self):
        # Show the "Effect" form
        self.statement_form_frame.grid(row=4, columnspan=1, sticky='ew')

    def hide(self):
        # Hide the "Effect" form
        self.statement_form_frame.grid_remove()

    def add_effect(self):
        # Add the new "Value" statement to the listbox

        is_observable = self.observable
        condition = self.condition_entry.get()
        program_str = self.program_entry.get()

        try:
            program_obj = Program.parse_string(program_str, ModelSingleton().agents)
        except Exception as e:
            print(e.args[0])
            return

        obj = Value(observable=is_observable, condition=condition, program=program_obj)

        if self.observable:
            self.statements_listbox.insert(END, f"Observable {condition} After {program_str}")
        else:
            self.statements_listbox.insert(END, f"{condition} After {program_str}")

        self.statements_listbox.objects.append(obj)
        print(self.statements_listbox.objects)

        # Clear the form
        self.condition_entry.delete(0, END)
        self.program_entry.delete(0, END)
