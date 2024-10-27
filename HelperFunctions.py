#HelperFunctions.py
#Author: John Botonakis
#Comments: Help from Google Gemini
#Desc: Functions to aid in the building of the GUI and
# address additional functionality where needed

import tkinter as tk


def create_alphabet_frame(window, rely_position, letters):
  """
  Creates a frame containing alphabet buttons.

  Args:
      window: The main window object.
      rely_position: The relative y position of the frame within the window.
      letters: A string containing the letters to display on the buttons.

  Returns:
      A tk.Frame object containing the alphabet buttons.
  """
  frame = tk.Frame(window, width=580, height=150)
  frame.place(relx=0.01, rely=rely_position)
  for letter in letters:
    button = tk.Button(frame, text=letter, width=5)
    button.pack(side=tk.LEFT, padx=5, pady=5)
  return frame