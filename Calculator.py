# We will make a calculator

import tkinter as tk
import tkinter.messagebox as tmsg
import math

root = tk.Tk()

root.title("Calculator")
root.iconbitmap("Calculator icon.ico")
i = 0 #keeps track of current position on input text field
#define the function to insert num at ith position
def get_num(num):
    global i
    screen.insert(i, num)
    i+=1
    
def get_op(exp):
    global i 
    screen.insert(i, exp)
    i+=1
    
def all_clear():
    screen.delete(0, tk.END)
    
def clear():
    entire_string = screen.get()
    try:
        all_clear()
        screen.insert(0, entire_string[:-1])
    except:
        all_clear()
        
def calc():
    string = screen.get()
    try:
        all_clear()
        screen.insert(0, eval(string))
    except:
        all_clear()
        tmsg.showinfo("Error", "There was an error")

# define trigonometric functions
# TODO Remeber to optimize by taking trigonometric expressions
def sin():
    try:
        num = math.sin(float(screen.get()))
        all_clear()
        screen.insert(0,num)
    except:
        all_clear()
        tmsg.showinfo("Error", "There was an error")
    
def cos():
    try:
        num = math.cos(float(screen.get()))
        all_clear()
        screen.insert(0,num)
    except:
        all_clear()
        tmsg.showinfo("Error", "There was an error")
        
def tan():
    try:
        num = math.tan(float(screen.get()))
        all_clear()
        screen.insert(0,num)
        
    except:
        all_clear()
        tmsg.showinfo("Error", "There was an error")
        
def inv_sin():
    try:
        num = math.asin(float(screen.get()))
        all_clear()
        screen.insert(0,math.degrees(num))
    except:
        all_clear()
        tmsg.showinfo("Error", "There was an error") 
        
def inv_cos():
    try:
        num = math.acos(float(screen.get()))
        all_clear()
        screen.insert(0,math.degrees(num))
    except:
        all_clear()
        tmsg.showinfo("Error", "There was an error") 

def inv_tan():
    try:
        num = math.atan(float(screen.get()))
        all_clear()
        screen.insert(0,math.degrees(num))
        
    except:
        all_clear()
        tmsg.showinfo("Error", "There was an error")         

# define a key binding function to bind '=' to 'Enter'
#def calc1(event):
 #   string = screen.get()
  #  try:
   #     all_clear()
   #     screen.insert(0, eval(string))
    #except:
     #   all_clear()
      #  tmsg.showinfo("Error", "There was an error")
    
# define factorial function        
def fact():
    try:
        num = math.factorial(float(screen.get()))
        all_clear()
        screen.insert(0, num)
    except:
        all_clear()
        tmsg.showinfo("Error", "There was an error")
        
#screen entry
screen = tk.Entry(root, font = 'lucida 30 bold')
screen.grid(row = 1, columnspan = 6, sticky = 'n'+'w'+'e'+'s')


#Buttons for numbers
b=tk.Button(root, text = "7", command = lambda: get_num(7)).grid(row = 2, column = 0, sticky = 'n'+'w'+'e'+'s')
b=tk.Button(root, text = '8', command = lambda: get_num(8)).grid(row = 2, column = 1, sticky = 'n'+'w'+'e'+'s')
b=tk.Button(root, text = '9', command = lambda: get_num(9)).grid(row = 2, column = 2, sticky = 'n'+'w'+'e'+'s')

b=tk.Button(root, text = '4', command = lambda: get_num(4)).grid(row = 3, column = 0, sticky = 'n'+'w'+'e'+'s')
b=tk.Button(root, text = '5', command = lambda: get_num(5)).grid(row = 3, column = 1, sticky = 'n'+'w'+'e'+'s')
b=tk.Button(root, text = '6', command = lambda: get_num(6)).grid(row = 3, column = 2, sticky = 'n'+'w'+'e'+'s')

