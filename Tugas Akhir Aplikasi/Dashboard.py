import tkinter as tk
from tkinter import Menu, ttk
from LoginUser import *
from FrmPesanan import *



class Dashboard:
    def __init__(self):
        # root window
        self.root = tk.Tk()
        self.root.title('Menu Demo')

        # Set tema
        style = ttk.Style()
        style.theme_use("winnative")

        # Menerapkan tema ke semua widget
        self.apply_theme_to_all_widgets()
        
        self.root.configure(bg='#27B6CC')

        self.__data = None
        self.__level = None
        self.root.geometry("900x400")

        # create a menubar
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)

        # create menus
        self.file_menu = Menu(self.menubar)
        self.guest_menu = Menu(self.menubar)
        self.admin_menu = Menu(self.menubar)
        self.mahasiswa_menu = Menu(self.menubar)
        self.dosen_menu = Menu(self.menubar)
        
        # tambah pilihan menu ke file menu
        self.file_menu.add_command(label='Login', command=lambda: self.new_window("Log Me In", LoginApp))
        self.file_menu.add_command(label='Exit', command=self.root.destroy)
        
        self.mahasiswa_menu.add_command(label='Sewa Properti Hajat', command=lambda: self.new_window("Aplikasi Sewa Properti Hajat", FormPesanan))

        # add menus to the menubar
        self.menubar.add_cascade(label="File", menu=self.file_menu)

    def apply_theme_to_all_widgets(self):
        style = ttk.Style()
        style.theme_use("winnative")
        # Menerapkan tema ke semua widget
        for cls in ("TButton", "TLabel", "TEntry", "TFrame", "TCheckbutton", "TRadiobutton", "TNotebook"):
            style.configure(cls)

    def new_window(self, title, _class):
        new = tk.Toplevel(self.root)
        new.transient(self.root)
        _class(new, title, self.update_main_window)

    def update_main_window(self, data):
        # Method to receive data from child windows
        self.__data = data
        login_valid = self.__data[1]  # Hanya perlu mengecek login berhasil atau tidak
        if login_valid:
            login_window = self.__data[2]  # Dapatkan objek Tkinter dari data
            login_window.destroy()  # Tutup jendela login
            index = self.file_menu.index('Login')
            # hapus menu login
            self.file_menu.delete(index)
            self.file_menu.add_command(label='Logout', command=self.Logout)
            # Tambahkan menu tambahan setelah login berhasil
            self.add_extra_menus()


    def add_extra_menus(self):
        # Contoh: tambahkan menu setelah login berhasil
        self.menubar.add_cascade(label="Penyewaan", menu=self.mahasiswa_menu)

    def Logout(self):
        index = self.file_menu.index('Logout')
        self.file_menu.delete(index)
        self.file_menu.add_command(label='Login', command=lambda: self.new_window("Log Me In", LoginApp))
        self.remove_all_menus()

    def remove_all_menus(self):
        index = self.menubar.index(self.__level)
        if index is not None:
            self.menubar.delete(index)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    menu_app = Dashboard()
    menu_app.run()
