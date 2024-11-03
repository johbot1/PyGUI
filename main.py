#Main.py
#Author: John Botonakis
#Desc: Holds the main logic for displaying the window and it's pieces
import tkinter as tk
from HelperFunctions import keybuilder, guessbuilder, wordbuilder, gallowsbuilder

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
gallowsbuilder(window)


#Word Frame
wordbuilder(window)

#Guesses Frame
guessbuilder(window)

#Keys
keybuilder(window)

if __name__ == '__main__':
    window.mainloop()