from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
new_word = {}
word = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    word = original_data.to_dict(orient='records')
else:
    word = data.to_dict(orient="records")


def display():
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(language_text, text='French', fill='black')
    new_word = random.choice(word)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(word_text, text=new_word['French'], fill='black')
    flip_timer = window.after(3000, flip)


def flip():
    canvas.itemconfig(language_text, text='English', fill='white')
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(word_text, text=new_word["English"], fill='white')


def is_known():
    word.remove(new_word)
    current_data = pandas.DataFrame(word)
    current_data.to_csv("data/words_to_learn.csv", index=False)
    display()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip)

canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR,  highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(400, 150, text="French", fill="black", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="", fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=display)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

display()


window.mainloop()
