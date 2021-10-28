from tkinter import *


window = Tk()
window.title("Tic-Tac-Toe")
window.minsize(width=210, height=260)
window.maxsize(width=210, height=260)


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