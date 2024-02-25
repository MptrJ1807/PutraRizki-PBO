# filename : FrmPesanan.py
import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Pesanan import Pesanan
from Barang_dipinjam import *
from Tarif_perhari import *
from datetime import datetime
# pip install tkcalendar
from tkcalendar import Calendar, DateEntry
class FormPesanan:   
    def __init__(self, parent, title, update_main_window):
        self.parent = parent
        self.update_main_window = update_main_window
        self.parent.geometry("1342x550")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        
        self.style = ttk.Style()
        self.style.theme_use('winnative')  # Menggunakan tema 'clam' agar sesuai dengan Tkinter default
        
        
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        
         # varchar 
        Label(mainFrame, text='NAMA_PEMINJAM:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox NAMA_PEMINJAM
        self.txtNAMA_PEMINJAM = Entry(mainFrame, border=0,font=('Microsoft Yahei UI Light',11)) 
        self.txtNAMA_PEMINJAM.grid(row=0, column=1, padx=5, pady=5)
        Frame(mainFrame,width=162,height=2,bg='black').place(x=130,y=29.4)
                
         # varchar 
        Label(mainFrame, text='NIK_KTP:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Frame(mainFrame,width=162,height=2,bg='black').place(x=130,y=65.4)
        # Textbox NIK_KTP
        self.txtNIK_KTP = Entry(mainFrame, border=0,font=('Microsoft Yahei UI Light',11)) 
        self.txtNIK_KTP.grid(row=1, column=1, padx=5, pady=5)
        self.txtNIK_KTP.bind("<Return>",self.onCari) # menambahkan event Enter key
        
                
         # varchar 
        Label(mainFrame, text='ALAMAT:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Textbox ALAMAT
        self.txtALAMAT = Entry(mainFrame, border=0,font=('Microsoft Yahei UI Light',11)) 
        self.txtALAMAT.grid(row=2, column=1, padx=5, pady=5)
        Frame(mainFrame,width=162,height=2,bg='black').place(x=130,y=101.4)
         # varchar 
         
        Label(mainFrame, text='NOMOR_TELEPON:').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        # Textbox NOMOR_TELEPON
        self.txtNOMOR_TELEPON = Entry(mainFrame, border=0,font=('Microsoft Yahei UI Light',11)) 
        self.txtNOMOR_TELEPON.grid(row=3, column=1, padx=5, pady=5)
        Frame(mainFrame,width=162,height=2,bg='black').place(x=130,y=135.4)
         # date 
         
        Label(mainFrame, text='TANGGAL:').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        # Date Input TANGGAL
        self.txtTANGGAL = DateEntry(mainFrame, width= 23, foreground= "#9BD1E8",bd=0, date_pattern='y-mm-dd') 
        self.txtTANGGAL.grid(row=4, column=1, padx=5, pady=5)
        Frame(mainFrame,width=163,height=2,bg='black').place(x=129,y=170)
         # date 
         
        Label(mainFrame, text='TANGGAL_MEMINJAM:').grid(row=0, column=3, sticky=W, padx=5, pady=5)
        # Date Input TANGGAL_MEMINJAM
        self.txtTANGGAL_MEMINJAM = DateEntry(mainFrame, width= 23, foreground= "#9BD1E8",bd=0, date_pattern='y-mm-dd')
        self.txtTANGGAL_MEMINJAM.grid(row=0, column=4, padx=5, pady=5)
        Frame(mainFrame,width=163,height=2,bg='black').place(x=444,y=27.4)
         # date 
         
        Label(mainFrame, text='TANGGAL_KEMBALI:').grid(row=1, column=3, sticky=W, padx=5, pady=5)
        # Date Input TANGGAL_KEMBALI
        self.txtTANGGAL_KEMBALI = DateEntry(mainFrame, width= 23, foreground= "#9BD1E8",bd=0, date_pattern='y-mm-dd')
        self.txtTANGGAL_KEMBALI.grid(row=1, column=4, padx=5, pady=5)
        Frame(mainFrame,width=163,height=2,bg='black').place(x=444,y=63.4)
         # varchar 
        # Combo Box BARANG_DIPINJAM
        Label(mainFrame, text='BARANG_DIPINJAM:').grid(row=5, column=0, padx=5, pady=5)
        barang_dipinjam_data = self.get_barang_dipinjam_data()
        self.txtBARANG_DIPINJAM_ID = ttk.Combobox(mainFrame, width=23,values=[nama_barang_dipinjam for nama_barang_dipinjam in barang_dipinjam_data])
        self.txtBARANG_DIPINJAM_ID.grid(row=5, column=1, padx=5, pady=5)
        self.txtBARANG_DIPINJAM_ID.bind("<<ComboboxSelected>>", self.onPropertiDisewaSelected)
        Frame(mainFrame,width=163,height=2,bg='black').place(x=129,y=205)
        
         # int 
        # Combo Box TARIF_PERHARI
        Label(mainFrame, text='TARIF_PERHARI:').grid(row=6, column=0, sticky=W, padx=5, pady=5)
        tarif_perhari_data = self.get_tarif_perhari_data() 
        self.txtTARIF_PERHARI_ID = ttk.Combobox(mainFrame, width=23,values=[nama_tarif_perhari for nama_tarif_perhari in tarif_perhari_data])
        self.txtTARIF_PERHARI_ID.grid(row=6, column=1, padx=5, pady=5)
        Frame(mainFrame,width=163,height=2,bg='black').place(x=129,y=241)
        
         # int 
        Label(mainFrame, text='TOTAL_BAYAR:').grid(row=2, column=3, sticky=W, padx=5, pady=5)
        # Textbox TOTAL_BAYAR
        self.txtTOTAL_BAYAR = Entry(mainFrame, border=0,font=('Microsoft Yahei UI Light',11)) 
        self.txtTOTAL_BAYAR.grid(row=2, column=4, padx=5, pady=5)
        Frame(mainFrame,width=162,height=2,bg='black').place(x=445,y=99.4)
        
         # enum 
        Label(mainFrame, text='STATUS_BAYAR:').grid(row=3, column=3, sticky=W, padx=5, pady=5)
        # Combo Box
        self.txtSTATUS_BAYAR = StringVar()
        CboSTATUS_BAYAR = ttk.Combobox(mainFrame, width = 23, textvariable = self.txtSTATUS_BAYAR) 
        CboSTATUS_BAYAR.grid(row=3, column=4, padx=5, pady=5)
        Frame(mainFrame,width=162,height=2,bg='black').place(x=445,y=135)
        # Adding combobox drop down list
        CboSTATUS_BAYAR['values'] = ('LUNAS','BELUM LUNAS')
        CboSTATUS_BAYAR.current()
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=20)
        self.btnSimpan.grid(row=0, column=15, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=20)
        self.btnClear.grid(row=1, column=15, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=20)
        self.btnHapus.grid(row=2, column=15, padx=5, pady=5)
        
        # define columns
        columns = ('id','nama_peminjam','nik_ktp','alamat','nomor_telepon','tanggal','tanggal_meminjam','tanggal_kembali','barang_dipinjam_id','tarif_perhari_id','total_bayar','status_bayar')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='id')
        self.tree.column('id', width="30")
        self.tree.heading('nama_peminjam', text='nama_peminjam')
        self.tree.column('nama_peminjam', width="150")
        self.tree.heading('nik_ktp', text='nik_ktp')
        self.tree.column('nik_ktp', width="100")
        self.tree.heading('alamat', text='alamat')
        self.tree.column('alamat', width="200")
        self.tree.heading('nomor_telepon', text='nomor_telepon')
        self.tree.column('nomor_telepon', width="100")
        self.tree.heading('tanggal', text='tanggal')
        self.tree.column('tanggal', width="100")
        self.tree.heading('tanggal_meminjam', text='tanggal_meminjam')
        self.tree.column('tanggal_meminjam', width="120")
        self.tree.heading('tanggal_kembali', text='tanggal_kembali')
        self.tree.column('tanggal_kembali', width="100")
        self.tree.heading('barang_dipinjam_id', text='barang_dipinjam_id')
        self.tree.column('barang_dipinjam_id', width="120")
        self.tree.heading('tarif_perhari_id', text='tarif_perhari_id')
        self.tree.column('tarif_perhari_id', width="100")
        self.tree.heading('total_bayar', text='total_bayar')
        self.tree.column('total_bayar', width="100")
        self.tree.heading('status_bayar', text='status_bayar')
        self.tree.column('status_bayar', width="100")
        # set tree position
        self.tree.place(x=0, y=280)
        self.onReload()
    
    def onClear(self, event=None):
        self.txtNAMA_PEMINJAM.delete(0,END)
        self.txtNAMA_PEMINJAM.insert(END,"")
                                
        self.txtNIK_KTP.delete(0,END)
        self.txtNIK_KTP.insert(END,"")
                                
        self.txtALAMAT.delete(0,END)
        self.txtALAMAT.insert(END,"")
                                
        self.txtNOMOR_TELEPON.delete(0,END)
        self.txtNOMOR_TELEPON.insert(END,"")
                                
        self.txtBARANG_DIPINJAM_ID.set("")
            
        self.txtTARIF_PERHARI_ID.set("")
            
        self.txtTOTAL_BAYAR.delete(0,END)
        self.txtTOTAL_BAYAR.insert(END,"")
                                
        self.txtSTATUS_BAYAR.set("")
            
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def get_barang_dipinjam_data(self):
        dt = Barang_dipinjam()
        res = dt.getComboData()
        return res 
    def get_tarif_perhari_data(self):
        dt = Tarif_perhari()
        res = dt.getComboData()
        return res 
    def onReload(self, event=None):
        # get data pesanan
        obj = Pesanan()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree.insert('',END, values=row)
            
    def onCari(self, event=None):
        nik_ktp = self.txtNIK_KTP.get()
        obj = Pesanan()
        res = obj.getByNIK_KTP(nik_ktp)
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            # self.txtNama.focus()
        return res
            
    def TampilkanData(self, event=None):
        nik_ktp = self.txtNIK_KTP.get()
        obj = Pesanan()
        res = obj.getByNIK_KTP(nik_ktp)
            
        self.txtNAMA_PEMINJAM.delete(0,END)
        self.txtNAMA_PEMINJAM.insert(END,obj.nama_peminjam)
                                
        self.txtALAMAT.delete(0,END)
        self.txtALAMAT.insert(END,obj.alamat)
                                
        self.txtNOMOR_TELEPON.delete(0,END)
        self.txtNOMOR_TELEPON.insert(END,obj.nomor_telepon)
                                
        self.txtTANGGAL.delete(0,END)
        self.txtTANGGAL.insert(END,obj.tanggal)
                                
        self.txtTANGGAL_MEMINJAM.delete(0,END)
        self.txtTANGGAL_MEMINJAM.insert(END,obj.tanggal_meminjam)
                                
        self.txtTANGGAL_KEMBALI.delete(0,END)
        self.txtTANGGAL_KEMBALI.insert(END,obj.tanggal_kembali)
                                
        self.txtBARANG_DIPINJAM_ID.set(obj.barang_dipinjam_id) 
                                
        self.txtTARIF_PERHARI_ID.set(obj.tarif_perhari_id) 
                                
        self.txtTOTAL_BAYAR.delete(0,END)
        self.txtTOTAL_BAYAR.insert(END,obj.total_bayar)
                                
        self.txtSTATUS_BAYAR.set(obj.status_bayar)
            
        self.btnSimpan.config(text="Update")
    def onSimpan(self, event=None):
        nama_peminjam = self.txtNAMA_PEMINJAM.get()
        nik_ktp = self.txtNIK_KTP.get()
        alamat = self.txtALAMAT.get()
        nomor_telepon = self.txtNOMOR_TELEPON.get()
        tanggal = self.txtTANGGAL.get()
        tanggal_meminjam = self.txtTANGGAL_MEMINJAM.get()
        tanggal_kembali = self.txtTANGGAL_KEMBALI.get()
        barang_dipinjam_id = self.txtBARANG_DIPINJAM_ID.get()
        tarif_perhari_id = self.txtTARIF_PERHARI_ID.get()
        
        status_bayar = self.txtSTATUS_BAYAR.get()  
        
                # Hitung selisih bulan antara tanggal mulai dan tanggal selesai
        selisih_hari = (datetime.strptime(tanggal_kembali, '%Y-%m-%d') - datetime.strptime(tanggal_meminjam, '%Y-%m-%d')).days
        
        # Ambil tarif perbulan dari database berdasarkan tarif_perbulan_id
        obj_tarif = Tarif_perhari()
        tarif = obj_tarif.getById(tarif_perhari_id)
        tarif_perhari = tarif
            
        # Hitung total bayar
        total_bayar = selisih_hari * tarif_perhari
             
        obj = Pesanan()
        obj.nama_peminjam = nama_peminjam
        obj.nik_ktp = nik_ktp
        obj.alamat = alamat
        obj.nomor_telepon = nomor_telepon
        obj.tanggal = tanggal
        obj.tanggal_meminjam = tanggal_meminjam
        obj.tanggal_kembali = tanggal_kembali
        obj.barang_dipinjam_id = barang_dipinjam_id
        obj.tarif_perhari_id = tarif_perhari_id
        obj.total_bayar = total_bayar
        obj.status_bayar = status_bayar
        if(self.ditemukan==True):
            res = obj.updateByNIK_KTP(nik_ktp)
            ket = 'Diperbarui'
            
        else:
            res = obj.simpan()
            ket = 'Disimpan'
            
            
        rec = obj.affected
        if(rec>0):
            self.tree.insert('', END, values=(obj.id, nama_peminjam, nik_ktp, alamat, nomor_telepon, tanggal, tanggal_meminjam, tanggal_kembali, barang_dipinjam_id, tarif_perhari_id, total_bayar, status_bayar))
            
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec
 
    def onDelete(self, event=None):
        nik_ktp = self.txtNIK_KTP.get()
        obj = Pesanan()
        obj.nik_ktp = nik_ktp
        if(self.ditemukan==True):
            res = obj.deleteByNIK_KTP(nik_ktp)
            rec = obj.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
 
 
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
        
    def onPropertiDisewaSelected(self, event=None):
        properti_dipilih = self.txtBARANG_DIPINJAM_ID.get()
        if properti_dipilih == "KursiLipat":
            self.txtTARIF_PERHARI_ID.set("20000")
        elif properti_dipilih == "MejaPersegi":
            self.txtTARIF_PERHARI_ID.set("30000")
        elif properti_dipilih == "AlatMakan":
            self.txtTARIF_PERHARI_ID.set("350000")
        elif properti_dipilih == "MicDanSpeaker":
            self.txtTARIF_PERHARI_ID.set("350000")
        elif properti_dipilih == "Genset":
            self.txtTARIF_PERHARI_ID.set("400000")
        elif properti_dipilih == "TendaKerucut":
            self.txtTARIF_PERHARI_ID.set("500000")
        elif properti_dipilih == "Pelaminan":
            self.txtTARIF_PERHARI_ID.set("600000")
        
if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormPesanan(root, "Aplikasi Data Pesanan")
    root.mainloop() 
    
