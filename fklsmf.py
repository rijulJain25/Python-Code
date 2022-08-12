import tkinter as tk
# for making asic screen layout
window = tk.Tk()

def mhello():
    label1 = tk.Label(window, text="Hello, nice to meet you")
    label1.pack()

# creating title for window
window.title("Creating 3 Widgets - label, textentry and button")

# creating a label widget (label1)
lbl_sample = tk.Label(window, text = "Enter you Name:")

# creating a text entry widgets
txt_entry = tk.Entry(window)

# creating a button widgets(called btn)
btn_sample = tk.Button(window, text = "Click here", command = mhello, fg ='red')

lbl_sample.pack()
txt_entry.pack()
btn_sample.pack()

window.geometry("200x150")
# tk.Label(text="This has to be the\nsimplest bit of code").pack()
# greeting = tk.Label(text="This has to be the\nsimplest bit of code")
# greeting.pack()
# Label = tk.Label(
#     text = "Hello, Tkinter",
#     foreground= "white", #set the text color to white
# )
#label.pack()
window.mainloop()
