from tkinter import messagebox
from tkinter import *


window = Tk()
text = StringVar()
window.title("Tic-Tac-Toe")
window.minsize(width=215, height=350)
window.maxsize(width=215, height=350)

global clicked, answer, counter
counter = 0
answer = False
clicked = True


def button_clicked(button):
    global clicked, answer, counter
    if button['text'] == '' and clicked is True:
        button['text'] = "X"
        button['state'] = 'disabled'
        button['fg'] = 'red'
        button['disabledforeground'] = 'red'
        clicked = False
        counter += 1
    elif clicked is False:
        button['text'] = "O"
        button['state'] = 'disabled'
        button['fg'] = 'blue'
        button['disabledforeground'] = 'blue'
        clicked = True
        counter += 1


    print(counter)
    if counter > 8 and clicked is False:
        messagebox.showinfo("Tie Game", "It's A Tie!")
        answer = messagebox.askyesno("Play Again?", "Want to play again?")
        play_again()
        clicked = True
    else:
        game_win()




def game_win():
    global answer
    global clicked
    if first_button['text'] == "X" and second_button['text'] == "X" and third_button['text'] == "X":
        messagebox.showinfo("We Got A Winner", "Player 1 Wins!!!")
        answer = messagebox.askyesno("Play Again?", "Want to play again?")
        play_again()
        clicked = True
    elif first_button['text'] == "X" and fourth_button['text'] == "X" and seventh_button['text'] == "X":
        messagebox.showinfo("We Got A Winner", "Player 1 Wins!!!")
        answer = messagebox.askyesno("Play Again?", "Want to play again?")
        play_again()
        clicked = True
    elif first_button['text'] == "X" and fifth_button['text'] == "X" and ninth_button['text'] == "X":
        messagebox.showinfo("We Got A Winner", "Player 1 Wins!!!")
        answer = messagebox.askyesno("Play Again?", "Want to play again?")
        play_again()
        clicked = True
    elif second_button['text'] == "X" and fifth_button['text'] == "X" and eight_button['text'] == "X":
        messagebox.showinfo("We Got A Winner", "Player 1 Wins!!!")
        answer = messagebox.askyesno("Play Again?", "Want to play again?")
        play_again()
        clicked = True
    elif third_button['text'] == "X" and fifth_button['text'] == "X" and seventh_button['text'] == "X":
        messagebox.showinfo("We Got A Winner", "Player 1 Wins!!!")
        answer = messagebox.askyesno("Play Again?", "Want to play again?")
        play_again()
        clicked = True
    elif fourth_button['text'] == "X" and fifth_button['text'] == "X" and sixth_button['text'] == "X":
        messagebox.showinfo("We Got A Winner", "Player 1 Wins!!!")
        answer = messagebox.askyesno("Play Again?", "Want to play again?")
        play_again()
        clicked = True
    elif third_button['text'] == "X" and sixth_button['text'] == "X" and ninth_button['text'] == "X":
        messagebox.showinfo("We Got A Winner", "Player 1 Wins!!!")
        answer = messagebox.askyesno("Play Again?", "Want to play again?")
        play_again()
        clicked = True
    elif seventh_button['text'] == "X" and eight_button['text'] == "X" and ninth_button['text'] == "X":
        messagebox.showinfo("We Got A Winner", "Player 1 Wins!!!")
        answer = messagebox.askyesno("Play Again?", "Want to play again?")
        play_again()
        clicked = True
    elif first_button['text'] == "O" and second_button['text'] == "O" and third_button['text'] == "O":
        messagebox.showinfo("We Got A Winner", "Player 2 Wins!!!")
        answer = messagebox.askyesno("Play Again?", "Want to play again?")
        play_again()
        clicked = True
    elif first_button['text'] == "O" and fourth_button['text'] == "O" and seventh_button['text'] == "O":
        messagebox.showinfo("We Got A Winner", "Player 2 Wins!!!")
        answer = messagebox.askyesno("Play Again?", "Want to play again?")
        play_again()
        clicked = True
    elif first_button['text'] == "O" and fifth_button['text'] == "O" and ninth_button['text'] == "O":
        messagebox.showinfo("We Got A Winner", "Player 2 Wins!!!")
        answer = messagebox.askyesno("Play Again?", "Want to play again?")
        play_again()
        clicked = True
    elif second_button['text'] == "O" and fifth_button['text'] == "O" and eight_button['text'] == "O":
        messagebox.showinfo("We Got A Winner", "Player 2 Wins!!!")
        answer = messagebox.askyesno("Play Again?", "Want to play again?")
        play_again()
        clicked = True
    elif fourth_button['text'] == "O" and fifth_button['text'] == "O" and sixth_button['text'] == "O":
        messagebox.showinfo("We Got A Winner", "Player 2 Wins!!!")
        answer = messagebox.askyesno("Play Again?", "Want to play again?")
        play_again()
        clicked = True
    elif third_button['text'] == "O" and sixth_button['text'] == "O" and ninth_button['text'] == "O":
        messagebox.showinfo("We Got A Winner", "Player 2 Wins!!!")
        answer = messagebox.askyesno("Play Again?", "Want to play again?")
        play_again()
        clicked = True
    elif third_button['text'] == "O" and fifth_button['text'] == "O" and seventh_button['text'] == "O":
        messagebox.showinfo("We Got A Winner", "Player 2 Wins!!!")
        answer = messagebox.askyesno("Play Again?", "Want to play again?")
        play_again()
        clicked = True
    elif seventh_button['text'] == "O" and eight_button['text'] == "O" and ninth_button['text'] == "O":
        messagebox.showinfo("We Got A Winner", "Player 2 Wins!!!")
        answer = messagebox.askyesno("Play Again?", "Want to play again?")
        play_again()
        clicked = True


