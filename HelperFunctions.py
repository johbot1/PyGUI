#HelperFunctions.py
#Author: John Botonakis
#Comments: Commenting Help from Google Gemini
#Desc: Functions to aid in the building of the GUI and
# address additional functionality where needed

from words import words, choose_word
import tkinter as tk

guessed_letters = []
chosen_word = choose_word()

global answer_string, letter_spaces, guess_letters

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
    guess_string = ' '.join(["_" for _ in range(6)])  # Generate a string of 6 underscores separated by spaces
    guess_spaces = tk.Label(guessed_letters_frame, text=guess_string, font=("Helvetica", 15))
    guess_spaces.pack()

def wordbuilder(window):
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
    answer_string = " _ ".join("_" for _ in chosen_word)  # Create underscores based on the word length

    # Display the underscores as the current state of the answer
    letter_spaces = tk.Label(answer_frame, text=answer_string, font=("Helvetica", 15))
    letter_spaces.pack()

def gallowsbuilder(window):
    gallows_frame = tk.Frame(window, bg="pink", width=200, height=300, bd=2, relief="raised")
    gallows_frame.place(relx=0.6, rely=0.1)

def update_guesses(letter):
    guessed_letters.append(letter)
    print(f"Current letter: {letter}")

    # Iterate through each letter in the chosen word
    for i, chosen_letter in enumerate(chosen_word):
        if chosen_letter == letter:  # Check for correct guess
            # Replace the corresponding underscore with the letter
            answer_string = answer_string[:i] + letter + answer_string[i+1:]
