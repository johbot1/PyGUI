# Main.py
# Author: John Botonakis
# Desc: Holds the main logic for displaying the window and it's pieces
from HelperFunctions import *


#FEEDBACK
# DONE      Add .gitignore
# DONE      FIX width
#           Ask for name before displaying anything!
#           Button Clickability
#           QUit Button
#           When letter is selected, turn dark/unclickable (Visual indication that it's no longer clickable)
#           Exit program when DO not want to play again


# Main window Setup
window = tk.Tk()
window.geometry('600x600')
window.title('Hangman!')
window.resizable(False, False)
window.focus_force()

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
title_frame = tk.Frame(window, width=500, height=50)
title_frame.pack(side=tk.TOP, fill=tk.X)
title_label = tk.Label(title_frame, text="HANGMAN", font=("Helvetica", 20))
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

if __name__ == '__main__':
    window.mainloop()
