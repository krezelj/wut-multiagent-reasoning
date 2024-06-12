from tkinter import *
from typing import Any

from ApplicationFiles.query_forms.QueryForm import QueryForm
from core.program import Program
from core.queries import ExecutabilityQuery
from core.statements import Effect


class ExecutableQueryForm(QueryForm):
    def __init__(self, root):
        super().__init__(root)
        self.statement_form_frame = LabelFrame(root, text="Executability query", width=500, font=15)  # Set the width
        self.statement_form_frame.pack_propagate(False)  # Prevent the frame from resizing to fit its contents
        # Create a StringVar for the dropdown menu
        self.dropdown_var = StringVar()
        self.dropdown_var.set("necessary")  # Set the default value

        # Create the dropdown menu
        self.dropdown_menu = OptionMenu(self.statement_form_frame, self.dropdown_var, "necessary", "possibly")
        self.dropdown_menu.grid(row=0, column=0)  # Adjust the row and column as needed

        self.main_label = Label(self.statement_form_frame, text="executable")
        self.program_entry = Entry(self.statement_form_frame)
        self.condition1_label = Label(self.statement_form_frame, text="from")
        self.condition1_entry = Entry(self.statement_form_frame)
        self.main_label.grid(row=1, column=0)
        self.program_entry.grid(row=1, column=1)
        self.condition1_label.grid(row=2, column=0)
        self.condition1_entry.grid(row=2, column=1)

    def show(self):
        # Show the "Impossible" form
        self.statement_form_frame.grid(row=4,columnspan=1, sticky='ew')  # Make the frame span two columns and take full available width

    def hide(self):
        # Hide the "Impossible" form
        self.statement_form_frame.grid_remove()

    def add_impossible(self):
        # Add the new "Impossible" statement to the listbox
        program = self.program_entry.get()
        condition1 = self.condition1_entry.get()
        # if_condition = self.if_entry.get()
        # obj = Effect(action=impossible, agent_condition=by,
        #              post_condition='false', pre_condition=if_condition)
        # self.statements_listbox.insert(END, f"Impossible {impossible} By {by} If {if_condition}")
        # self.statements_listbox.objects.append(obj)
        # print(self.statements_listbox.objects)
        #
        # # Clear the form
        # self.impossible_entry.delete(0, END)
        # self.by_entry.delete(0, END)
        # self.if_entry.delete(0, END)

    def answer_query(self, agents) -> Any:
        necessary = True if self.dropdown_var.get() == "necessary" else False
        program = self.program_entry.get()
        print(agents)
        condition1 = None if self.condition1_entry.get() == "" else self.condition1_entry.get()
        return ExecutabilityQuery(necessary, Program.parse_string(program, agents), condition1)

