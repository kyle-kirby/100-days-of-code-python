from tkinter import *
import pandas
import random

current_word = {}
to_learn_list = {}
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn_list = original_data.to_dict(orient="records")
else:
    to_learn_list = data.to_dict(orient="records")


# --Countdown--#
def countdown(count):

    if count > 0:
        window.after(1000, countdown, count -1)
    else:
        canvas.itemconfig(canvas_image, image=back_card_img)
        title_label.config(text="English", fg="white", bg="#91C2AF")
        word_label.config(text=current_word["English"], fg="white", bg="#91C2AF")


#--Word Selection--#
def word_selection():
    global current_word
    canvas.itemconfig(canvas_image, image=card_img)
    title_label.config(text="French", font=("Ariel", 40, "italic"), fg="black", bg="white")
    current_word = random.choice(to_learn_list)
    word_label.config(text=current_word["French"], fg="black", bg="white")

    countdown(3)

#--Remove Known Words--#
def is_known():
    to_learn_list.remove(current_word)
    print(len(to_learn_list))
    data = pandas.DataFrame(to_learn_list)
    data.to_csv("data/words_to_learn.csv", index=False)

    word_selection()

#---UI SETUP ---#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_img)
back_card_img = PhotoImage(file="images/card_back.png")
canvas.grid(column=0, row=0, columnspan=2)

#Labels
title_label = Label(text="Text", font=("Ariel", 40, "italic"), bg="white")
title_label.place(x=400, y=150, anchor="center")
word_label = Label(text="Word", font=("Ariel", 60, "bold"), bg="white")
word_label.place(x=400, y=263, anchor="center")

#Buttons
no_image = PhotoImage(file="images/wrong.png")
no_button = Button(image=no_image, highlightthickness=0, command=word_selection)
no_button.grid(column=0, row=2)
yes_image = PhotoImage(file="images/right.png")
yes_button = Button(image=yes_image, highlightthickness=0, command=is_known)
yes_button.grid(column=1, row=2)


word_selection()
window.mainloop()