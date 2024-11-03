#HelperFunctions.py
#Author: John Botonakis
#Comments: Help from Google Gemini
#Desc: Functions to aid in the building of the GUI and
# address additional functionality where needed

import tkinter as tk
def keybuilder(window):
    alphabet_buttons = []
    alphabet_frame1 = tk.Frame(window, width=580, height=150)
    alphabet_frame1.place(relx=0.01, rely=0.7)

    alphabet_frame2 = tk.Frame(window, width=580, height=150)
    alphabet_frame2.place(relx=0.05, rely=0.78)

    alphabet_frame3 = tk.Frame(window, width=580, height=150)
    alphabet_frame3.place(relx=0.1, rely=0.86)

    line1 = "QWERTYUIOP"
    line2 = "ASDFGHJKL"
    line3 = "ZXCVBNM"

    for letter in line1:
        # Creates a button with a unique name (button_a, button_b, etc)
        button_name = f"button_{letter.lower()}"  # Makes lowercase for consistency
        button = tk.Button(alphabet_frame1, text=letter, width=5, command=lambda letter=letter: print(letter))
        button.pack(side=tk.LEFT, padx=5, pady=5)
        print(button_name)
        button_name = button
        alphabet_buttons.append(button_name)

    for letter in line2:
        # Creates a button with a unique name (button_a, button_b, etc)
        button_name = f"button_{letter.lower()}"  # Makes lowercase for consistency
        button = tk.Button(alphabet_frame2, text=letter, width=5, command=lambda letter=letter: print(letter))
        button.pack(side=tk.LEFT, padx=5, pady=5)
        print(button_name)
        button_name = button
        alphabet_buttons.append(button_name)

    for letter in line3:
        # Creates a button with a unique name (button_a, button_b, etc)
        button_name = f"button_{letter.lower()}"  # Makes lowercase for consistency
        button = tk.Button(alphabet_frame3, text=letter, width=5, command=lambda letter=letter: print(letter))
        button.pack(side=tk.LEFT, padx=5, pady=5)
        print(button_name)
        button_name = button
        alphabet_buttons.append(button_name)

def guessbuilder(window):
    guessed_letters_frame = tk.Frame(window, bd=2, relief="raised")
    guessed_letters_frame.place(relx=0.01, rely=0.1, relwidth=0.5, relheight=0.2)
    # Label for "Guessed:" text
    guessed_text_label = tk.Label(guessed_letters_frame, text="Guesses: ", font=("Helvetica", 15))
    guessed_text_label.pack()

def wordbuilder(window):
    answer_frame = tk.Frame(window, bd=2, relief="raised")
    answer_frame.place(relx=0.01, rely=0.4, relwidth=0.5, relheight=0.2)
    # Label for "Guessed:" text
    answer_text_label = tk.Label(answer_frame, text="Answer: ", font=("Helvetica", 15))
    answer_text_label.pack()

def gallowsbuilder(window):
    gallows_frame = tk.Frame(window, bg="pink", width=200, height=300, bd=2, relief="raised")
    gallows_frame.place(relx=0.6, rely=0.1)