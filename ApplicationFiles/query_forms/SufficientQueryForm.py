from tkinter import *
from typing import Any

from ApplicationFiles.query_forms.QueryForm import QueryForm
from core.agent_group import AgentGroup
from core.program import Program
from core.queries import ExecutabilityQuery, AccessabilityQuery, SufficiencyQuery
from core.statements import Effect


class SufficientQueryForm(QueryForm):
    def __init__(self, root):
        super().__init__(root)
        self.statement_form_frame = LabelFrame(root, text="Sufficiency query", width=500, font=15)  # Set the width
        self.statement_form_frame.pack_propagate(False)  # Prevent the frame from resizing to fit its contents

        self.main_label = Label(self.statement_form_frame, text="sufficient for")
        self.program_entry = Entry(self.statement_form_frame, width=30)
        self.condition1_entry = Entry(self.statement_form_frame, width=30)
        self.main_label.grid(row=1, column=0)
        self.program_entry.grid(row=0, column=0)
        self.condition1_entry.grid(row=2, column=0)

    def show(self):
        # Show the "Impossible" form
        self.statement_form_frame.grid(row=4, column=1,columnspan=1, sticky='ew')  # Make the frame span two columns and take full available width

    def hide(self):
        # Hide the "Impossible" form
        self.statement_form_frame.grid_remove()

    def answer_query(self, agents) -> Any:
        program_string = self.program_entry.get()
        program_list = [s.strip() for s in program_string.split(',')]
        condition1 = self.condition1_entry.get()
        print(program_list)
        print(condition1)
        return SufficiencyQuery(AgentGroup(program_list, agents), Program.parse_string(condition1, agents))


