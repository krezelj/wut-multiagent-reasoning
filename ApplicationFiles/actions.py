
def readSignature(signature, FluentInput, ActionsInput, AgentsInput):
    # data must be separated by ', ' (comma + space).
    def extractData(text):
        text.split(", ")
    signature.fluents = extractData(FluentInput.get())
    signature.actions = extractData(ActionsInput.get())
    signature.fluents = extractData(AgentsInput.get())