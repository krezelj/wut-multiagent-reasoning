from tkinter import *
from typing import Any

from ApplicationFiles.query_forms.QueryForm import QueryForm
from core.agent_group import AgentGroup
from core.program import Program
from core.queries import ExecutabilityQuery, ValueQuery, AccessabilityQuery
from core.statements import Effect


class AccessibilityQueryForm(QueryForm):
    def __init__(self, root):
        super().__init__(root)
        self.statement_form_frame = LabelFrame(root, text="Accessibility query", width=500, font=15)  # Set the width
        self.statement_form_frame.pack_propagate(False)  # Prevent the frame from resizing to fit its contents
        # Create a StringVar for the dropdown menu
        self.dropdown_var = StringVar()
        self.dropdown_var.set("necessary")  # Set the default value

        # Create the dropdown menu
        self.dropdown_menu = OptionMenu(self.statement_form_frame, self.dropdown_var, "necessary", "possibly")
        self.dropdown_menu.grid(row=0, column=0)  # Adjust the row and column as needed

        self.program_entry = Entry(self.statement_form_frame, width=30)
        self.program_label = Label(self.statement_form_frame, text="by")
        self.condition1_label = Label(self.statement_form_frame, text="accessible")
        self.condition1_entry = Entry(self.statement_form_frame, width=30)
        self.condition2_label = Label(self.statement_form_frame, text="from")
        self.condition2_entry = Entry(self.statement_form_frame, width=30)
        self.program_label.grid(row=2, column=0)
        self.program_entry.grid(row=2, column=1)
        self.condition1_label.grid(row=1, column=0)
        self.condition1_entry.grid(row=1, column=1)
        self.condition2_label.grid(row=3, column=0)
        self.condition2_entry.grid(row=3, column=1)

    def show(self):
        # Show the "Impossible" form
        self.statement_form_frame.grid(row=4,column=1,columnspan=1, sticky='ew')  # Make the frame span two columns and take full available width

    def hide(self):
        # Hide the "Impossible" form
        self.statement_form_frame.grid_remove()

    def answer_query(self, agents) -> Any:
        necessary = True if self.dropdown_var.get() == "necessary" else False
        program_string = self.program_entry.get()
        program_list = [s.strip() for s in program_string.split(',')]

        condition1 = self.condition1_entry.get()
        print(agents)
        condition2 = None if self.condition2_entry.get() == "" else self.condition2_entry.get()
        return AccessabilityQuery(necessary, condition1,  AgentGroup(program_list, agents), condition2)

