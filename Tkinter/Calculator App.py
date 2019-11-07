#Kush Kansara
#April 22nd, 2018
#Calculator Assignment

# The purpose of this code was the create a simple calculator with the functions +, -, x, /

from tkinter import *
from math import pi, sqrt
root = Tk()

class Calculator:
#class of calculator and its operations
    def __init__(self, master):
        global root
        root.geometry("550x700")
        root.resizable(height = False, width = False)
        
        global display
        display = ""
        dispw = 10
        disph = 8
        buttonfg = "black"
        buttonbg = "#20f1fc"
        button2fg = "black"
        button2bg = "#f29b37"
        button3fg = "black"
        button3bg = "#f29b37"
        txtfont = ("Arial", 10)
        
        self.master = master
        master.title("Calculator")

        #top display
        self.expression = StringVar()
        self.total_label = Label(master, textvariable = self.expression, bg = "#2de285", fg = "white", justify = "center", height = 4, font = ("Arial", 20)).grid(row=0, columnspan = 64, sticky = E + W)

        #number buttons
        Button(root, text = "1", font = txtfont, height = disph, fg = buttonfg, bg = buttonbg, padx = 2, pady = 2, width = dispw, command = lambda: self.add_to_display("1")).grid(row = 1, column = 0)
        Button(root, text = "2", font = txtfont, height = disph, fg = buttonfg, bg = buttonbg, padx = 2, pady = 2, width = dispw, command = lambda: self.add_to_display("2")).grid(row = 1, column = 1)
        Button(root, text = "3", font = txtfont, height = disph, fg = buttonfg, bg = buttonbg, padx = 2, pady = 2, width = dispw, command = lambda: self.add_to_display("3")).grid(row = 1, column = 2)
        Button(root, text = "4", font = txtfont, height = disph, fg = buttonfg, bg = buttonbg, padx = 2, pady = 2, width = dispw, command = lambda: self.add_to_display("4")).grid(row = 2, column = 0)
        Button(root, text = "5", font = txtfont, height = disph, fg = buttonfg, bg = buttonbg, padx = 2, pady = 2, width = dispw, command = lambda: self.add_to_display("5")).grid(row = 2, column = 1)
        Button(root, text = "6", font = txtfont, height = disph, fg = buttonfg, bg = buttonbg, padx = 2, pady = 2, width = dispw, command = lambda: self.add_to_display("6")).grid(row = 2, column = 2)
        Button(root, text = "7", font = txtfont, height = disph, fg = buttonfg, bg = buttonbg, padx = 2, pady = 2, width = dispw, command = lambda: self.add_to_display("7")).grid(row = 3, column = 0)
        Button(root, text = "8", font = txtfont, height = disph, fg = buttonfg, bg = buttonbg, padx = 2, pady = 2, width = dispw, command = lambda: self.add_to_display("8")).grid(row = 3, column = 1)
        Button(root, text = "9", font = txtfont, height = disph, fg = buttonfg, bg = buttonbg, padx = 2, pady = 2, width = dispw, command = lambda: self.add_to_display("9")).grid(row = 3, column = 2)
        Button(root, text = "0", font = txtfont, height = disph, fg = buttonfg, bg = buttonbg, padx = 2, pady = 2, width = dispw, command = lambda: self.add_to_display("0")).grid(row = 4, column = 1)

        #operational buttons
        Button(root, text = "+", font = txtfont, height = disph, fg = button2fg, bg = button2bg, padx = 2, pady = 2, width = dispw, command = lambda: self.add_to_display("+")).grid(row = 1, column = 3)
        Button(root, text = "-", font = txtfont, height = disph, fg = button2fg, bg = button2bg, padx = 2, pady = 2, width = dispw, command = lambda: self.add_to_display("-")).grid(row = 2, column = 3)
        Button(root, text = "*", font = txtfont, height = disph, fg = button2fg, bg = button2bg, padx = 2, pady = 2, width = dispw, command = lambda: self.add_to_display("*")).grid(row = 3, column = 3)
        Button(root, text = "/", font = txtfont, height = disph, fg = button2fg, bg = button2bg, padx = 2, pady = 2, width = dispw, command = lambda: self.add_to_display("/")).grid(row = 4, column = 3)
        Button(root, text = "=", font = txtfont, height = disph, fg = button2fg, bg = button2bg, padx = 2, pady = 2, width = dispw, command = lambda: self.equal_sign()).grid(row = 4, column = 2)
        Button(root, text = "c", font = txtfont, height = disph, fg = button3fg, bg = button3bg, padx = 2, pady = 2, width = dispw, command = lambda: self.clear_display()).grid(row = 4, column = 4)
        Button(root, text = "←", font = txtfont, height = disph, fg = button3fg, bg = button3bg, padx = 2, pady = 2, width = 22, command = lambda: self.back_space()).grid(row = 1, column = 4, columnspan = 3, sticky = W)
        Button(root, text = "(", font = txtfont, height = disph, fg = button3bg, bg = button3bg, padx = 2, pady = 2, width = dispw, command = lambda: self.add_to_display("(")).grid(row = 2, column = 4)
        Button(root, text = ")", font = txtfont, height = disph, fg = button3fg, bg = button3bg, padx = 2, pady = 2, width = dispw, command = lambda: self.add_to_display(")")).grid(row = 2, column = 5)
        Button(root, text = ".", font = txtfont, height = disph, fg = button2fg, bg = button2bg, padx = 2, pady = 2, width = dispw, command = lambda: self.add_to_display(".")).grid(row = 4, column = 0)
        Button(root, text = "π", font = txtfont, height = disph, fg = button3fg, bg = button3bg, padx = 2, pady = 2, width = dispw, command = lambda: self.add_to_display("pi")).grid(row = 4, column = 5)
        Button(root, text = "^", font = txtfont, height = disph, fg = button3fg, bg = button3bg, padx = 2, pady = 2, width = dispw, command = lambda: self.add_to_display("**")).grid(row = 3, column = 5)
        Button(root, text = "√", font = txtfont, height = disph, fg = button3fg, bg = button3bg, padx = 2, pady = 2, width = dispw, command = lambda: self.add_to_display("sqrt(")).grid(row = 3, column = 4)
        
        

    def add_to_display(self, text):
        global display
        display = display + text

        if len(display) > 2:
            if display[-2] != "(":
                self.expression.set(display)
            else:
                display = display + ")"
                self.expression.set(display)
        else:
            self.expression.set(display) 

    def clear_display(self):
        global display
        display = ""
        self.expression.set(display)

    def equal_sign(self):
        global display
        try:
            answer = eval(display)
            display = str(answer)
            self.expression.set(display)

        except SyntaxError or ValueError:
            self.expression.set("Invalid Syntax, Try Again")
            display = ""

    def back_space(self):
        global display
        display = display[:-1]
        self.expression.set(display)
        

calc_gui = Calculator(root)
root.mainloop()