def play_again():
    global answer
    if answer is True:
        first_button['text'] = ""
        second_button['text'] = ""
        third_button['text'] = ""
        fourth_button['text'] = ""
        fifth_button['text'] = ""
        sixth_button['text'] = ""
        seventh_button['text'] = ""
        eight_button['text'] = ""
        ninth_button['text'] = ""
    else:
        messagebox.showinfo("Thank You!", "Thank you for playing!")

    enable_buttons()


def enable_buttons():
    first_button['state'] = "normal"
    second_button['state'] = "normal"
    third_button['state'] = "normal"
    fourth_button['state'] = "normal"
    fifth_button['state'] = "normal"
    sixth_button['state'] = "normal"
    seventh_button['state'] = "normal"
    eight_button['state'] = "normal"
    ninth_button['state'] = "normal"


x_player = Button(text="X",  fg='red', width=7, height=1)
x_player.grid(column=1, row=3)

first_player = Label(text="Player 1", width=7, height=2)
first_player.grid(column=0, row=3)

o_player = Button(text="O",  fg='blue', width=7, height=1)
o_player.grid(column=1, row=4)

second_player = Label(text="Player 2", width=7, height=2)
second_player.grid(column=0, row=4)

first_button = Button(text="", width=7, height=5, highlightthickness=2, fg='black', command=lambda: button_clicked(first_button))
first_button.grid(column=0, row=0)

second_button = Button(text="", width=7, height=5, highlightthickness=2, fg='black', command=lambda: button_clicked(second_button))
second_button.grid(column=1, row=0)

third_button = Button(text="", width=7, height=5, highlightthickness=2, fg='black', command=lambda: button_clicked(third_button))
third_button.grid(column=2, row=0)

fourth_button = Button(text="", width=7, height=5, highlightthickness=2, fg='black', command=lambda: button_clicked(fourth_button))
fourth_button.grid(column=0, row=1)

fifth_button = Button(text="", width=7, height=5, highlightthickness=2, fg='black', command=lambda: button_clicked(fifth_button))
fifth_button.grid(column=1, row=1)

sixth_button = Button(text="", width=7, height=5, highlightthickness=2, fg='black', command=lambda: button_clicked(sixth_button))
sixth_button.grid(column=2, row=1)

seventh_button = Button(text="", width=7, height=5, highlightthickness=2, fg='black', command=lambda: button_clicked(seventh_button))
seventh_button.grid(column=0, row=2)

eight_button = Button(text="", width=7, height=5, highlightthickness=2, fg='black', command=lambda : button_clicked(eight_button))
eight_button.grid(column=1, row=2)

ninth_button = Button(text="", width=7, height=5, highlightthickness=2, fg='black', command=lambda: button_clicked(ninth_button))
ninth_button.grid(column=2, row=2)

window.mainloop()