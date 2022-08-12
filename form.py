import tkinter as tk
import mysql.connector as c

conn = c.connect(host='localhost', user='root', passwd='Ram#1212')
mycursor = conn.cursor()

def DatabaseEntry():
    name = txt_entry1.get()
    id = txt_entry2.get()
    year = txt_entry3.get()
    genre = txt_entry4.get()
    collection = txt_entry5.get()
    mycursor.execute("insert into movies value(?,?,?,?,?);", (id, name, year, genre, collection))


window = tk.Tk()
window.geometry("500x350")
window.title("Movie detail")
lbl_name = tk.Label(window, text = "Name of Movie: ", anchor='nw')
txt_entry1 = tk.Entry(window)
lbl_Id = tk.Label(window, text = "Movie ID: ", anchor='nw')
txt_entry2 = tk.Entry(window)
lbl_year = tk.Label(window, text = "Release year: ", anchor='nw')
txt_entry3 = tk.Entry(window)
lbl_genre = tk.Label(window, text = "Enter Genre of movie: ", anchor='nw')
txt_entry4 = tk.Entry(window)
lbl_Collection = tk.Label(window, text = "Box Office Collection: ", anchor='nw')
txt_entry5 = tk.Entry(window)
btn_sample = tk.Button(window, text = "Submit", command = DatabaseEntry, fg ='red')

lbl_name.pack()
txt_entry1.pack()
lbl_Id.pack()
txt_entry2.pack()
lbl_year.pack()
txt_entry3.pack()
lbl_genre.pack()
txt_entry4.pack()
lbl_Collection.pack()
txt_entry5.pack()
btn_sample.pack()

window.mainloop()
