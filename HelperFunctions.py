#HelperFunctions.py
#Author: John Botonakis
#Comments: Commenting Help from Google Gemini
#Desc: Functions to aid in the building of the GUI and
# address additional functionality where needed

import tkinter as tk
import tkinter.messagebox
from tkinter import messagebox

from words import choose_word, HANGMANPICS

global answer_string, guess_spaces, guess_letters, guess_limit,letter_spaces,chosen_word

guessed_letters = []
guess_limit = 0

def start_game():
    global current_answer, chosen_word
    """
        Initializes a word, and creates a display of underscores the length of that word to symbolize guesses
        """

    # Pick a word to guess
    chosen_word = choose_word()

    # Initialize current_answer with underscores corresponding to the word length
    current_answer = ['_'] * len(chosen_word)  # For example, if the word is "cloud", this would be ['_', '_', '_', '_', '_']

def reset_game():
    global guessed_letters, chosen_word, guess_limit, current_answer, answer_string
    """
        Resets the game by clearing guessed letters, selecting a new word,
        and updating the displays to reflect a fresh start.
        """
# Reset the guessed letters list and the guess limit
    guessed_letters = []
    guess_limit = 0

    # Select a new word
    chosen_word = choose_word()

    # Reset the current answer (underscores for each letter in the chosen word)
    current_answer = ["_" for _ in chosen_word]
    answer_string = " ".join(current_answer)

    # Update the word display (clear underscores)
    update_answer_display()

    # Reset the guessed letters display
    update_guess_display()

    # Reset the gallows display
    reset_gallows()

def information():
    """
        Shows an informational popup to the user.
        """
    info1 = messagebox.askyesno("Help", "Welcome to Hangman! Have you played before?")
    if info1:
        messagebox.showinfo("Help", "Awesome! Have fun playing.")
    else:
        messagebox.showinfo("Help", "The goal of the game is to guess the word in the ANSWER section using"
                                    " individual letters to pice together the word!")
        messagebox.showinfo("Help", "You have 7 guesses. If you guess the word before he gets hanged, "
                                    "you win! Otherwise, you've condemned him to death.")
        messagebox.showinfo("Help", "Use the Restart Game button to restart the game. Have fun!")


