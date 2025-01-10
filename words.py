# Words.py
# Author: John Botonakis
# Desc:
# This holds the wordbank for all possible words, along with the function to choose from those words

import random as r

words = ["python", "linux", "windows", "java", "javascript", "php",
         "ruby", "swift", "kotlin", "golang", "rust", "typescript", "html", "css",
         "mongo", "mysql", "postgres", "oracle", "docker", "kubernetes",
         "azure", "devops", "google", "firefox", "cloud", "server",
         "blockchain", "crypto", "cybersecurity", "software", "hardware", "network", "data"]


# Choose_word:
# Simple shuffle and return a random word from the word bank
def choose_word():
    r.shuffle(words)
    return words[r.randint(0, len(words) - 1)]


# Author: Chris Horton
# GitHub: https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
HANGMANPICS = ['''
  +---+
      |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
