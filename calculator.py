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

def addnum(num):
    if states["finished"] < 1:
        states["hiddenline"] += "{}".format(num) 
        calcline.set(states["hiddenline"])
        states["numbers"][states["moves"]] += "{}".format(num)
        try:
            if states["numbers"][states["moves"]].find(".") == -1:
                states["dot"] = 0
        except AttributeError:
            pass

def addop(op):
    if states["moves"] != 1 and states["finished"] != 2:
        states["finished"] -= 1
        states["moves"] = 1
        if op == "+":
            states["hiddenline"] += "+"
            states["operand"] = "plus"
        if op == "-":
            if states["hiddenline"] == " " and states["hiddenline"] != " -" and states["finished"] != 2:
                states["moves"] = 0
                states["hiddenline"] += "-"
                calcline.set(states["hiddenline"])
                states["numbers"][0] += "-"
            elif states["hiddenline"] != " " and states["finished"] != 2 and states["hiddenline"] != " -":
                states["hiddenline"] += "-"
                states["operand"] = "minus"
        elif op == "/":
            states["hiddenline"] += "/"
            states["operand"] = "divide"
        elif op == "*":
            states["hiddenline"] += "*"
            states["operand"] = "multiply"
        elif op == "^":
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

Label(mainframe, textvariable=calcline, font = ('Lucida Console', 15), height=2).grid(column=1, row=1 , sticky=N, columnspan=6)

Button(mainframe, text="1", command=lambda: addnum(1), height=3, width=10, activebackground="darkgray").grid(column=1, row=2, sticky=(N, W, S, E))
Button(mainframe, text="2", command=lambda: addnum(2), height=3, width=10, activebackground="darkgray").grid(column=2, row=2, sticky=(N, W, S, E))
Button(mainframe, text="3", command=lambda: addnum(3), height=3, width=10, activebackground="darkgray").grid(column=3, row=2, sticky=(N, W, S, E))
Button(mainframe, text="+", command=lambda: addop("+"), height=3, width=10, activebackground="darkgray").grid(column=5, row=2, sticky=(N, W, S, E))
Button(mainframe, text="-", command=lambda: addop("-"), height=3, width=10, activebackground="darkgray").grid(column=6, row=2, sticky=(N, W, S, E))

Button(mainframe, text="4", command=lambda: addnum(4), height=3, width=5, activebackground="darkgray").grid(column=1, row=3, sticky=(N, W, S, E))
Button(mainframe, text="5", command=lambda: addnum(5), height=3, width=5, activebackground="darkgray").grid(column=2, row=3, sticky=(N, W, S, E))
Button(mainframe, text="6", command=lambda: addnum(6), height=3, width=5, activebackground="darkgray").grid(column=3, row=3, sticky=(N, W, S, E))
Button(mainframe, text="*", command=lambda: addop("*"), height=3, width=5, activebackground="darkgray").grid(column=5, row=3, sticky=(N, W, S, E))
Button(mainframe, text="/", command=lambda: addop("/"), height=3, width=5, activebackground="darkgray").grid(column=6, row=3, sticky=(N, W, S, E))

Button(mainframe, text="7", command=lambda: addnum(7), height=3, width=5, activebackground="darkgray").grid(column=1, row=4, sticky=(N, W, S, E))
Button(mainframe, text="8", command=lambda: addnum(8), height=3, width=5, activebackground="darkgray").grid(column=2, row=4, sticky=(N, W, S, E))
Button(mainframe, text="9", command=lambda: addnum(9), height=3, width=5, activebackground="darkgray").grid(column=3, row=4, sticky=(N, W, S, E))
Button(mainframe, text="^", command=lambda: addop("^"), height=3, width=5, activebackground="darkgray").grid(column=5, row=4, sticky=(N, W, S, E))
Button(mainframe, text="x^2", command=addsquared, height=3, width=5, activebackground="darkgray").grid(column=6, row=4, sticky=(N, W, S, E))

Button(mainframe, text=".", command=addpoint, height=3, width=5, activebackground="darkgray").grid(column=1, row=5, sticky=(N, W, S, E))
Button(mainframe, text="0", command=lambda: addnum(0), height=3, width=5, activebackground="darkgray").grid(column=2, row=5, sticky=(N, W, S, E))
Button(mainframe, text="=", command=calculate, height=3, width=5, activebackground="darkgray").grid(column=3, row=5, sticky=(N, W, S, E))
Button(mainframe, text="clear", command=clear, height=3, width=5, activebackground="darkgray").grid(column=5, row=5, sticky=(N, W, S, E))

root.mainloop()
