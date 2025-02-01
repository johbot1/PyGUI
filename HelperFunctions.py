# HelperFunctions.py
# Author: John Botonakis
# Desc: Functions to aid in the building of the GUI and
# address additional functionality where needed

import tkinter as tk
from tkinter import messagebox, simpledialog

from words import choose_word, HANGMANPICS

global answer_string, guess_spaces, guess_letters, guess_limit, letter_spaces, chosen_word, playing, name, keyboard_buttons, buttons

keyboard_buttons = []
buttons = {}
guessed_letters = []
guess_limit = 0

name = ""


# start_game:
# Initializes the game logic by choosing a word for the player to guess,
# then generating an answer variable that is a set amount of underscores
# equal to the word length. After, it begins the playing loop.
def start_game():
    global current_answer, chosen_word, playing, name

    # # Ask for name
    asking_for_name = True
    while asking_for_name:
        name_input = simpledialog.askstring("Name", "Enter your name")
        if name_input is None or name_input.isalpha() == False:
            messagebox.showinfo("Name", "Please enter your name with only letters "
                                        "(No spaces, numbers, or special characters.)")
        else:
            asking_for_name = False
            name = name_input
            messagebox.showinfo("Welcome!", f"Welcome to Hangman, {name_input}")
            information()

    chosen_word = choose_word()
    current_answer = ['_'] * len(
        chosen_word)  # For example, if the word is "cloud", this would be ['_', '_', '_', '_', '_']

    playing = True


# Reset_game:
# Resets the currently played game by clearing out the previously
# guessed letters, selecting a new goal word, and updates each display
# area to its original view.
def reset_game():
    global guessed_letters, chosen_word, guess_limit, current_answer, answer_string

    guessed_letters = []
    guess_limit = 0
    chosen_word = choose_word()
    current_answer = ["_" for _ in chosen_word]
    answer_string = " ".join(current_answer)
    update_answer_display()
    update_guess_display()
    reset_gallows()
    # Re-enable all letter buttons
    for button in buttons.values():
        button.config(state=tk.NORMAL)


# Information:
# Shows an informational popup sequence to the user to explain the game of Hangman
def information():
    global name
    info1 = messagebox.askyesno("Help", f"Say, {name}, have you played Hangman before?")
    if info1:
        messagebox.showinfo("Help", "Awesome! Have fun playing.")
    else:
        messagebox.showinfo("Help", "The goal of the game is to guess the word in the ANSWER section using"
                                    " individual letters to pice together the word!")
        messagebox.showinfo("Help", "You have 7 guesses. If you guess the word before he gets hanged, "
                                    "you win! Otherwise, you've condemned him to death.")
        messagebox.showinfo("Help", "Use the Restart Game button to restart the game. Have fun!")


# Keybuilder:
# Creates the frames that hold the keys to guess with.
# It takes in a 'window' object, so the frames have a home to stick to.
def keybuilder(window):
    global keyboard_buttons, buttons
    # This defines the layout of the letters similar to a keyboard
    lines = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
    # Magic Numbers for Frame positioning and scale.
    frame_width = 580
    frame_height = 200
    initial_x = 0.01
    initial_y = 0.7
    x_delta = 0.03
    y_delta = 0.08

    # Initialize button list
    keyboard_buttons = []

    # Creating the frames using the 'lines' list
    alphabet_frames = []
    for i in range(3):
        frame = tk.Frame(window, width=frame_width, height=frame_height)
        frame.place(relx=initial_x + i * x_delta, rely=initial_y + i * y_delta)
        alphabet_frames.append(frame)

    # Create buttons inside frames
    for frame, letters in zip(alphabet_frames, lines):
        for letter in letters:
            button = tk.Button(
                frame,
                text=letter,
                width=2,
                foreground="red",
                command=lambda l=letter: update_guesses(l),
            )
            button.pack(side=tk.LEFT, padx=2, pady=5)
            setattr(button, "guessed", False)  # Add a custom attribute

            buttons[letter] = button  # Store button in dictionary
        # print(f'{button_name} "has been created!') #Debugging help
    return buttons


