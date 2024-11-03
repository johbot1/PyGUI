#HelperFunctions.py
#Author: John Botonakis
#Comments: Commenting Help from Google Gemini
#Desc: Functions to aid in the building of the GUI and
# address additional functionality where needed
guessed_letters = []

import tkinter as tk

def keybuilder(window):
    """
    Creates the keyboard frame with alphabet buttons.
    Args:
        window: The main window object to create the keyboard frame.
    """
    alphabet_buttons = []  # Initialize an empty list to store button objects
    # Define the layout of alphabet lines
    lines = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]  # Letter lines for each row

    # Frame dimensions and positions
    frame_width = 580
    frame_height = 150
    initial_x = 0.01
    initial_y = 0.7
    x_delta = 0.04
    y_delta = 0.08

    # Create and position the frames
    alphabet_frames = []
    for i in range(3):
        frame = tk.Frame(window, width=frame_width, height=frame_height)
        frame.place(relx=initial_x + i * x_delta, rely=initial_y + i * y_delta)
        alphabet_frames.append(frame)

    # Create buttons for each letter in each frame
    for frame, letter_line in zip(alphabet_frames, lines):
        for letter in letter_line:
            button_name = f"button_{letter.lower()}"
            button = tk.Button(frame, text=letter, width=5, command=lambda letter=letter: update_guesses(letter))
            button.pack(side=tk.LEFT, padx=5, pady=5)
            alphabet_buttons.append(button)
            button_name = button
            alphabet_buttons.append(button_name)  # Add the new button, with its name, into the buttons group
            # print(f'{button_name} "has been created!') #Debugging help


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

def update_guesses(letter):
    global guessed_letters
    guessed_letters.append(letter)
    update_guess_display()

def update_guess_display():
    print('working')