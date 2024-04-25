from tkinter import *

def setProperties(root:Tk):
    root.title("WUT-multiagent-reasoning")
    # Window Properties:
    window_width = 1080
    window_height = 720
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2
    
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

def signatureSection(root):
    
    group_box = LabelFrame(root, text="Signature", font=(15))
    SignatureWarningLabel = Label(root,text="ww",font=(12),foreground="red")
    SignatureWarningLabel.grid(row=0, column=0)
    
    group_box.grid(row=1, column=0)
    group_box.grid_columnconfigure(0, pad=30, minsize=80)
    group_box.grid_columnconfigure(1, pad=30, minsize=400)
    group_box.grid_rowconfigure(0, minsize=30)
    group_box.grid_rowconfigure(1, minsize=30)
    group_box.grid_rowconfigure(2, minsize=30)
    FluentLabel = Label(group_box, text="Fluents:", font=(15))
    ActionsLabel = Label(group_box, text="Actions:", font=(15))
    AgentsLabel = Label(group_box, text="Agents:", font=(15))
    
    FluentLabel.grid(row=0, column=0, pady=3)
    ActionsLabel.grid(row=1, column=0, pady=3)
    AgentsLabel.grid(row=2, column=0, pady=3)
    
    FluentInput = Entry(group_box, font=(15))
    ActionsInput= Entry(group_box, font=(15))
    AgentsInput = Entry(group_box, font=(15))

    FluentInput.grid(row=0, column=1, sticky="ew", padx=15, pady=3)
    ActionsInput.grid(row=1, column=1, sticky="ew", padx=15, pady=3)
    AgentsInput.grid(row=2, column=1, sticky="ew", padx=15, pady=3)

    return FluentInput, ActionsInput, AgentsInput, SignatureWarningLabel