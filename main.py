#Main.py
#Author: John Botonakis
#Desc: Holds the main logic for displaying the window and it's pieces
import tkinter as tk

#Main window Setup
window = tk.Tk()
window.geometry('600x600')
window.title('Hangman!')
window.resizable(False, False)

#Centering the window to the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# Calculate window position
widthdivisor = 3 #Found this to be good size for the dividing the width to keep window centered
heightdivisor = 4 #Found this to be good size for the dividing the height to keep window centered
x = (screen_width - window.winfo_width()) // widthdivisor
y = (screen_height - window.winfo_height()) // heightdivisor

# Sets window position
window.geometry(f"+{x}+{y}")

#Main Title
title_frame = tk.Frame(window, bg="lightblue", width=500, height=50)
title_frame.pack(side=tk.TOP, fill=tk.X)
title_label = tk.Label(title_frame, text="HANGMAN", font=("Helvetica", 20))
title_label.pack(pady=10)

#Hangman Frame
gallows_frame = tk.Frame(window, bg="lightgreen", width=200, height=200)


#Guesses Frame
guessed_letters_frame = tk.Frame(window, bg="green", width=200, height=50)


#Keys
# alphabet_frame = tk.Frame(window, bg="blue", width=300, height=200)
# alphabet_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
# alphabet_buttons = []
# for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#     button = tk.Button(alphabet_frame, text=letter, width=2)
#     button.pack(side=tk.LEFT, padx=5, pady=5)
#     alphabet_buttons.append(button)





if __name__ == '__main__':
    window.mainloop()