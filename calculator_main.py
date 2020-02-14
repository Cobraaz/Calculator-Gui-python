from tkinter import *
from tkinter.messagebox import *
import math as m

# Some useful variable
font = ('Verdana', 18, 'bold')
window = Tk()


# important function
def all_clear():
    textField.delete(0, END)


def clear():
    ex = textField.get()
    ex = ex[0:len(ex) - 1]
    textField.delete(0, END)
    textField.insert(0, ex)


def click_btn_function(event):
    print('btn clicked')
    b = event.widget
    text = b['text']
    print(text)

    if text == 'x':
        textField.insert(END, '*')
        return

    if text == '=':
        try:
            ex = textField.get()
            anser = eval(ex)
            textField.delete(0, END)
            textField.insert(0, anser)
        except Exception as e:
            print('Error..', e)
            showerror('Error', e)
        return
    textField.insert(END, text)


# creating a window

window.title('My Calculator')
window.geometry('465x450')

# Picture label
pic = PhotoImage(file='cal2.png')
headingLabel = Label(window, image=pic)
headingLabel.pack(side=TOP, pady=10)

# heading level
heading = Label(window, text='My Calculator', font=font, underline=0)
heading.pack(side=TOP)

# textfield
textField = Entry(window, font=font, justify=CENTER)
textField.pack(side=TOP, pady=10, fill=X, padx=10)

# Button
buttonFrame = Frame(window)
buttonFrame.pack(side=TOP, padx=10)

# adding button
temp = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn = Button(buttonFrame, text=str(temp), font=font, width=5, relief='ridge', activebackground='orange',
                     activeforeground='white')
        btn.grid(row=i, column=j)
        temp = temp + 1
        btn.bind('<Button-1>', click_btn_function)

zeroBtn = Button(buttonFrame, text='0', font=font, width=5, relief='ridge', activebackground='orange',
                 activeforeground='white')
zeroBtn.grid(row=3, column=0)

dotBtn = Button(buttonFrame, text='.', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
dotBtn.grid(row=3, column=1)

equalBtn = Button(buttonFrame, text='=', font=font, width=5, relief='ridge', activebackground='orange',
                  activeforeground='white')
equalBtn.grid(row=3, column=2)

plusBtn = Button(buttonFrame, text='+', font=font, width=5, relief='ridge', activebackground='orange',
                 activeforeground='white')
plusBtn.grid(row=0, column=3)

minusBtn = Button(buttonFrame, text='-', font=font, width=5, relief='ridge', activebackground='orange',
                  activeforeground='white')
minusBtn.grid(row=1, column=3)

multBtn = Button(buttonFrame, text='x', font=font, width=5, relief='ridge', activebackground='orange',
                 activeforeground='white')
multBtn.grid(row=2, column=3)

divideBtn = Button(buttonFrame, text='/', font=font, width=5, relief='ridge', activebackground='orange',
                   activeforeground='white')
divideBtn.grid(row=3, column=3)

clearBtn = Button(buttonFrame, text='<--', font=font, width=11, relief='ridge', activebackground='orange',
                  activeforeground='white', command=clear)
clearBtn.grid(row=4, column=0, columnspan=2)

allclearBtn = Button(buttonFrame, text='AC', font=font, width=11, relief='ridge', activebackground='orange',
                     activeforeground='white', command=all_clear)
allclearBtn.grid(row=4, column=2, columnspan=2)

# binding button
plusBtn.bind('<Button-1>', click_btn_function)
minusBtn.bind('<Button-1>', click_btn_function)
multBtn.bind('<Button-1>', click_btn_function)
divideBtn.bind('<Button-1>', click_btn_function)
zeroBtn.bind('<Button-1>', click_btn_function)
dotBtn.bind('<Button-1>', click_btn_function)
equalBtn.bind('<Button-1>', click_btn_function)


def enterClick(event):
    print('hi')
    e = Event()
    e.widget = equalBtn
    click_btn_function(e)


textField.bind('<Return>', enterClick)
#############################################################################################
# Scientific function
scFrame = Frame(window)

sqrtBtn = Button(scFrame, text='√', font=font, width=5, relief='ridge', activebackground='orange',
                 activeforeground='white')
sqrtBtn.grid(row=0, column=0)

powBtn = Button(scFrame, text='^', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
powBtn.grid(row=0, column=1)
factBtn = Button(scFrame, text='x!', font=font, width=5, relief='ridge', activebackground='orange',
                 activeforeground='white')
factBtn.grid(row=0, column=2)
radBtn = Button(scFrame, text='toRad', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
radBtn.grid(row=0, column=3)

defBtn = Button(scFrame, text='toDeg', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
defBtn.grid(row=1, column=0)
sinBtn = Button(scFrame, text='sinƟ', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
sinBtn.grid(row=1, column=1)
cosBtn = Button(scFrame, text='cosƟ', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
cosBtn.grid(row=1, column=2)

tanBtn = Button(scFrame, text='tanƟ', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
tanBtn.grid(row=1, column=3)

normalcalc = True


def calculate_sc(event):
    print('btn..')
    btn = event.widget
    text = btn['text']
    print(text)
    answer = ''
    ex = textField.get()
    if text == 'toDeg':
        print('cal degree')
        answer = str(m.degrees(float(ex)))
    elif text == 'toRad':
        print('radian')
        answer = str(m.radians(float(ex)))
    elif text == 'x!':
        print('cal factorial')
        answer = str(m.factorial(int(ex)))
    elif text == 'sinƟ':
        print('cal sin')
        answer = str(m.sin(m.radians(int(ex))))
    elif text == 'cosƟ':
        print('cal cos')
        answer = str(m.cos(m.radians(int(ex))))
    elif text == 'tanƟ':
        print('cal tan')
        answer = str(m.tan(m.radians(int(ex))))
    elif text == '√':
        print('cal sqrt')
        answer = str(m.sqrt(int(ex)))
    elif text == '^':
        print('cal power')
        base, pow = ex.split('^')
        answer = m.pow(int(base), int(pow))

    textField.delete(0, END)
    textField.insert(0, answer)


def sc_click():
    global normalcalc
    if normalcalc:
        # sc...
        buttonFrame.pack_forget()
        # add sc frame
        scFrame.pack(side=TOP, pady=20)
        buttonFrame.pack(side=TOP)
        window.geometry('465x590')

        print('show sc')
        normalcalc = False
    else:
        print('show normal')
        scFrame.pack_forget()
        window.geometry('465x450')
        normalcalc = True


# binding function
sqrtBtn.bind('<Button-1>', calculate_sc)
powBtn.bind('<Button-1>', calculate_sc)
factBtn.bind('<Button-1>', calculate_sc)
radBtn.bind('<Button-1>', calculate_sc)
defBtn.bind('<Button-1>', calculate_sc)
sinBtn.bind('<Button-1>', calculate_sc)
cosBtn.bind('<Button-1>', calculate_sc)
tanBtn.bind('<Button-1>', calculate_sc)

fontMenu = ('', 11)
menubar = Menu(window)
mode = Menu(menubar, font=fontMenu, tearoff=0)
mode.add_checkbutton(label='Scientific Calculator', command=sc_click)

menubar.add_cascade(label="Mode", menu=mode)

window.config(menu=menubar)

window.mainloop()