def keybuilder(window):
    """
    Creates the keyboard frame with alphabet buttons.
    Args:
        window: The main window object to attach the keyboard frame to.
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
    global guess_spaces
    """
    Creates a frame to display guessed letters.

    Args:
        window: The main Tkinter window object to attach the guessed letters frame to.
    """

    # Create a frame to hold the guessed letters section
    guessed_letters_frame = tk.Frame(window, bd=2, relief="raised")
    guessed_letters_frame.place(relx=0.01, rely=0.1, relwidth=0.5, relheight=0.2)

    # Add a label for the "Guesses:" text
    guessed_text_label = tk.Label(guessed_letters_frame, text="Guesses: ", font=("Helvetica", 15))
    guessed_text_label.pack()

    # Create and display spaces for guessed letters, initialized as underscores
    guess_string = ' '.join(["_" for _ in range(len(HANGMANPICS)-1)])  # Generate a string of 6 underscores separated by spaces
    guess_spaces = tk.Label(guessed_letters_frame, text=guess_string, font=("Helvetica", 15))
    guess_spaces.pack()

def wordbuilder(window):
    global answer_string, letter_spaces
    """
        Creates a frame to display the current answer in the hangman game, showing
        the word with underscores for unguessed letters.

        Args:
            window: The main Tkinter window object to attach the answer frame to.
        """

    # Create a frame to hold the answer display section
    answer_frame = tk.Frame(window, bd=2, relief="raised")
    answer_frame.place(relx=0.01, rely=0.4, relwidth=0.5, relheight=0.2)

    # Label for "Answer:" text
    answer_text_label = tk.Label(answer_frame, text="Answer:", font=("Helvetica", 15))
    answer_text_label.pack()

    # Generate the answer string with underscores for each letter in the chosen word
    answer_string = " ".join("_" for _ in chosen_word)  # Create underscores based on the word length

    # Display the underscores as the current state of the answer
    letter_spaces = tk.Label(answer_frame, text=answer_string, font=("Helvetica", 15))
    letter_spaces.pack()

def gallowsbuilder(window):
    global gallows_text
    """
       Creates a gallows frame to display ASCII art of the hangman.

       Args:
           window: The main Tkinter window object to attach the gallows frame to.
       """
    # Create the gallows frame
    gallows_frame = tk.Frame(window, width=200, height=300, bd=2, relief="raised")
    gallows_frame.place(relx=0.6, rely=0.1)

    # Create a Label widget inside the gallows frame to hold the ASCII art
    gallows_text = tk.Label(gallows_frame, text="", font=("Courier", 20), anchor="n", justify="left")
    gallows_text.pack(pady=10)  # Add some padding for spacing

    # Add text to the gallows
    gallows_text.config(text=HANGMANPICS[0])

def add_reset_button(window):
    """
    Adds a reset button to the GUI that restarts the game when clicked.
    """
    xpos = 0.88
    ypos = 0.94
    reset_button = tk.Button(window, text="Reset Game", font=("Helvetica", 15), command=reset_game)
    reset_button.place(relx=xpos, rely=ypos, anchor="center")  # Adjust placement as needed

def add_info_button(window):
    """
       Adds an information button to the GUI that explains the game when clicked.
       """
    xpos = 0.04
    ypos = 0.94
    reset_button = tk.Button(window, text="?", font=("Helvetica", 15), command=information)
    reset_button.place(relx=xpos, rely=ypos, anchor="center")



def update_guesses(letter):
    global guessed_letters, chosen_word, current_answer, guess_limit  # Global variables for guessed letters and word
    """
       Handles the letter press event in the game.

       Args:
           letter: The letter that was pressed by the user.
       """

    #Case sensitivity (It will in fact kill me)
    letter = letter.lower()

    # Check if the letter has already been guessed
    if letter in guessed_letters:
        messagebox.showerror("Double Dip", f"Appreciate your enthusiasm but you already guessed that letter.")
        return  # Don't do anything if the letter was already guessed

    # Add the letter to the guessed letters list
    guessed_letters.append(letter)


    # Flag to check if the guess was correct
    correct_guess = False

    # Iterate through each letter in the chosen word
    for i, chosen_letter in enumerate(chosen_word):
        if chosen_letter == letter:  # If the guessed letter matches a letter in the chosen word
            current_answer[i] = letter  # Replace the underscore with the correct letter
            correct_guess = True  # Mark as a correct guess
            guessed_letters.remove(letter) # Remove the correct letter from the guess list to avoid confusion


    # If the guess was correct, update the answer string with the newly revealed letters
    if correct_guess:
        update_answer_display()
    else:
        guess_limit += 1 #Increment the guess counter by 1
        if guess_limit ==7:
            game_over()
        else:
            update_guess_display()
            update_gallows()

def update_guess_display():
    global guessed_letters, guess_spaces, guess_limit, chosen_word
    """
    Updates the displayed word in the `guessbuilder` frame, showing incorrectly guessed letters
    and underscores for the remaining letters.
    """

    displaytext =  ""

    # Iterate over each letter in guessed_letters and display it
    for letter in guessed_letters:
        displaytext += letter + " "

    # Add remaining underscores for incorrect guesses
    remaining_spaces = (len(HANGMANPICS)-1) - len(guessed_letters)
    displaytext += "_ " * remaining_spaces

    # Remove the trailing space after the last letter
    displaytext = displaytext.strip()

    # Update the displayed word in the GUI (the `letter_spaces` label)
    guess_spaces.config(text=displaytext, font=("Helvetica", 15))  # Update the Tkinter label with the new word display
    # print(f"Updated Word: {displaytext}")  # For debugging, print the updated word

def update_answer_display():
    global guessed_letters, letter_spaces, guess_limit
    """
    Updates the displayed word in the `wordbuilder` frame, showing correctly guessed letters
    and underscores for the remaining letters.
    """
    displaytext = ""

    # Iterate over each letter in the chosen word
    for i, letter in enumerate(chosen_word):
        if current_answer[i] != "_":  # If the letter has been guessed, show it
            displaytext += current_answer[i] + " "
        else:  # If the letter has not been guessed, show an underscore
            displaytext += "_ "

    # Remove the trailing space after the last letter
    displaytext = displaytext.strip()

    # Update the displayed word in the GUI (the `letter_spaces` label)
    letter_spaces.config(text=displaytext, font=("Helvetica", 15))  # Update the Tkinter label with the new word display
    # print(f"Updated Word: {displaytext}")  # For debugging, print the updated word

def update_gallows():
    global guess_limit, gallows_text

    if guess_limit < len(HANGMANPICS):
        gallows_text.config(text="", font=("Helvetica", 20))
        gallows_text.config(text=HANGMANPICS[guess_limit], font=("Courier", 20), anchor="n", justify="left")  # Update the Tkinter label with the new word display
    else:
        gallows_text.config(text=HANGMANPICS[-1], font=("Courier", 20))

def reset_gallows():
    global gallows_text
    """
    Resets the gallows figure to its initial state (no drawing).
    """
    gallows_text.config(text=HANGMANPICS[0])  # Set to the first (empty) hangman figure

def game_over():
    messagebox.showerror("Killed", f"So close, but so far. The word was {chosen_word}.")
    quitdialogue = messagebox.askyesno("Try again", "Would you like to try again?")
    if quitdialogue:
        reset_game()
    else:
        messagebox.showerror("Given Up", f"That's fair. It's alot to weigh on a conscious. Thanks for playing!")

def game_win():
    messagebox.showerror("Winner!", f"You did it! Congratulations.")
    quitdialogue = messagebox.askyesno("Try again", "Would you like to try again?")
    if quitdialogue:
        reset_game()
    else:
        messagebox.showerror("Successful Leave", f"Thanks for playing!")