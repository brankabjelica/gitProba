"""
Digitron
"""
import tkinter as tk

argument = ""

def press(num):
    global argument
    argument = argument + str(num)
    function.set(argument)
    
def equal():
    try:
        global argument
        result = str(eval(argument))
        function.set(result)
        argument = ""
    except:
        function.set("Error")
        argument = ""
        
def clear():
    global argument
    argument = ""
    function.set("")
    
if __name__ == "__main__":
    calc = tk.Tk()
    calc.title("Calculator")
    function = tk.StringVar()
    argument_field = tk.Entry(calc, textvariable=function)
    argument_field.grid(columnspan=4, ipadx=70)
    function.set("Enter your argument")
    
    b1 = tk.Button(calc, text="1", width=5, command=lambda: press(1))
    b1.grid(row=2, column=0)
    b2 = tk.Button(calc, text="2", width=5, command=lambda: press(2))
    b2.grid(row=2, column=1)
    b3 = tk.Button(calc, text="3", width=5, command=lambda: press(3))
    b3.grid(row=2, column=2)
    b4 = tk.Button(calc, text="4", width=5, command=lambda: press(4))
    b4.grid(row=3, column=0)
    b5 = tk.Button(calc, text="5", width=5, command=lambda: press(5))
    b5.grid(row=3, column=1)
    b6 = tk.Button(calc, text="6", width=5, command=lambda: press(6))
    b6.grid(row=3, column=2)
    b7 = tk.Button(calc, text="7", width=5, command=lambda: press(7))
    b7.grid(row=4, column=0)
    b8 = tk.Button(calc, text="8", width=5, command=lambda: press(8))
    b8.grid(row=4, column=1)
    b9 = tk.Button(calc, text="9", width=5, command=lambda: press(9))
    b9.grid(row=4, column=2)
    b0 = tk.Button(calc, text="0", width=5, command=lambda: press(0))
    b0.grid(row=5, column=0)
    cl = tk.Button(calc, text="Clear", width=5, command=clear) 
    cl.grid(row=5, column=1)
    eql = tk.Button(calc, text="=", width=5, command=equal) 
    eql.grid(row=5, column=2)
    plus = tk.Button(calc, text="+", width=5, command=lambda: press("+")) 
    plus.grid(row=2, column=3)
    minus = tk.Button(calc, text="-", width=5, command=lambda: press("-")) 
    minus.grid(row=3, column=3)
    multiply = tk.Button(calc, text="*", width=5, command=lambda: press("*")) 
    multiply.grid(row=4, column=3)
    divide = tk.Button(calc, text="/", width=5, command=lambda: press("/")) 
    divide.grid(row=5, column=3)

    calc.mainloop()
    
