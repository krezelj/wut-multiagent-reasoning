from ApplicationFiles.statement_form.Form import Form
from tkinter import *

from core.statements import Release


class ReleaseForm(Form):
    def __init__(self, root, statements_listbox):
        super().__init__(root, statements_listbox)
        self.statement_form_frame = LabelFrame(root, text="Release statement", width=500,font=(15))  # Set the width
        self.statement_form_frame.pack_propagate(False)  # Prevent the frame from resizing to fit its contents
        self.release_label = Label(self.statement_form_frame, text="Release")
        self.release_entry = Entry(self.statement_form_frame)
        self.by_label_release = Label(self.statement_form_frame, text="by")
        self.by_entry_release = Entry(self.statement_form_frame)
        self.releases_label = Label(self.statement_form_frame, text="releases")
        self.releases_entry = Entry(self.statement_form_frame)
        self.if_label_release = Label(self.statement_form_frame, text="if")
        self.if_entry_release = Entry(self.statement_form_frame)
        self.add_release_button = Button(self.statement_form_frame, text="Add", command=self.add_release)

        # self.release_label.grid(row=0, column=0)
        self.release_entry.grid(row=0, column=1)
        self.by_label_release.grid(row=0, column=2)
        self.by_entry_release.grid(row=0, column=3)
        self.releases_label.grid(row=1, column=0)
        self.releases_entry.grid(row=1, column=1)
        self.if_label_release.grid(row=1, column=2)
        self.if_entry_release.grid(row=1, column=3)
        self.add_release_button.pack(side='right')

    def show(self):
        self.statement_form_frame.grid(row=4, columnspan=1, sticky='ew')

    def hide(self):
        self.statement_form_frame.grid_remove()

    def add_release(self):
        release = self.release_entry.get()
        by = self.by_entry_release.get()
        releases = self.releases_entry.get()
        if_condition = self.if_entry_release.get()
        obj = Release(action=release, agent_condition=by,
                        fluent=releases, pre_condition=if_condition)

        if if_condition != '':
            self.statements_listbox.insert(END, f"{release} By {by} Releases {releases} If {if_condition}")
        else:
            self.statements_listbox.insert(END, f"{release} By {by} Releases {releases}")
        self.statements_listbox.objects.append(obj)
        print(self.statements_listbox.objects)

        # Clear the form
        self.release_entry.delete(0, END)
        self.by_entry_release.delete(0, END)
        self.releases_entry.delete(0, END)
        self.if_entry_release.delete(0, END)
