import tkinter as tk
from tkinter import Entry,Button,END, filedialog, Text,LEFT,RIGHT,X
def openfile():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/M S I/Documents/Latihan/",
        title="Open text file",
        filetypes=(("text file", "*.txt"),)
    )
    pathh.insert(END, tf)
    tf = open(tf) # or tf = open(tf, 'r')
    data = tf.read()
    txtarea.insert(END, data)
    tf.close

def savefile():
    teks = pathh.get()
    with open(pathh.get(),"w")as file1:
        file1.write(txtarea.get(1.0,"end-1c") )

    txtarea.delete("1.0", "end")
    file1.clos()
ws = tk.Tk()
ws.title("PhytonGuides")
ws.geometry("400x450")
ws['bg']='#fb0'
txtarea = Text(ws, width=40, height=20)
txtarea.pack(pady=20)
pathh = Entry(ws)
pathh.pack(side=LEFT, expand=True, fill=X, padx=20)
Button(
    ws,
    text="openfile",
    command=openfile
    ).pack(side=RIGHT, expand=True, fill=X, padx=20)
Button(
    ws,
    text="Save File",
    command=savefile
    ).pack(side=RIGHT, expand=True, fill=X, padx=20)
ws.mainloop()