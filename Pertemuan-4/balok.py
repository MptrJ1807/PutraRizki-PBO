import tkinter as tk
from tkinter import Label, Entry, Button, END, W

def hitung_luas():
    p = float(txtPanjang.get())
    l = float(txtLebar.get())
    t = float(txtTinggi.get())
    
    luas_permukaan = round(2 * (p*l + p*t + l*t), 2)
    
    txtLuasPermukaan.delete(0, END)
    txtLuasPermukaan.insert(END, luas_permukaan)
    
    
def hitung_volume():
    p = float(txtPanjang.get())
    l = float(txtLebar.get())
    t = float(txtTinggi.get())
    
    volume = round(p * l * t, 2)
    
    txtVolume.delete(0, END)
    txtVolume.insert(END, volume)

def hitung():
    hitung_luas()
    hitung_volume()


# Create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Volume dan Luas Permukaan balok")

# Windows
frame = tk.Frame(app)
frame.pack(padx=60, pady=60)

# Label Nama
nama_label = Label(frame, text="Nama : Muhammad Putra Rizki Julianto  : 220511080")
nama_label.grid(row=0, column=0, columnspan=2, sticky=W, padx=5, pady=5)

# Label panjang
Panjang_label = Label(frame, text="Panjang:")
Panjang_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Textbox panjang
txtPanjang = Entry(frame)
txtPanjang.grid(row=1, column=1)

# Label lebar
Lebar_label = Label(frame, text="Lebar:")
Lebar_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Textbox lebar
txtLebar = Entry(frame)
txtLebar.grid(row=2, column=1)

# Label tinggi
Tinggi_label = Label(frame, text="Tinggi:")
Tinggi_label.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Textbox tinggi
txtTinggi = Entry(frame)
txtTinggi.grid(row=3, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=4, column=0, columnspan=2, pady=5)

# Output Label Luas Permukaan
luas_permukaan_label = Label(frame, text="Luas Permukaan: ")
luas_permukaan_label.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan
txtLuasPermukaan = Entry(frame)
txtLuasPermukaan.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Label Volume
volume_label = Label(frame, text="Volume: ")
volume_label.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=6, column=1, sticky=W, padx=5, pady=5)


app.mainloop()
