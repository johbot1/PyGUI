#Main.py
#Author: John Botonakis
#Desc: Holds the main logic for displaying the window and it's pieces
import tkinter as tk
from HelperFunctions import create_alphabet_frame

#Main window Setup
window = tk.Tk()
window.geometry('600x600')
window.title('Hangman!')
window.resizable(False, False)

#Centering the window to the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# Calculate window position
widthdivisor = 2 #Found this to be good size for the dividing the width to keep window centered
heightdivisor = 8 #Found this to be good size for the dividing the height to keep window centered
x = (screen_width - window.winfo_width()) // widthdivisor
y = (screen_height - window.winfo_height()) // heightdivisor

# Sets window position
window.geometry(f"+{x}+{y}")

#Main Title
title_frame = tk.Frame(window, width=500, height=50)
title_frame.pack(side=tk.TOP, fill=tk.X)
title_label = tk.Label(title_frame, text="HANGMAN", font=("Helvetica", 20))
title_label.pack(pady=10)

#Hangman Frame
gallows_frame = tk.Frame(window, bg="pink", width=200, height=300, bd=2,relief = "raised")
gallows_frame.place(relx=0.6, rely=0.1)


#Word Frame
answer_frame = tk.Frame(window, bd=2,relief = "raised")
answer_frame.place(relx=0.01, rely=0.4, relwidth=0.5, relheight=0.2)
# Label for "Guessed:" text
answer_text_label = tk.Label(answer_frame, text="Answer: ", font=("Helvetica", 15))
answer_text_label.pack()

#Guesses Frame
guessed_letters_frame = tk.Frame(window, bd=2,relief = "raised")
guessed_letters_frame.place(relx=0.01, rely=0.1, relwidth=0.5, relheight=0.2)
# Label for "Guessed:" text
guessed_text_label = tk.Label(guessed_letters_frame, text="Guesses: ", font=("Helvetica", 15))
guessed_text_label.pack()


# Keys (using a loop to create multiple frames)
letter_sets = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
rely_positions = [0.7, 0.78, 0.86]

for letters, rely_position in zip(letter_sets, rely_positions):
    create_alphabet_frame(window, rely_position, letters)

if __name__ == '__main__':
    window.mainloop()