import os
import tkinter as tk

root = tk.Tk()
root.title("Java Loader")


def runapp():
    os.system('python compilor.py')


canvas = tk.Canvas(root, height="300", width="300", bg="pink")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relheight="0.8", relwidth="0.8", relx="0.1", rely="0.1")

label = tk.Label(frame, text='Welcome To \n Group \n 2 Java \n Compilor.', font=('georgia', 20, 'bold'), fg='green')
label.pack()


ranApp = tk.Button(root, text="Load Java Compilor. Click Here", padx=10, pady=5, fg="red", bg="pink",font=('georgia', 9, 'bold'), command=runapp)
ranApp.pack()


root.mainloop()

