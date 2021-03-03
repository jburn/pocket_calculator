"""
A simple calculator with a graphical interface.
Made just for fun and to test out tkinter and ttk

Author: Juho Bruun
Date: 04.05.2020

"""

from tkinter import *
from tkinter import ttk
import operator as op

"""
The program alters between different states using this dictionary.


hiddenline: The string that is used to edit the calcline variable that is visible to the user.

moves: Used to ensure that the user only uses a single operand at a time in the calculation.

operand: Used to set the operand to use for calculate function.

numbers: Used to set the variables for each side of the operand, and for the calculate function to use.

finished: This state is reached after pressing calculate or in an overflowerror situation.
    '1' is soft finished (clear or an operand breaks this state)
    '2' is hard finished (only clear breaks this state)

dot: Used to ensure that the user cannot use more than one dot on a single variable.
"""

states = {
"hiddenline": " ",
"moves": 0,
"operand": "",
"numbers":["", ""],
"finished": 0,
"dot": 0
}


def calculate():
    """
    This function calculates the two given variables using the current operand state.
    Used by the '=' button.
    """
    if states["finished"] != 2:    
        try:
            if states["operand"] == "plus":
                answer = op.add(float(states["numbers"][0]), float(states["numbers"][1]))
            elif states["operand"] == "minus":
                answer = op.sub(float(states["numbers"][0]), float(states["numbers"][1]))
            elif states["operand"] == "multiply":
                answer = op.mul(float(states["numbers"][0]), float(states["numbers"][1]))
            elif states["operand"] == "divide":
                answer = op.truediv(float(states["numbers"][0]), float(states["numbers"][1]))
            elif states["operand"] == "power":
                answer = op.pow(float(states["numbers"][0]), float(states["numbers"][1]))
            states["hiddenline"] = str(answer)
            calcline.set(str(answer))
            states["moves"] = 0
            states["finished"] = 1
            states["numbers"][0] = answer
            states["numbers"][1] = ""
            states["dot"] = 0
        except ValueError:
            pass
            #print("Error: Add another number to the operation")
        except UnboundLocalError:
            pass
            #print("Error: Cannot operate on a single number")
        except OverflowError:
            #print("Error: Result too large")
            calcline.set("Result too large, press clear")
            states["finished"] = 2



def clear():
    """
    This function clears the the visible text on the screen and resets all the states to default.
    Used by the 'clear' button.
    """
    states["finished"] = 0
    states["moves"] = 0
    states["hiddenline"] = " "
    states["numbers"][0] = ""
    states["numbers"][1] = ""
    states["dot"] = 0
    calcline.set(states["hiddenline"])


"""
The following functions are used by all the different buttons in the interface 
to alter the states as needed, and to put the variables and operands on the calcline.
"""

def addone():
    if states["finished"] < 1:
        states["hiddenline"] += "1" 
        calcline.set(states["hiddenline"])
        states["numbers"][states["moves"]] += "1"
        try:
            if states["numbers"][states["moves"]].find(".") == -1:
                states["dot"] = 0
        except AttributeError:
            pass

def addtwo():
    if states["finished"] < 1:
        states["hiddenline"] += "2" 
        calcline.set(states["hiddenline"])
        states["numbers"][states["moves"]] += "2"
        try:
            if states["numbers"][states["moves"]].find(".") == -1:
                states["dot"] = 0
        except AttributeError:
            pass

def addthree():
    if states["finished"] < 1:
        states["hiddenline"] += "3" 
        calcline.set(states["hiddenline"])
        states["numbers"][states["moves"]] += "3"
        try:
            if states["numbers"][states["moves"]].find(".") == -1:
                states["dot"] = 0
        except AttributeError:
            pass

def addfour():
    if states["finished"] < 1:
        states["hiddenline"] += "4" 
        calcline.set(states["hiddenline"])
        states["numbers"][states["moves"]] += "4"
        try:
            if states["numbers"][states["moves"]].find(".") == -1:
                states["dot"] = 0
        except AttributeError:
            pass

def addfive():
    if states["finished"] < 1:
        states["hiddenline"] += "5" 
        calcline.set(states["hiddenline"])
        states["numbers"][states["moves"]] += "5"
        try:
            if states["numbers"][states["moves"]].find(".") == -1:
                states["dot"] = 0
        except AttributeError:
            pass

def addsix():
    if states["finished"] < 1:
        states["hiddenline"] += "6" 
        calcline.set(states["hiddenline"])
        states["numbers"][states["moves"]] += "6"
        try:
            if states["numbers"][states["moves"]].find(".") == -1:
                states["dot"] = 0
        except AttributeError:
            pass

def addseven():
    if states["finished"] < 1:
        states["hiddenline"] += "7" 
        calcline.set(states["hiddenline"])
        states["numbers"][states["moves"]] += "7"
        try:
            if states["numbers"][states["moves"]].find(".") == -1:
                states["dot"] = 0
        except AttributeError:
            pass

def addeight():
    if states["finished"] < 1:
        states["hiddenline"] += "8" 
        calcline.set(states["hiddenline"])
        states["numbers"][states["moves"]] += "8"
        try:
            if states["numbers"][states["moves"]].find(".") == -1:
                states["dot"] = 0
        except AttributeError:
            pass

def addnine():
    if states["finished"] < 1:
        states["hiddenline"] += "9" 
        calcline.set(states["hiddenline"])
        states["numbers"][states["moves"]] += "9"
        try:
            if states["numbers"][states["moves"]].find(".") == -1:
                states["dot"] = 0
        except AttributeError:
            pass

def addzero():
    if states["finished"] < 1:
        states["hiddenline"] += "0" 
        calcline.set(states["hiddenline"])
        states["numbers"][states["moves"]] += "0"
        try:
            if states["numbers"][states["moves"]].find(".") == -1:
                states["dot"] = 0
        except AttributeError:
            pass