# Guessbuilder:
# Creates a frame to hold the guessed letters so the player
# can see how many guesses they have left before losing.
# It takes in a 'window' object, so the frame will have a home to stick to.
def guessbuilder(window):
    global guess_spaces
    font_size = 20

    guessed_letters_frame = tk.Frame(window, bd=2, relief="raised")
    guessed_letters_frame.place(relx=0.01, rely=0.1, relwidth=0.5, relheight=0.2)
    guessed_text_label = tk.Label(guessed_letters_frame, text="Guesses: ", font=("Helvetica", font_size))
    guessed_text_label.pack()

    # This creates the spaces for each of the guessed letters, with each "_" representing a guess
    # and each guess getting switched for a letter when made. Once all are filled, the player has
    # run out of guesses, and the game is over.
    guess_string = ' '.join(
        ["_" for _ in range(len(HANGMANPICS) - 1)])
    guess_spaces = tk.Label(guessed_letters_frame, text=guess_string, font=("Helvetica", font_size))
    guess_spaces.pack()


# Wordbuilder:
# Creates a frame to hold the current answer as well as any letters
# that are correct.
# It takes in a 'window' object, so the frame will have a home to stick to.
def wordbuilder(window):
    global answer_string, letter_spaces
    font_size = 20
    answer_frame = tk.Frame(window, bd=2, relief="raised")
    answer_frame.place(relx=0.01, rely=0.4, relwidth=0.5, relheight=0.2)
    answer_text_label = tk.Label(answer_frame, text="Answer:", font=("Helvetica", font_size))
    answer_text_label.pack()

    # Creates and displays a length of underscores equal to the chosen_word length
    answer_string = " ".join("_" for _ in chosen_word)
    letter_spaces = tk.Label(answer_frame, text=answer_string, font=("Helvetica", font_size))
    letter_spaces.pack()


# Gallowsbuilder:
# Creates a frame to hold the ascii art of the hangman
# It takes in a 'window' object, so the frame will have a home to stick to.
def gallowsbuilder(window):
    global gallows_text
    gallows_font_size = 30
    gallows_frame = tk.Frame(window, width=300, height=800, bd=2, relief="raised")
    gallows_frame.place(relx=0.65, rely=0.1)
    gallows_text = tk.Label(gallows_frame, text="", font=("Courier", gallows_font_size), anchor="n", justify="left")
    gallows_text.pack(pady=10)
    gallows_text.config(text=HANGMANPICS[0])


# Add_reset_button:
# Implements a button to reset the GUI when called on
# It takes in a 'window' object, so the frame will have a home to stick to.
def add_reset_button(window):
    xpos = 0.88
    ypos = 0.94
    reset_button = tk.Button(window, text="Reset Game", font=("Helvetica", 15), command=reset_game)
    reset_button.place(relx=xpos, rely=ypos, anchor="center")


# Add_info_button:
# Implements a button that displays the informational popup sequence
# It takes in a 'window' object, so the frame will have a home to stick to.
def add_info_button(window):
    xpos = 0.04
    ypos = 0.94
    reset_button = tk.Button(window, text="?", font=("Helvetica", 15), command=information)
    reset_button.place(relx=xpos, rely=ypos, anchor="center")


def add_quit_button(window):
    xpos = 0.88  # Adjust position as needed
    ypos = 0.88
    quit_button = tk.Button(window, text="Quit", font=("Helvetica", 15), command=window.quit)
    quit_button.place(relx=xpos, rely=ypos, anchor="center")


