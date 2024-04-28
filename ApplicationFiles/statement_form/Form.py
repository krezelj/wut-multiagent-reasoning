class Form:
    def __init__(self, root, statements_listbox):
        self.root = root
        self.statements_listbox = statements_listbox

    def show(self):
        raise NotImplementedError

    def hide(self):
        raise NotImplementedError
