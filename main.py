from tkinter import *


window = Tk()
window.title("Tic-Tac-Toe")
window.minsize(width=215, height=350)
window.maxsize(width=215, height=350)


x_player = Button(text="X", width=7, height=1)
x_player.grid(column=1, row=3)

first_player = Label(text="Player 1", width=7, height=2)
first_player.grid(column=0, row=3)

o_player = Button(text="O", width=7, height=1)
o_player.grid(column=1, row=4)

second_player = Label(text="Player 2", width=7, height=2)
second_player.grid(column=0, row=4)

first_button = Button(text="", width=7, height=5, highlightthickness=2, fg='black')
first_button.grid(column=0, row=0)

second_button = Button(text="", width=7, height=5, highlightthickness=2, fg='black')
second_button.grid(column=1, row=0)

third_button = Button(text="", width=7, height=5, highlightthickness=2, fg='black')
third_button.grid(column=2, row=0)

fourth_button = Button(text="", width=7, height=5, highlightthickness=2, fg='black')
fourth_button.grid(column=0, row=1)

fifth_button = Button(text="", width=7, height=5, highlightthickness=2, fg='black')
fifth_button.grid(column=1, row=1)

sixth_button = Button(text="", width=7, height=5, highlightthickness=2, fg='black')
sixth_button.grid(column=2, row=1)

seventh_button = Button(text="", width=7, height=5, highlightthickness=2, fg='black')
seventh_button.grid(column=0, row=2)

eight_button = Button(text="", width=7, height=5, highlightthickness=2, fg='black')
eight_button.grid(column=1, row=2)

ninth_button = Button(text="", width=7, height=5, highlightthickness=2, fg='black')
ninth_button.grid(column=2, row=2)

window.mainloop()