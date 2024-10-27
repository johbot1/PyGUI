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
gallows_frame = tk.Frame(window, bg="pink", width=185, height=300, relief=tk.RAISED)
gallows_frame.place(relx=0.68, rely=0.1)


#Guesses Frame
guessed_letters_frame = tk.Frame(window, bg="green", width=200, height=50)
guessed_letters_frame.place(relx=0.01, rely=0.1, relwidth=0.5, relheight=0.2)


#Keys
alphabet_frame1 = tk.Frame(window, width=580, height=150)
alphabet_frame1.place(relx=0.01, rely=0.7)
alphabet_frame2 = tk.Frame(window, width=580, height=150)
alphabet_frame2.place(relx=0.05, rely=0.78)
alphabet_frame3 = tk.Frame(window, width=580, height=150)
alphabet_frame3.place(relx=0.1, rely=0.86)
alphabet_buttons = []

line1 = "QWERTYUIOP"
line2 = "ASDFGHJKL"
line3 = "ZXCVBNM"

for letter in line1:
    button = tk.Button(alphabet_frame1, text=letter, width=5)
    button.pack(side=tk.LEFT, padx=5, pady=5)
    alphabet_buttons.append(button)
for letter in line2:
    button = tk.Button(alphabet_frame2, text=letter, width=5)
    button.pack(side=tk.LEFT, padx=5, pady=5)
    alphabet_buttons.append(button)
for letter in line3:
    button = tk.Button(alphabet_frame3, text=letter, width=5)
    button.pack(side=tk.LEFT, padx=5, pady=5)
    alphabet_buttons.append(button)



if __name__ == '__main__':
    window.mainloop()