from tkinter import *

from ApplicationFiles.query_forms.AccessibilityQueryForm import AccessibilityQueryForm
from ApplicationFiles.query_forms.ExecutableQueryForm import ExecutableQueryForm
from ApplicationFiles.query_forms.SufficientQueryForm import SufficientQueryForm
from ApplicationFiles.query_forms.ValueQueryForm import ValueQueryForm


class QueriesForms:
    def __init__(self, root, statements_listbox):
        self.model = None
        self.root = root
        self.statements_listbox = statements_listbox

        # Create a new frame for the query forms
        self.query_forms_frame = root
        self.query_types = {
            "Executable": ExecutableQueryForm(self.query_forms_frame),
            "Value": ValueQueryForm(self.query_forms_frame),
            "Accessibility": AccessibilityQueryForm(self.query_forms_frame),
            "Sufficiency": SufficientQueryForm(self.query_forms_frame),
        }
        self.current_form = None
        # Create a frame for the statement controls
        self.statement_controls_frame = LabelFrame(root, text="Query Controls", font=15)
        self.statement_controls_frame.grid(row=3, column=1, sticky='ew', pady=(10, 0))

        # Create a dropdown menu for the statement types
        self.query_type_var = StringVar()
        self.query_type_var.set("Select query type")  # Set the initial value to the label text
        self.query_type_dropdown = OptionMenu(self.statement_controls_frame, self.query_type_var, *self.query_types.keys(), command=self.show_form)
        self.query_type_dropdown.config(width=20)
        self.query_type_dropdown.grid(row=0, column=0, sticky='e')
        self.answer_button = Button(self.statement_controls_frame, text="Answer", command=self.answer_query)
        self.answer_button.grid(row=1, column=0, sticky='w')
        self.answer = Label(self.statement_controls_frame, text="")
        self.answer.grid(row=1, column=1, sticky='w')

    def answer_query(self):
        query = self.current_form.answer_query(self.model.agents)
        result = query.answer(self.model)
        self.answer.config(text="Answer: " + str(result))



    def set_model(self, model):
        self.model = model

    def show_form(self, query_type):
        # Hide the current form if it exists
        if self.current_form is not None:
            self.current_form.hide()

        # Show the selected form
        self.current_form = self.query_types[query_type]
        self.current_form.show()
        self.query_type_var.set("Select query type")  # Set the initial value to the label text
