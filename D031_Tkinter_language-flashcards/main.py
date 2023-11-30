from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
pair = {}


# ------------------------ GETTING WORDS ------------------------ #

df = pandas.read_csv("data/french_words.csv")
words_dict = df.to_dict(orient="records")


def next_card():
    global pair, flip_timer
    pair = random.choice(words_dict)
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=pair["French"], fill="black")
    flip_timer = window.after(3000, turn_card)


def turn_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    global pair
    canvas.itemconfig(language_text, text="English", fill="white")
    # noinspection PyTypeChecker
    canvas.itemconfig(word_text, text=pair["English"], fill="white")


# ------------------------ UI SETUP ------------------------ #
# screen
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, background=BACKGROUND_COLOR)
flip_timer = window.after(3000, turn_card)

# canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(400, 150, text="Press any button to start", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# buttons
x_image = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_image, highlightthickness=0, relief="flat", borderwidth=0, command=next_card)
x_button.grid(column=0, row=1)
v_image = PhotoImage(file="images/right.png")
v_button = Button(image=v_image, highlightthickness=0, relief="flat", borderwidth=0, command=next_card)
v_button.grid(column=1, row=1)


next_card()

window.mainloop()


