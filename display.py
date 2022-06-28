import tkinter as tk
from tkinter import StringVar


window = tk.Tk()
window.title('Calculator')
window.geometry('200x250')

expression = ''
equation = StringVar()


def press(num):
    global expression

    # concatenation of string
    expression = expression + str(num)
 
    # update the expression by using set method
    equation.set(expression)

def enter():
    global expression

    try:
        total = str(eval(expression))
        equation.set(total)
        expression = ''
    except:
        equation.set('error')
        expression = ''



def clear():
    global expression
    
    expression = ''
    equation.set('')


def average():
    pass
 
display = tk.Entry(window, textvariable=equation, fg='black', bg='light green', width=32,)
display.place(x=0, y=0)

button_enter = tk.Button(window, text='=', command=enter, bg='orange', fg='white', width=5, height=3)
button_enter.place(x=150, y=130)

button_plus = tk.Button(window,text='+',command=lambda:press('+'), bg='grey', fg='white', width=5,height=1)
button_plus.place(x=150, y=100)

button_minus = tk.Button(window,text='-',command=lambda: press('-'),bg='grey',fg='white',width=5,height=1)
button_minus.place(x=150, y=70)

button_multiply = tk.Button(window,text='*',command=lambda: press('*'),bg='black',fg='white',width=5,height=1)
button_multiply.place(x=150, y=40)

button_divide = tk.Button(window,text='/',command=lambda: press('/'),bg='black',fg='white',width=5,height=1)
button_divide.place(x=100, y=40)


button_erase = tk.Button(window,text='C',command=clear, bg='black',fg='white',width=5,height=1)
button_erase.place(x=0, y=40)

button_average = tk.Button(window,text='AV',command=average(),bg='black',fg='white',width=5,height=1)
button_average.place(x=50, y=40)

button_zero = tk.Button(window,text='0',command=lambda:press(0),bg='grey',fg='white',width=12,height=1)
button_zero.place(x=0, y=160)

button_dot = tk.Button(window,text='.',command=lambda:press('.'),bg='grey',fg='white',width=5,height=1)
button_dot.place(x=100, y=160)

button1 = tk.Button(window,text='1', command=lambda: press(1), bg='grey', fg='white', width=5,height=1)
button1.place(x=0, y=130)

button2 = tk.Button(window,text='2',command=lambda: press(2),bg='grey',fg='white',width=5,height=1)
button2.place(x=50, y=130)

button3 = tk.Button(window,text='3',command=lambda: press(3),bg='grey',fg='white',width=5,height=1)
button3.place(x=100, y=130)

button4 = tk.Button(window,text='4',command=lambda: press(4),bg='grey',fg='white',width=5,height=1)
button4.place(x=0, y=100)

button5 = tk.Button(window,text='5',command=lambda: press(5),bg='grey',fg='white',width=5,height=1)
button5.place(x=50, y=100)

button6 = tk.Button(window,text='6',command=lambda: press(6),bg='grey',fg='white',width=5,height=1)
button6.place(x=100, y=100)

button7 = tk.Button(window,text='7',command=lambda: press(7),bg='grey',fg='white',width=5,height=1)
button7.place(x=0, y=70)

button8 = tk.Button(window,text='8',command=lambda: press(8),bg='grey',fg='white',width=5,height=1)
button8.place(x=50, y=70)

button9 = tk.Button(window,text='9',command=lambda: press(9),bg='grey',fg='white',width=5,height=1)
button9.place(x=100, y=70)


window.mainloop()