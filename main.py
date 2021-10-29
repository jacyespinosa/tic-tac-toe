import tkinter
from tkinter import *


window = Tk()
text = StringVar()
window.title("Tic-Tac-Toe")
window.minsize(width=215, height=350)
window.maxsize(width=215, height=350)

clicked = True


def button_clicked(button):
    global clicked
    if button['text'] == '' and clicked:
        text.set("X")
        clicked = False
    if button['text'] == ' ' and clicked is False:
        text.set("O")
        clicked = True


x_player = Button(text="X",  fg='red', width=7, height=1)
x_player.grid(column=1, row=3)

first_player = Label(text="Player 1", width=7, height=2)
first_player.grid(column=0, row=3)

o_player = Button(text="O",  fg='blue', width=7, height=1)
o_player.grid(column=1, row=4)

second_player = Label(text="Player 2", width=7, height=2)
second_player.grid(column=0, row=4)

first_button = Button(textvariable=text, width=7, height=5, highlightthickness=2, fg='black', command=lambda: button_clicked(first_button))
first_button.grid(column=0, row=0)

second_button = Button(textvariable=text, width=7, height=5, highlightthickness=2, fg='black', command=lambda: button_clicked(second_button))
second_button.grid(column=1, row=0)

third_button = Button(textvariable=text, width=7, height=5, highlightthickness=2, fg='black', command=lambda: button_clicked(third_button))
third_button.grid(column=2, row=0)

fourth_button = Button(textvariable=text, width=7, height=5, highlightthickness=2, fg='black', command=lambda: button_clicked(fourth_button))
fourth_button.grid(column=0, row=1)

fifth_button = Button(textvariable=text, width=7, height=5, highlightthickness=2, fg='black', command=lambda: button_clicked(fifth_button))
fifth_button.grid(column=1, row=1)

sixth_button = Button(textvariable=text, width=7, height=5, highlightthickness=2, fg='black', command=lambda: button_clicked(sixth_button))
sixth_button.grid(column=2, row=1)

seventh_button = Button(textvariable=text, width=7, height=5, highlightthickness=2, fg='black', command=lambda: button_clicked(seventh_button))
seventh_button.grid(column=0, row=2)

eight_button = Button(textvariable=text, width=7, height=5, highlightthickness=2, fg='black', command=lambda : button_clicked(eight_button))
eight_button.grid(column=1, row=2)

ninth_button = Button(textvariable=text, width=7, height=5, highlightthickness=2, fg='black', command=lambda: button_clicked(ninth_button))
ninth_button.grid(column=2, row=2)

window.mainloop()