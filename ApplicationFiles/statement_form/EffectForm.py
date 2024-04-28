from ApplicationFiles.statement_form.Form import Form
from tkinter import *

from core.statements import Effect


class EffectForm(Form):
    def __init__(self, root, statements_listbox):
        super().__init__(root, statements_listbox)
        self.statement_form_frame = LabelFrame(root, text="Effect statement", width=500,font=(15))  # Set the width
        self.statement_form_frame.pack_propagate(False)  # Prevent the frame from resizing to fit its contents
        self.effect_label = Label(self.statement_form_frame, text="Effect")
        self.effect_entry = Entry(self.statement_form_frame)
        self.by_label_effect = Label(self.statement_form_frame, text="by")
        self.by_entry_effect = Entry(self.statement_form_frame)
        self.causes_label = Label(self.statement_form_frame, text="causes")
        self.causes_entry = Entry(self.statement_form_frame)
        self.if_label_effect = Label(self.statement_form_frame, text="if")
        self.if_entry_effect = Entry(self.statement_form_frame)
        self.add_effect_button = Button(self.statement_form_frame, text="Add", command=self.add_effect)

        # self.effect_label.grid(row=0, column=0)
        self.effect_entry.grid(row=0, column=1)
        self.by_label_effect.grid(row=0, column=2)
        self.by_entry_effect.grid(row=0, column=3)
        self.causes_label.grid(row=1, column=0)
        self.causes_entry.grid(row=1, column=1)
        self.if_label_effect.grid(row=1, column=2)
        self.if_entry_effect.grid(row=1, column=3)
        self.add_effect_button.pack(side='right')

    def show(self):
        # Show the "Effect" form
        self.statement_form_frame.grid(row=4, columnspan=1, sticky='ew')  # Make the frame span two columns and take full available width

    def hide(self):
        # Hide the "Effect" form
        self.statement_form_frame.grid_remove()

    def add_effect(self):
        # Add the new "Effect" statement to the listbox
        effect = self.effect_entry.get()
        by = self.by_entry_effect.get()
        causes = self.causes_entry.get()
        if_condition = self.if_entry_effect.get()
        obj = Effect(action=effect, agent_condition=by,
                        post_condition=causes, pre_condition=if_condition)

        if if_condition != '':
            self.statements_listbox.insert(END, f"{effect} By {by} Causes {causes} If {if_condition}")
        else:
            self.statements_listbox.insert(END, f"{effect} By {by} Causes {causes}")
        self.statements_listbox.objects.append(obj)
        print(self.statements_listbox.objects)

        # Clear the form
        self.effect_entry.delete(0, END)
        self.by_entry_effect.delete(0, END)
        self.causes_entry.delete(0, END)
        self.if_entry_effect.delete(0, END)
