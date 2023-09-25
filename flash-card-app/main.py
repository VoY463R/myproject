from tkinter import *
import pandas
import random
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
english_word = None
french_word_dict = {}
current_card = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except:
    french_word = pandas.read_csv("data/french_words.csv")
    french_word_dict = french_word.to_dict(orient="records")
else:
    french_word_dict = data.to_dict(orient="records")

def next_card():
    global random_word_english, flip_timer, current_card
    window.after_cancel(flip_timer)
    try:
        current_card = random.choice(french_word_dict)
    except:
        messagebox.showinfo(title="Finish", message="You've learned all words!")
    else:
        random_word_french = current_card["French"]
        random_word_english = current_card["English"]
        canvas.itemconfig(word, text=random_word_french, fill="black")
        canvas.itemconfig(language, text="French", fill="black")
        canvas.itemconfig(canvas_image, image=card_front_image)
        flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(word, text=random_word_english, fill="white")
    canvas.itemconfig(language, text="English", fill="white")
    
def learn():
    try:
        french_word_dict.remove(current_card)
    except:
        return
    words_to_learn = french_word_dict
    data = pandas.DataFrame(words_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
    


window = Tk()
window.title("flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

card_back_image = PhotoImage( file="images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_image = PhotoImage( file="images/card_front.png")
canvas_image = canvas.create_image(400, 263,image=card_front_image)

language = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))

word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=learn)
right_button.grid(column=1, row=1)

wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()