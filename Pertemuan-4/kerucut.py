import tkinter as tk
import math
from tkinter import Label, Entry, Button, END, W

def hitung_luas():
    r = float(txtJariJari.get())
    h = float(txtTinggi.get())
    s = float(txtPelukis.get())
    
    luas_permukaan = round(math.pi * r**2 + math.pi * r * s, 2)
    
    txtLuasPermukaan.delete(0, END)
    txtLuasPermukaan.insert(END, luas_permukaan)
    
    
def hitung_volume():
    r = float(txtJariJari.get())
    h = float(txtTinggi.get())
    s = float(txtPelukis.get())
    
    volume = round((1/3) * math.pi * r**2 * h, 2)
    
    txtVolume.delete(0, END)
    txtVolume.insert(END, volume)

def hitung():
    hitung_luas()
    hitung_volume()


# Create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Volume dan Luas Permukaan prisma segitiga")

# Windows
frame = tk.Frame(app)
frame.pack(padx=60, pady=60)

# Label Nama
nama_label = Label(frame, text="Nama : Muhammad Putra Rizki Julianto  : 220511080")
nama_label.grid(row=0, column=0, columnspan=2, sticky=W, padx=5, pady=5)

# Label panjang
JariJari_label = Label(frame, text="Jari - Jari:")
JariJari_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Textbox panjang
txtJariJari = Entry(frame)
txtJariJari.grid(row=1, column=1)

# Label lebar
Tinggi_label = Label(frame, text="Tinggi:")
Tinggi_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Textbox lebar
txtTinggi = Entry(frame)
txtTinggi.grid(row=2, column=1)

# Label tinggi
Pelukis_label = Label(frame, text="Garis Pelukis:")
Pelukis_label.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Textbox tinggi
txtPelukis = Entry(frame)
txtPelukis.grid(row=3, column=1)

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
