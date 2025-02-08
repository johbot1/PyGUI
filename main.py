# Main.py
# Author: John Botonakis
# Desc: Holds the main logic for displaying the window and it's pieces

import HelperFunctions
from HelperFunctions import *

# Main window Setup
window = tk.Tk()
window.geometry('600x600')
window.title('Hangman!')
window.resizable(False, False)
window.config(background='lightblue')
window.focus_force()
HelperFunctions.window = window

# Centering the window to the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate window position
widthdivisor = 3  # Found this to be good size for the dividing the width to keep window centered
heightdivisor = 6  # Found this to be good size for the dividing the height to keep window centered
x = (screen_width - window.winfo_width()) // widthdivisor
y = (screen_height - window.winfo_height()) // heightdivisor

# Sets window position
window.geometry(f"+{x}+{y}")



# Begins logic of game before rendering any GUI elements
start_game()

# Main Title
title_frame = tk.Frame(window, width=500, height=50,background='lightblue')
title_frame.pack(side=tk.TOP, fill=tk.X)
title_label = tk.Label(title_frame, text="HANGMAN", font=("Helvetica", 20),background='lightblue')
title_label.pack(pady=10)

# Hangman Frame
gallowsbuilder(window)

# Word Frame
wordbuilder(window)

# Guesses Frame
guessbuilder(window)

# Keys
keybuilder(window)
add_reset_button(window)
add_info_button(window)
add_quit_button(window)



if __name__ == '__main__':
    window.mainloop()
