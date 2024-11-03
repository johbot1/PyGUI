#Words.py
#Author: John Botonakis
#Comments: Commenting Help from Google Gemini
#Desc: A place to house the word list that players are able to guess from

import random as r

words = ["python", "linux", "windows", "java", "javascript", "php",
         "ruby", "swift", "kotlin", "golang", "rust", "typescript", "html", "css",
        "mongo", "mysql", "postgres", "oracle", "docker", "kubernetes",
         "azure", "devops", "google","firefox", "cloud", "server",
         "blockchain", "crypto", "cybersecurity", "software", "hardware", "network", "data"]

def choose_word():
    r.shuffle(words)
    return words[r.randint(0,len(words)-1)]