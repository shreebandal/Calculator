from tkinter import *
import math

def click(event):
    text = event.widget.cget("text")
    if text == "X":
        text = "*"
    elif text == "pow":
        text = "**"
    elif text == "sqrt":
        text = "**0.5"
    elif text == "sqr":
        text = "**2"
    elif text == "fact":
        text=""
        window.num.set(math.factorial(eval(window.num.get())))
    elif text == "sin":
        text=""
        window.num.set(math.sin(eval(window.num.get())))
    elif text == "cos":
        text=""
        window.num.set(math.cos(eval(window.num.get())))
    elif text == "tan":
        text=""
        window.num.set(math.tan(eval(window.num.get())))
    elif text == "log":
        text=""
        window.num.set(math.log10(eval(window.num.get())))
    elif text == "1/x":
        text = "**-1"
    elif text == "<":
        text = ""
        if window.num.get()[len(window.num.get())-1].isdigit():
            Count = 0
            Number = int(window.num.get())
            while Number:
                Number = Number // 10
                Count += 1
            if Count <= 1:
                window.num.set(0)
            else:
                window.num.set(window.num.get()[0:len(window.num.get()) - 1])
    if text == "C":
        window.num.set(0)
    elif window.num.get() == "Error":
        window.num.set(text)
    elif window.num.get() == "0":
        if text.isdigit():
            window.num.set(text)
        else:
            if text == "=":
                window.num.set(0)
            else:
                window.num.set("0"+text)
    elif text == "=":
        end = window.num.get()[len(window.num.get())-1]
        if end.isdigit():
            window.num.set(eval(window.num.get()))
        else:
            window.num.set("Error")
    else:
        end = window.num.get()[len(window.num.get()) - 1]
        if end.isdigit():
            window.num.set(window.num.get()+text)
        else:
            if text.isdigit():
                window.num.set(window.num.get() + text)
            else:
                window.num.set(window.num.get()[0:len(window.num.get()) - 1]+text)

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.wm_iconbitmap("cal.ico")
        self.title("Calculator")
        self.geometry("520x610")
        self.minsize(520,610)
        self.maxsize(520,610)

    def outputScreen(self):
        self.num = StringVar()
        self.numentry = Entry(self, textvar=self.num,font="lucida 30")
        self.numentry.pack(fill=X,padx=10,pady=10)
        self.num.set(0)

    def makeFrame(self):
        self.frame = Frame(self)
        self.frame.pack()

    def makeButton(self,btn,len):
        if len == 4:
            self.btn = Button(self.frame,text=f"{btn}",font="lucida 25")
        elif len == 3:
            self.btn = Button(self.frame, text=f"{btn}", padx=3, font="lucida 25")
        else:
            self.btn = Button(self.frame, text=f"{btn}", padx=16, font="lucida 25")

        self.btn.pack(side=LEFT, padx=10, pady=5)
        self.btn.bind('<Button-1>', click)

if __name__=='__main__':
    window = GUI()
    window.outputScreen()
    mylist = [["sqrt","fact","sin","cos","("],["<", "sqr", "log", "tan", ")"],["C", "7", "8", "9", "="],
              ["X","4","5","6","+"],["%","1","2","3","/"],["pow","1/x", "0", "-", "."]]
    for sublist in mylist:
        window.makeFrame()
        for i in sublist:
            window.makeButton(i,len(i))
    window.mainloop()