# Update_guesses:
# Handles any event regarding guesses and letter buttons within the game.
def update_guesses(letter):
    global guessed_letters, chosen_word, current_answer, guess_limit

    # Case sensitivity is important (It will in fact kill me)
    letter = letter.lower()
    guessed_letters.append(letter)

    # A flag set to check if the guess is correct.
    # Most guesses are false, which is why it begins as such.
    correct_guess = False

    # Disable the button after it is clicked
    if letter.upper() in buttons:
        buttons[letter.upper()].config(state=tk.DISABLED)

    # Check to determine if the guess was correct or not
    for i, chosen_letter in enumerate(chosen_word):
        if chosen_letter == letter:
            current_answer[i] = letter
            correct_guess = True

    # If the flag is set to "True", update each display and proceed.
    # If this was the last letter or the last guess and it's successful,
    # proceed to game_win.
    if correct_guess:
        update_answer_display()
        guessed_letters.remove(letter)
        if all(letter in current_answer for letter in chosen_word):
            game_win()

    # If the guess is incorrect, the flag stays "False", and the
    # guess limit is increased by 1. If this was the last guess and
    # its wrong, proceed to game_over.
    else:
        guess_limit += 1
        if guess_limit >= len(HANGMANPICS) - 1:
            update_guess_display()
            game_over()
        else:
            update_guess_display()
            update_gallows()


# Update_guess_display:
# Updates the guess_display with any incorrect guesses and remaining guess spaces
def update_guess_display():
    global guessed_letters, guess_spaces, guess_limit, chosen_word
    font_size = 20

    displaytext = ""
    for letter in guessed_letters:
        displaytext += letter + " "

    remaining_spaces = (len(HANGMANPICS) - 1) - len(guessed_letters)
    displaytext += "_ " * remaining_spaces
    displaytext = displaytext.strip()
    guess_spaces.config(text=displaytext, font=("Helvetica", font_size))
    # print(f"Updated Word: {displaytext}")  # For debugging, print the updated word


# Update_answer_display:
# Updates the answer_display with any correct guesses and remaining letter spaces
def update_answer_display():
    global guessed_letters, letter_spaces, guess_limit
    displaytext = ""
    font_size = 20

    for i, letter in enumerate(chosen_word):
        if current_answer[i] != "_":
            displaytext += current_answer[i] + " "
        else:
            displaytext += "_ "

    displaytext = displaytext.strip()
    letter_spaces.config(text=displaytext, font=("Helvetica", font_size))

    # print(f"Updated Word: {displaytext}")  # For debugging, print the updated word


# Update_gallows:
# Updates the gallows display with the current art of the hangman state
# This acts as immediate visual feedback on the player's progress
def update_gallows():
    global guess_limit

    if guess_limit < len(HANGMANPICS):
        gallows_text.config(text="", font=("Helvetica", 30))  # Reset to blank
        gallows_text.config(text=HANGMANPICS[guess_limit], font=("Courier", 30), anchor="n",
                            justify="left")
    else:
        gallows_text.config(text=HANGMANPICS[-1], font=("Courier", 20))


# Reset_gallows:
# Resets the gallows art frame to its default state (empty)
def reset_gallows():
    global gallows_text

    gallows_text.config(text=HANGMANPICS[0])


# Game_over:
# Handles behaviour for when the game is lost by the player
def game_over():
    global playing
    gallows_text.config(text=HANGMANPICS[-1], font=("Courier", 20), anchor="n",
                        justify="left")
    messagebox.showerror("Killed", f"So close, but so far. The word was {chosen_word}.")
    quitdialogue = messagebox.askyesno("Try again", "Would you like to try again?")
    if quitdialogue:
        reset_game()
    else:
        messagebox.showerror("Given Up", f"That's fair. It's alot to weigh on a conscious. Thanks for playing!")
        playing = False


# Game_win:
# Handles behaviour for when the game is won by the player
def game_win():
    global playing
    if playing:
        messagebox.showerror("Winner!", f"You did it! Congratulations.")
        retrydialogue = messagebox.askyesno("Try again", "Would you like to try again?")
        if retrydialogue:
            reset_game()
        else:
            messagebox.showerror("Successful Leave", f"Thanks for playing!")
            playing = False
