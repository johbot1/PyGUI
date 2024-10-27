import tkinter as tk

mainwindow = tk.Tk()


mainwindow.geometry('500x500')
mainwindow.title('Shop')
label = tk.Label(mainwindow, text="Wares", font=('Arial', 35))
label.pack()

if __name__ == '__main__':
    mainwindow.mainloop()