def addplus():
    if states["moves"] != 1 and states["finished"] != 2:
        states["finished"] -= 1
        states["moves"] = 1
        states["hiddenline"] += "+"
        states["operand"] = "plus"
        try:
            if states["numbers"][states["moves"]].find(".") == -1:
                states["dot"] = 0
        except AttributeError:
            pass
        calcline.set(states["hiddenline"])

def addminus():
    if states["hiddenline"] == " " and states["hiddenline"] != "-":
        states["hiddenline"] += "-"
        calcline.set(states["hiddenline"])
        states["numbers"][0] += "-"
    elif states["moves"] != 1 and states["hiddenline"] != " " and states["finished"] != 2 and states["hiddenline"] != " -":
        states["finished"] -= 1
        states["moves"] = 1
        states["hiddenline"] += "-"
        states["operand"] = "minus"
        try:
            if states["numbers"][states["moves"]].find(".") == -1:
                states["dot"] = 0
        except AttributeError:
            pass
        calcline.set(states["hiddenline"])

def adddivide():
    if states["moves"] != 1 and states["finished"] != 2:
        states["finished"] -= 1
        states["moves"] = 1
        states["hiddenline"] += "/" 
        states["operand"] = "divide"
        try:
            if states["numbers"][states["moves"]].find(".") == -1:
                states["dot"] = 0
        except AttributeError:
            pass
        calcline.set(states["hiddenline"])

def addmultiply():
    if states["moves"] != 1 and states["finished"] != 2:
        states["finished"] -= 1
        states["moves"] = 1
        states["hiddenline"] += "*"
        states["operand"] = "multiply"
        try:
            if states["numbers"][states["moves"]].find(".") == -1:
                states["dot"] = 0
        except AttributeError:
            pass
        calcline.set(states["hiddenline"])

def addpower():
    if states["moves"] != 1 and states["finished"] != 2:
        states["finished"] -= 1
        states["moves"] = 1
        states["hiddenline"] += "^"
        states["operand"] = "power"
        try:
            if states["numbers"][states["moves"]].find(".") == -1:
                states["dot"] = 0
        except AttributeError:
            pass
        calcline.set(states["hiddenline"])

def addsquared():
    states["finished"] -= 1
    if states["moves"] != 1 and states["finished"] != 2:
        try:
            squared = float(states["hiddenline"]) ** 2
            states["hiddenline"] = str(squared)
            calcline.set(squared)
            states["numbers"][0] = str(squared)
            if states["numbers"][states["moves"]].find(".") == -1:
                states["dot"] = 0
            states["finished"] = 1
        except OverflowError:
            states["finished"] = 2
            calcline.set("Number too large, press clear")
        except ValueError:
            pass
            print("Error: Cant square without a variable")

def addpoint():
    if states["finished"] < 1 and states["dot"] < 1:
        states["numbers"][states["moves"]] += "."
        states["hiddenline"] += "."
        calcline.set(states["hiddenline"])
        states["dot"] = 1


"""
Configuring the interface, grid and different elements of the interface.
"""
root = Tk()
root.title("Calculator")
calcline = StringVar()

mainframe = ttk.Frame(root, padding="5 5 5 5")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, textvariable=calcline, font = ('Lucida Console', 15)).grid(column=1, row=1 , sticky=N, columnspan=5)

ttk.Button(mainframe, text="1", command=addone).grid(column=1, row=2, sticky=(N, W, S, E))
ttk.Button(mainframe, text="2", command=addtwo).grid(column=2, row=2, sticky=(N, W, S, E))
ttk.Button(mainframe, text="3", command=addthree).grid(column=3, row=2, sticky=(N, W, S, E))
ttk.Button(mainframe, text="+", command=addplus).grid(column=4, row=2, sticky=(N, W, S, E))
ttk.Button(mainframe, text="-", command=addminus).grid(column=5, row=2, sticky=(N, W, S, E))

ttk.Button(mainframe, text="4", command=addfour).grid(column=1, row=3, sticky=(N, W, S, E))
ttk.Button(mainframe, text="5", command=addfive).grid(column=2, row=3, sticky=(N, W, S, E))
ttk.Button(mainframe, text="6", command=addsix).grid(column=3, row=3, sticky=(N, W, S, E))
ttk.Button(mainframe, text="*", command=addmultiply).grid(column=4, row=3, sticky=(N, W, S, E))
ttk.Button(mainframe, text="/", command=adddivide).grid(column=5, row=3, sticky=(N, W, S, E))

ttk.Button(mainframe, text="7", command=addseven).grid(column=1, row=4, sticky=(N, W, S, E))
ttk.Button(mainframe, text="8", command=addeight).grid(column=2, row=4, sticky=(N, W, S, E))
ttk.Button(mainframe, text="9", command=addnine).grid(column=3, row=4, sticky=(N, W, S, E))
ttk.Button(mainframe, text="^", command=addpower).grid(column=4, row=4, sticky=(N, W, S, E))
ttk.Button(mainframe, text="x^2", command=addsquared).grid(column=5, row=4, sticky=(N, W, S, E))

ttk.Button(mainframe, text=".", command=addpoint).grid(column=1, row=5, sticky=(N, W, S, E))
ttk.Button(mainframe, text="0", command=addzero).grid(column=2, row=5, sticky=(N, W, S, E))
ttk.Button(mainframe, text="=", command=calculate).grid(column=3, row=5, sticky=(N, W, S, E))
ttk.Button(mainframe, text="clear", command=clear).grid(column=5, row=5, sticky=(N, W, S, E))

root.mainloop()
