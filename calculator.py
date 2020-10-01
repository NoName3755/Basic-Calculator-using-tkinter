from tkinter import *

# making the window for calculator
root = Tk()
root.geometry("350x460")
root.minsize = root.maxsize(350, 460)
root.title("Calculator by Milan")


# making the click function
def click(event):
    global scvalue
    # extracting the value from the button
    text = event.widget.cget("text")

    # making the function of '='
    if text == "=":
        try:
            # if it is number
            if scvalue.get().isdigit():
                value = int(scvalue.get())

            # if expression then calculate
            else:
                value = eval(screen.get())
            scvalue.set(value)
            # Must be update coz it value won't show
            screen.update()

        # Handling the wrong statement
        except Exception as e:
            scvalue.set("Invalid Syntax!!")
            screen.update()
    # making the function of "C"
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


# making the blank text window
scvalue = StringVar()
scvalue.set("")

# making the Entry part where display what we click
screen = Entry(root, textvar=scvalue, font="lucida 30 bold")
screen.pack(fill=X, ipadx=6, pady=10, padx=10)

# making the frame and pack on the root and putting the button on the frame
f = Frame(root, bg="gray")
b = Button(f, text="C", font="lucida 25 bold", padx=17)
b.grid(row=0, column=0)
b.bind("<Button-1>", click)  # click one time call "click" function

b = Button(f, text="/", font="lucida 25 bold", padx=24.5)
b.grid(row=0, column=1)
b.bind("<Button-1>", click)  # click one time call "click" function

b = Button(f, text="*", font="lucida 25 bold", padx=22)
b.grid(row=0, column=2)
b.bind("<Button-1>", click)  # click one time call "click" function

b = Button(f, text="-", font="lucida 25 bold", padx=29)
b.grid(row=0, column=3)
b.bind("<Button-1>", click)  # click one time call "click" function
f.pack(anchor="nw")

# making the frame and pack on the root and putting the button on the frame
f = Frame(root, bg="gray")
b = Button(f, text="7", font="lucida 25 bold", padx=20)
b.grid(row=0, column=0)
b.bind("<Button-1>", click)

b = Button(f, text="8", font="lucida 25 bold", padx=20)
b.grid(row=0, column=1)
b.bind("<Button-1>", click)

b = Button(f, text="9", font="lucida 25 bold", padx=20)
b.grid(row=0, column=2)
b.bind("<Button-1>", click)


b = Button(f, text="+", font="lucida 25 bold", padx=24)
b.grid(row=0, column=3, rowspan=2, sticky=N+S)
b.bind("<Button-1>", click)

b = Button(f, text="4", font="lucida 25 bold", padx=20)
b.grid(row=1, column=0)
b.bind("<Button-1>", click)

b = Button(f, text="5", font="lucida 25 bold", padx=20)
b.grid(row=1, column=1)
b.bind("<Button-1>", click)

b = Button(f, text="6", font="lucida 25 bold", padx=20)
b.grid(row=1, column=2)
b.bind("<Button-1>", click)

b = Button(f, text="1", font="lucida 25 bold", padx=20)
b.grid(row=2, column=0)
b.bind("<Button-1>", click)

b = Button(f, text="2", font="lucida 25 bold", padx=20)
b.grid(row=2, column=1)
b.bind("<Button-1>", click)

b = Button(f, text="3", font="lucida 25 bold", padx=20)
b.grid(row=2, column=2)
b.bind("<Button-1>", click)

b = Button(f, text="0", font="lucida 25 bold", padx=20)
# expanding the '0' in east and west direction, E means East and w means west
b.grid(row=3, column=0, columnspan=2, sticky=E+W)
b.bind("<Button-1>", click)

b = Button(f, text=".", font="lucida 25 bold", padx=24.5)
b.grid(row=3, column=2)
b.bind("<Button-1>", click)

b = Button(f, text="=", font="lucida 25 bold", padx=24)
# expanding the '=' in east and west direction, S means South and N means North
b.grid(row=2, column=3, rowspan=2, sticky=S+N)
b.bind("<Button-1>", click)

f.pack(anchor="nw")


root.mainloop()
