import tkinter as tk

root = tk.Tk()
root.title("Skvělá gui")
root.geometry("400x300")

label = tk.Label(root, text="Bla bla bla")
label.pack()

def on_click():
    label.config( text="Button works")
button = tk.Button(root,text="Click me!", command=on_click)
button.pack()
root.mainloop()