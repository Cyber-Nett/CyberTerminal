from tkinter import *

root = Tk()
root.geometry("700x700")
root.title("CyberTerminal")

fg_color = "Cyan"


def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    if (INPUT == "120"):
        Output.insert(END, 'Correct')
    else:
        Output.insert(END, "Wrong answer")


inputtxt = Text(root, height=700,
                width=700,
                bg="black",
                fg=fg_color,
                insertbackground="green")
inputtxt.pack()
mainloop()