b=tk.Button(root, text = '1', command = lambda: get_num(1)).grid(row = 4, column = 0, sticky = 'n'+'w'+'e'+'s')
b=tk.Button(root, text = '2', command = lambda: get_num(2)).grid(row = 4, column = 1, sticky = 'n'+'w'+'e'+'s')
b=tk.Button(root, text = '3', command = lambda: get_num(3)).grid(row = 4, column = 2, sticky = 'n'+'w'+'e'+'s')

b=tk.Button(root, text = '+', command = lambda : get_op("+")).grid(row = 2, column = 3, sticky = 'n'+'w'+'e'+'s')
b=tk.Button(root, text = '<-', command = lambda: clear()).grid(row = 2, column = 4, sticky = 'n'+'w'+'e'+'s')
b=tk.Button(root, text = 'C', command = lambda: all_clear()).grid(row = 2, column = 5, sticky = 'n'+'w'+'e'+'s')

b=tk.Button(root, text = '-', command = lambda: get_op("-")).grid(row = 3, column = 3, sticky = 'n'+'w'+'e'+'s')
b=tk.Button(root, text = '%', command = lambda: get_op("%")).grid(row = 3, column = 4, sticky = 'n'+'w'+'e'+'s')
b=tk.Button(root, text = '(x)!', command = lambda: fact()).grid(row = 3, column = 5, sticky = 'n'+'w'+'e'+'s')

b=tk.Button(root, text = '*', command = lambda: get_op("*")).grid(row = 4, column = 3, sticky = 'n'+'w'+'e'+'s')
b=tk.Button(root, text = '(', command = lambda: get_op("(")).grid(row = 4, column = 4, sticky = 'n'+'w'+'e'+'s')
b=tk.Button(root, text = ')', command = lambda: get_op(")")).grid(row = 4, column = 5, sticky = 'n'+'w'+'e'+'s')

b=tk.Button(root, text = 'pi', command = lambda: get_op("3.1459")).grid(row = 5, column = 0, sticky = 'n'+'w'+'e'+'s')
b=tk.Button(root, text = '0', command = lambda: get_num(0)).grid(row = 5, column = 1, sticky = 'n'+'w'+'e'+'s')
b=tk.Button(root, text = '.', command = lambda: get_num(".")).grid(row = 5, column = 2, sticky = 'n'+'w'+'e'+'s')
b=tk.Button(root, text = '/', command = lambda: get_op("/")).grid(row = 5, column = 3, sticky = 'n'+'w'+'e'+'s')
b=tk.Button(root, text = 'exp', command = lambda: get_op("2.71828")).grid(row = 5, column = 4, sticky = 'n'+'w'+'e'+'s')
b=tk.Button(root, text = '^', command = lambda: get_op("**")).grid(row = 5, column = 5, sticky = 'n'+'w'+'e'+'s')

b=tk.Button(root, text = 'sin', command = lambda: sin()).grid(row = 6, column = 0, sticky = 'n'+'w'+'e'+'s')
b=tk.Button(root, text = 'cos', command = lambda: cos()).grid(row = 6, column = 1, sticky = 'n'+'w'+'e'+'s')
b=tk.Button(root, text = 'tan', command = lambda: tan()).grid(row = 6, column = 2, sticky = 'n'+'w'+'e'+'s')
b=tk.Button(root, text = 'Inv sin', command = lambda: inv_sin()).grid(row = 6, column = 3, sticky = 'n'+'w'+'e'+'s')
b=tk.Button(root, text = 'Inv cos', command = lambda: inv_cos()).grid(row = 6, column = 4, sticky = 'n'+'w'+'e'+'s')
b=tk.Button(root, text = 'Inv tan', command = lambda: inv_tan()).grid(row = 6, column = 5, sticky = 'n'+'w'+'e'+'s')

b1=tk.Button(root, text = '=', command = lambda: calc(), borderwidth = 5, relief = 'raised')
b1.grid(row = 7, columnspan = 6, sticky = 'n'+'w'+'e'+'s')

root.mainloop()