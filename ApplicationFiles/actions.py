import re
from ApplicationFiles.errors import *
def readSignature(signature, FluentInput, ActionsInput, AgentsInput):
    # data must be separated by ',' (comma + space).
    # tutaj może bym dodał jeszcze obsługę żeby nie było tak że jakiś obiekt ma spacje.
    # Żeby nie było że użytkownik poda: nazwa1, nazwa 2
    
    def clearWord(text):
        return text.strip()
    def extractData(text):
        return text.split(",")
    
    def validateList(txt_list):
        for word in txt_list:
            if(word.isspace()):
                raise SpaceException()
            if(word == ''):
                raise EmptyWordException()
            if(word.isdigit()):
                raise DigitWordException()

    signature.fluents = [clearWord(i) for i in extractData(FluentInput.get())]
    signature.actions = [clearWord(i) for i in extractData(ActionsInput.get())]
    signature.agents = [clearWord(i) for i in extractData(AgentsInput.get())]
    
    def signatureValidator(list, name):
        try:
            validateList(list)
        except SpaceException as se:
            raise Exception(name + " can not be multi-word")
        except DigitWordException as dwe:
            raise Exception(name + " can not be a digit")
        except EmptyWordException as ee:
            raise Exception(name + " can not be empty word")
    try:
        signatureValidator(signature.fluents, "Fluent")
        if clearWord(ActionsInput.get()) != '':
            signatureValidator(signature.actions, "Action")
        if clearWord(AgentsInput.get()) != '':
            signatureValidator(signature.agents, "Agent")
    except Exception as e:
        raise e