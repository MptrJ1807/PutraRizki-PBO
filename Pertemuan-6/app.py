import tkinter as tk
from tkinter import Menu
from japanese import *
from russian import *
from perancis import *

# root window
root = tk.Tk()
root.title('Menu Demo')
#root.attributes('-fullscreen', True)
root.geometry("900x400")
# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create a menu
file_menu = Menu(menubar)
app_menu = Menu(menubar)
data_menu = Menu(menubar)

# add a menu item to the menu
file_menu.add_command(
    label='File Open', command=root.destroy
)

file_menu.add_command(
    label='Exit', command=root.destroy
)



def new_window( number, _class):
    new = tk.Toplevel()
    new.transient()
    new.grab_set()
    _class(new, number)

# add the File menu to the menubar

menubar.add_command(
    label='Bahasa jepang', command= lambda: new_window("Bahasa Jepang", japanese)
)
menubar.add_command(
    label='Bahasa Russia', command= lambda: new_window("Bahasa Russia", russian)
)
menubar.add_command(
    label='Bahasa Perancis', command= lambda: new_window("Bahasa Perancis", perancis)
)
    
root.mainloop()