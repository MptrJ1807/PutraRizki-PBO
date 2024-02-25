from tkinter import *
from tkinter import messagebox
import mysql.connector
from customtkinter import *
from Dashboard import Dashboard

class LoginApp:
    def __init__(self, root, title, update_main_window):
        self.root = root
        self.update_main_window = update_main_window
        self.root.title('Login Peminjam property')
        self.root.geometry('925x500+300+200')
        self.root.configure(bg="#fff")
        self.root.resizable(False, False)

        self.show_watermark()

        self.img1 = PhotoImage(file='asset1.png')
        Label(self.root, image=self.img1, bg='white').place(x=450, y=70)
        # Form login
        self.frame = Frame(self.root, width=350, height=350, bg="white")
        self.frame.place(x=50, y=70)

        

        heading = Label(self.frame, text='Sign in', fg='#7160FA', bg='white',
                        font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=120, y=5)

        self.user = Entry(self.frame, width=25, fg='black', border=0, bg='white',
                          font=('Microsoft YaHei UI Light', 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, 'Username')
        self.user.bind('<FocusIn>', self.saat_masuk)
        self.user.bind('<FocusOut>', self.saat_keluar)

        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=107)

        self.kode = Entry(self.frame, width=25, fg='black', border=0, bg='white',
                          font=('Microsoft YaHei UI Light', 11))
        self.kode.place(x=30, y=150)
        self.kode.insert(0, 'Password')
        self.kode.bind('<FocusIn>', self.saat_masuk)
        self.kode.bind('<FocusOut>', self.saat_keluar)

        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=177)

        Button(self.frame, width=39, pady=7, text='Sign in', bg='#7160FA', fg='white', border=0,
               command=self.login).place(
            x=35, y=204)
        label = Label(self.frame, text="belum memiliki akun?", fg='black', bg='white',
                      font=('Microsoft YaHei UI Light', 9))
        label.place(x=75, y=270)

        daftar = Button(self.frame, width=6, text='daftar', border=0, bg='white', cursor='hand2', fg='#7160FA',
                        command=self.signup)
        daftar.place(x=200, y=270)

    def show_watermark(self):
        watermark_label = Label(self.root,
                                text='Dibuat oleh Muhammad Putra Rizki Julianto | 220511080',
                                font=('calibri(Body)', 10), bg='white', fg='gray', anchor='sw',
                                padx=10, pady=10)
        watermark_label.pack(side=BOTTOM, anchor='sw')

    def saat_masuk(self, e):
        widget = e.widget
        if widget == self.user:
            self.user.delete(0, 'end')
        elif widget == self.kode:
            self.kode.delete(0, 'end')

    def saat_keluar(self, e):
        widget = e.widget
        if widget == self.user and self.user.get() == '':
            self.user.insert(0, 'Username')
        elif widget == self.kode and self.kode.get() == '':
            self.kode.insert(0, 'Password')

    def login(self):
        username = self.user.get()
        password = self.kode.get()
        
        query = "SELECT * FROM user WHERE Username = %s AND Password = %s"
        data = (username, password)
        result = self.execute_query(query, data, fetch=True)

        
        if result and len(result) > 0:
            messagebox.showinfo("Login Berhasil", "Selamat datang, " + username + "!")
            # Panggil metode update_main_window di Dashboard untuk memperbarui menu bar
            self.update_main_window(["level", True, self.root])  # Sertakan objek Tkinter jendela login
        else:
            messagebox.showerror("Login Gagal", "Username atau password tidak valid!")


    def signup(self):
        window=Toplevel(self.root)
        window.title("Form Registrasi")
        window.geometry('925x500+300+200')
        window.configure(bg='#fff')
        window.resizable(False,False)

        img = PhotoImage(file='asset2.png')
        Label(window,image=img,border=0,bg='white').place(x=50,y=60)

        frame=Frame(window,width=350,height=390,bg='#fff')
        frame.place(x=480,y=50)

        heading=Label(frame,text='Sign up',fg='#7160FA',bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
        heading.place(x=120,y=5)
        
        self.show_watermark(window)
        ##############-------------------------------------#####-------------------------------------##############
        def saat_masuk_regist_user(e):
            self.user_regist.delete(0, 'end')
            
        def saat_keluar_regist_user(e):
            if self.user_regist.get()=='':
                self.user_regist.insert(0,'Username')

        self.user_regist = Entry(frame,width='25',fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
        self.user_regist.place(x=30,y=80)
        self.user_regist.insert(0, 'Username')
        self.user_regist.bind('<FocusIn>', saat_masuk_regist_user)
        self.user_regist.bind('<FocusOut>', saat_keluar_regist_user)

        Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
        ##############-------------------------------------#####-------------------------------------##############
        def saat_masuk_regist_password(e):
            self.kode_regist.delete(0, 'end')
            
        def saat_keluar_regist_password(e):
            if self.kode_regist.get()=='':
                self.kode_regist.insert(0,'Password')

        self.kode_regist = Entry(frame,width='25',fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
        self.kode_regist.place(x=30,y=150)
        self.kode_regist.insert(0, 'Password')
        self.kode_regist.bind('<FocusIn>', saat_masuk_regist_password)
        self.kode_regist.bind('<FocusOut>', saat_keluar_regist_password)

        Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
        ##############-------------------------------------#####-------------------------------------##############
        def saat_masuk_regist_konfirm(e):
            self.konfir_kode_regist.delete(0, 'end')
            
        def saat_keluar_regist_konfirm(e):
            if self.konfir_kode_regist.get()=='':
                self.konfir_kode_regist.insert(0,'Confirm Password')

        self.konfir_kode_regist = Entry(frame,width='25',fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
        self.konfir_kode_regist.place(x=30,y=220)
        self.konfir_kode_regist.insert(0, 'Confirm Password')
        self.konfir_kode_regist.bind('<FocusIn>', saat_masuk_regist_konfirm)
        self.konfir_kode_regist.bind('<FocusOut>', saat_keluar_regist_konfirm)

        Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)
        ##############-------------------------------------#####-------------------------------------##############

        #koneksi database#
        def register_user():
            username_from_form = self.user_regist.get()
            password_from_form = self.kode_regist.get()
            confirm_password_from_form = self.konfir_kode_regist.get()
            
            if password_from_form==confirm_password_from_form:
                query = "INSERT INTO user (Username, Password) VALUES (%s, %s)"
                data = (username_from_form, password_from_form)
                self.execute_query(query, data)
                messagebox.showinfo("Registrasi Berhasil", "Registrasi berhasil dilakukan!")
                window.lift()  # Dorong jendela registrasi ke depan setelah menunjukkan notifikasi
                window.destroy()

            else:
                messagebox.showerror('invalid', "Konfirmasi Password harus sama!")


        Button(frame, width=39, pady=7, text='Sign up', bg='#7160FA', fg='white', border=0, command=register_user).place(
            x=35, y=280)

        label = Label(frame, text="Sudah memiliki akun?", fg='black', bg='white',
                      font=('Microsoft YaHei UI Light', 9))
        label.place(x=75, y=340)

        masuk = Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#7160FA')
        masuk.place(x=200, y=340)
        
        
        window.lift()  
        window.mainloop()

    def show_watermark(self, window=None):
        if window:
            watermark_label = Label(window, text='Dibuat oleh Muhammad Putra Rizki Julianto | 220511080',
                                    font=('calibri(Body)', 10), bg='white', fg='gray', anchor='sw',
                                    padx=10, pady=10)
            watermark_label.pack(side=BOTTOM, anchor='sw')
        else:
            watermark_label = Label(self.root,
                                    text='Dibuat oleh Muhammad Putra Rizki Julianto | 220511080',
                                    font=('calibri(Body)', 10), bg='white', fg='gray', anchor='sw',
                                    padx=10, pady=10)
            watermark_label.pack(side=BOTTOM, anchor='sw')

    def connect_db(self):
        try:
            connection = mysql.connector.connect(
                host="sql.freedb.tech",
                user="freedb_PutraRJ303",
                password="tc5PUE#@K@53?dy",
                database="freedb_PropertiHajat"
            )
            return connection
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
            return None

    def execute_query(self, query, data=None, fetch=False):
        connection = self.connect_db()
        if connection:
            try:
                cursor = connection.cursor()
                if data:
                    cursor.execute(query, data)
                else:
                    cursor.execute(query)

                if fetch:
                    result = cursor.fetchall()
                    return result
                else:
                    connection.commit()
                    return cursor
            except mysql.connector.Error as err:
                messagebox.showerror("Query Error", f"Error: {err}")
            finally:
                cursor.close()
                connection.close()

if __name__ == '__main__':
    root = Tk()
    menu_app = Dashboard()
    aplikasi = LoginApp(root, update_main_window=menu_app.update_main_window)
    root.mainloop()