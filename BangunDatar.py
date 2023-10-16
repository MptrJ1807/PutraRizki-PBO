import tkinter as tk
import math
from tkinter import ttk


class BangunDatarCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Bangun Datar")
        self.root.geometry("600x470")

        self.notebook = ttk.Notebook(self.root)

        self.persegi_frame = ttk.Frame(self.notebook)
        self.persegi_panjang_frame = ttk.Frame(self.notebook)
        self.jajar_genjang_frame = ttk.Frame(self.notebook)
        self.segitiga_frame = ttk.Frame(self.notebook)
        self.belah_ketupat_frame = ttk.Frame(self.notebook)
        self.layang_layang_frame = ttk.Frame(self.notebook)
        self.trapesium_frame = ttk.Frame(self.notebook)
        self.lingkaran_frame = ttk.Frame(self.notebook)

        self.notebook.add(self.persegi_frame, text="Persegi")
        self.notebook.add(self.persegi_panjang_frame, text="Persegi Panjang")
        self.notebook.add(self.jajar_genjang_frame, text="Jajar Genjang")
        self.notebook.add(self.segitiga_frame, text="Segitiga")
        self.notebook.add(self.belah_ketupat_frame, text = "Belah ketupat")
        self.notebook.add(self.layang_layang_frame, text="Layang Layang")
        self.notebook.add(self.trapesium_frame, text="Trapesium")
        self.notebook.add(self.lingkaran_frame, text ="Lingkaran")

        self.notebook.pack(pady=0)

        self.setup_persegi_ui()
        self.setup_persegi_panjang_ui()
        self.setup_jajar_genjang_ui()
        self.setup_segitiga_ui()
        self.setup_belah_ketupat_ui()
        self.setup_layang_layang_ui()
        self.setup_trapesium_ui()
        self.setup_lingkaran_ui()
        
        
    
    def setup_persegi_ui(self):
        # Variabel untuk menyimpan panjang sisi
        self.sisi_var = tk.DoubleVar()

        # Label dan entry untuk panjang sisi
        label_sisi = ttk.Label(self.persegi_frame, text="Panjang Sisi:")
        label_sisi.pack(pady=10)

        entry_sisi = ttk.Entry(self.persegi_frame, textvariable=self.sisi_var)
        entry_sisi.pack(pady=10)

        # Tombol untuk menghitung keliling
        btn_keliling = ttk.Button(self.persegi_frame, text="Hitung Keliling", command=self.hitung_persegi_keliling)
        btn_keliling.pack(pady=5)

        # Tombol untuk menghitung luas
        btn_luas = ttk.Button(self.persegi_frame, text="Hitung Luas", command=self.hitung_persegi_luas)
        btn_luas.pack(pady=5)

    def setup_persegi_panjang_ui(self):
        # Variabel untuk menyimpan panjang dan lebar
        self.panjang_var = tk.DoubleVar()
        self.lebar_var = tk.DoubleVar()

        # Label dan entry untuk panjang
        label_panjang = ttk.Label(self.persegi_panjang_frame, text="Panjang:")
        label_panjang.pack(pady=5)

        entry_panjang = ttk.Entry(self.persegi_panjang_frame, textvariable=self.panjang_var)
        entry_panjang.pack(pady=5)

        # Label dan entry untuk lebar
        label_lebar = ttk.Label(self.persegi_panjang_frame, text="Lebar:")
        label_lebar.pack(pady=5)

        entry_lebar = ttk.Entry(self.persegi_panjang_frame, textvariable=self.lebar_var)
        entry_lebar.pack(pady=5)

        # Tombol untuk menghitung keliling
        btn_keliling = ttk.Button(self.persegi_panjang_frame, text="Hitung Keliling",
                                  command=self.hitung_persegi_panjang_keliling)
        btn_keliling.pack(pady=5)

        # Tombol untuk menghitung luas
        btn_luas = ttk.Button(self.persegi_panjang_frame, text="Hitung Luas",
                              command=self.hitung_persegi_panjang_luas)
        btn_luas.pack(pady=5)

    def setup_jajar_genjang_ui(self):
        # Variabel untuk menyimpan panjang, tinggi, dan alas
        self.alas_jajar_genjang_var = tk.DoubleVar()
        self.tinggi_jajar_genjang_var = tk.DoubleVar()
        self.sisi1_jajar_genjang_var = tk.DoubleVar()
        self.sisi2_jajar_genjang_var = tk.DoubleVar()
        self.sisi3_jajar_genjang_var = tk.DoubleVar()
        self.sisi4_jajar_genjang_var = tk.DoubleVar()

        # Label dan entry untuk alas
        label_alas_jajar_genjang = ttk.Label(self.jajar_genjang_frame, text="Alas:")
        label_alas_jajar_genjang.pack(pady=5)

        entry_alas_jajar_genjang = ttk.Entry(self.jajar_genjang_frame, textvariable=self.alas_jajar_genjang_var)
        entry_alas_jajar_genjang.pack(pady=5)

        # Label dan entry untuk tinggi
        label_tinggi_jajar_genjang = ttk.Label(self.jajar_genjang_frame, text="Tinggi:")
        label_tinggi_jajar_genjang.pack(pady=5)

        entry_tinggi_jajar_genjang = ttk.Entry(self.jajar_genjang_frame, textvariable=self.tinggi_jajar_genjang_var)
        entry_tinggi_jajar_genjang.pack(pady=5)

        # Label dan entry untuk sisi miring
        label_sisi1_jajar_genjang = ttk.Label(self.jajar_genjang_frame, text="Sisi 1:")
        label_sisi1_jajar_genjang.pack(pady=5)

        entry_sisi1_jajar_genjang = ttk.Entry(self.jajar_genjang_frame, textvariable=self.sisi1_jajar_genjang_var)
        entry_sisi1_jajar_genjang.pack(pady=5)
        
        label_sisi2_jajar_genjang = ttk.Label(self.jajar_genjang_frame, text="Sisi 2:")
        label_sisi2_jajar_genjang.pack(pady=5)

        entry_sisi2_jajar_genjang = ttk.Entry(self.jajar_genjang_frame, textvariable=self.sisi2_jajar_genjang_var)
        entry_sisi2_jajar_genjang.pack(pady=5)
        
        label_sisi3_jajar_genjang = ttk.Label(self.jajar_genjang_frame, text="Sisi 3:")
        label_sisi3_jajar_genjang.pack(pady=5)

        entry_sisi3_jajar_genjang = ttk.Entry(self.jajar_genjang_frame, textvariable=self.sisi3_jajar_genjang_var)
        entry_sisi3_jajar_genjang.pack(pady=5)
        
        label_sisi4_jajar_genjang = ttk.Label(self.jajar_genjang_frame, text="Sisi 4:")
        label_sisi4_jajar_genjang.pack(pady=5)

        entry_sisi4_jajar_genjang = ttk.Entry(self.jajar_genjang_frame, textvariable=self.sisi4_jajar_genjang_var)
        entry_sisi4_jajar_genjang.pack(pady=5)

        # Tombol untuk menghitung keliling
        btn_keliling = ttk.Button(self.jajar_genjang_frame, text="Hitung Keliling",
                                  command=self.hitung_jajar_genjang_keliling)
        btn_keliling.pack(pady=5)

        # Tombol untuk menghitung luas
        btn_luas = ttk.Button(self.jajar_genjang_frame, text="Hitung Luas",
                              command=self.hitung_jajar_genjang_luas)
        btn_luas.pack(pady=5)
        
    def setup_segitiga_ui(self):
        # Variabel untuk menyimpan alas, tinggi, dan sisi-sisi segitiga
        self.alas_segitiga_var = tk.DoubleVar()
        self.tinggi_segitiga_var = tk.DoubleVar()
        self.sisi1_segitiga_var = tk.DoubleVar()
        self.sisi2_segitiga_var = tk.DoubleVar()
        self.sisi3_segitiga_var = tk.DoubleVar()

        # Label dan entry untuk alas segitiga
        label_alas_segitiga = ttk.Label(self.segitiga_frame, text="Alas:")
        label_alas_segitiga.pack(pady=5)

        entry_alas_segitiga = ttk.Entry(self.segitiga_frame, textvariable=self.alas_segitiga_var)
        entry_alas_segitiga.pack(pady=5)

        # Label dan entry untuk tinggi segitiga
        label_tinggi_segitiga = ttk.Label(self.segitiga_frame, text="Tinggi:")
        label_tinggi_segitiga.pack(pady=5)

        entry_tinggi_segitiga = ttk.Entry(self.segitiga_frame, textvariable=self.tinggi_segitiga_var)
        entry_tinggi_segitiga.pack(pady=5)

        # Label dan entry untuk sisi-sisi segitiga
        label_sisi1_segitiga = ttk.Label(self.segitiga_frame, text="Sisi 1:")
        label_sisi1_segitiga.pack(pady=5)

        entry_sisi1_segitiga = ttk.Entry(self.segitiga_frame, textvariable=self.sisi1_segitiga_var)
        entry_sisi1_segitiga.pack(pady=5)
        
        label_sisi2_segitiga = ttk.Label(self.segitiga_frame, text="Sisi 2:")
        label_sisi2_segitiga.pack(pady=5)

        entry_sisi2_segitiga = ttk.Entry(self.segitiga_frame, textvariable=self.sisi2_segitiga_var)
        entry_sisi2_segitiga.pack(pady=5)

        label_sisi3_segitiga = ttk.Label(self.segitiga_frame, text="Sisi 3:")
        label_sisi3_segitiga.pack(pady=5)

        entry_sisi3_segitiga = ttk.Entry(self.segitiga_frame, textvariable=self.sisi3_segitiga_var)
        entry_sisi3_segitiga.pack(pady=5)

        # Tombol untuk menghitung keliling
        btn_keliling = ttk.Button(self.segitiga_frame, text="Hitung Keliling",
                                command=self.hitung_segitiga_keliling)
        btn_keliling.pack(pady=5)

        # Tombol untuk menghitung luas
        btn_luas = ttk.Button(self.segitiga_frame, text="Hitung Luas",
                            command=self.hitung_segitiga_luas)
        btn_luas.pack(pady=5)
        
    def setup_belah_ketupat_ui(self):
        # Variabel untuk menyimpan alas, tinggi, dan sisi-sisi segitiga
        self.dimensi1_belah_ketupat_var = tk.DoubleVar()
        self.dimensi2_belah_ketupat_var = tk.DoubleVar()
        self.sisi1_belah_ketupat_var = tk.DoubleVar()
        self.sisi2_belah_ketupat_var = tk.DoubleVar()
        self.sisi3_belah_ketupat_var = tk.DoubleVar()
        self.sisi4_belah_ketupat_var = tk.DoubleVar()
        
        #label dan entry untuk dimensi1 belah ketupat
        label_dimensi1_belah_ketupat = ttk.Label(self.belah_ketupat_frame, text="dimensi 1:")
        label_dimensi1_belah_ketupat.pack(pady=5)
        
        entry_dimensi1_belah_ketupat = ttk.Entry(self.belah_ketupat_frame, textvariable=self.dimensi1_belah_ketupat_var)
        entry_dimensi1_belah_ketupat.pack(pady=5)
        
        #label dan entry untuk dimensi2 belah ketupat
        label_dimensi2_belah_ketupat =ttk.Label(self.belah_ketupat_frame, text="dimensi 2")
        label_dimensi2_belah_ketupat.pack(pady=5)
        
        entry_dimensi2_belah_ketupat = ttk.Entry(self.belah_ketupat_frame, textvariable=self.dimensi2_belah_ketupat_var)
        entry_dimensi2_belah_ketupat.pack(pady=5)
        
        #label dan entry untuk sisi sisi belah ketupat
        label_sisi1_belah_ketupat = ttk.Label(self.belah_ketupat_frame, text="sisi 1")
        label_sisi1_belah_ketupat.pack(pady=5)
        
        entry_sisi1_belah_ketupat = ttk.Entry(self.belah_ketupat_frame, textvariable=self.sisi1_belah_ketupat_var)
        entry_sisi1_belah_ketupat.pack(pady=5)
        
        label_sisi2_belah_ketupat = ttk.Label(self.belah_ketupat_frame, text="sisi 2")
        label_sisi2_belah_ketupat.pack(pady=5)
        
        entry_sisi2_belah_ketupat = ttk.Entry(self.belah_ketupat_frame, textvariable=self.sisi2_belah_ketupat_var)
        entry_sisi2_belah_ketupat.pack(pady=5)
        
        label_sisi3_belah_ketupat = ttk.Label(self.belah_ketupat_frame, text="sisi 3")
        label_sisi3_belah_ketupat.pack(pady=5)
        
        entry_sisi3_belah_ketupat = ttk.Entry(self.belah_ketupat_frame, textvariable=self.sisi3_belah_ketupat_var)
        entry_sisi3_belah_ketupat.pack(pady=5)
        
        label_sisi4_belah_ketupat = ttk.Label(self.belah_ketupat_frame, text="sisi 4")
        label_sisi4_belah_ketupat.pack(pady=5)
        
        entry_sisi4_belah_ketupat = ttk.Entry(self.belah_ketupat_frame, textvariable=self.sisi4_belah_ketupat_var)
        entry_sisi4_belah_ketupat.pack(pady=5)
        
        # Tombol untuk menghitung keliling
        btn_keliling = ttk.Button(self.belah_ketupat_frame, text="Hitung Keliling",
                                command=self.hitung_belah_ketupat_keliling)
        btn_keliling.pack(pady=5)

        # Tombol untuk menghitung luas
        btn_luas = ttk.Button(self.belah_ketupat_frame, text="Hitung Luas",
                            command=self.hitung_belah_ketupat_luas)
        btn_luas.pack(pady=5)
        
    def setup_layang_layang_ui(self):
        # Variabel untuk menyimpan alas, tinggi, dan sisi-sisi layang layang
        self.dimensi1_layang_layang_var = tk.DoubleVar()
        self.dimensi2_layang_layang_var = tk.DoubleVar()
        self.sisi1_layang_layang_var = tk.DoubleVar()
        self.sisi2_layang_layang_var = tk.DoubleVar()
        self.sisi3_layang_layang_var = tk.DoubleVar()
        self.sisi4_layang_layang_var = tk.DoubleVar()
        
        #label dan entry untuk dimensi1 layang layang
        label_dimensi1_layang_layang = ttk.Label(self.layang_layang_frame, text="dimensi 1:")
        label_dimensi1_layang_layang.pack(pady=5)
        
        entry_dimensi1_layang_layang = ttk.Entry(self.layang_layang_frame, textvariable=self.dimensi1_layang_layang_var)
        entry_dimensi1_layang_layang.pack(pady=5)
        
        #label dan entry untuk dimensi2 layang layang
        label_dimensi2_layang_layang =ttk.Label(self.layang_layang_frame, text="dimensi 2")
        label_dimensi2_layang_layang.pack(pady=5)
        
        entry_dimensi2_layang_layang = ttk.Entry(self.layang_layang_frame, textvariable=self.dimensi2_layang_layang_var)
        entry_dimensi2_layang_layang.pack(pady=5)
        
        #label dan entry untuk sisi sisi layang layang
        label_sisi1_layang_layang = ttk.Label(self.layang_layang_frame, text="sisi 1")
        label_sisi1_layang_layang.pack(pady=5)
        
        entry_sisi1_layang_layang = ttk.Entry(self.layang_layang_frame, textvariable=self.sisi1_layang_layang_var)
        entry_sisi1_layang_layang.pack(pady=5)
        
        label_sisi2_layang_layang = ttk.Label(self.layang_layang_frame, text="sisi 2")
        label_sisi2_layang_layang.pack(pady=5)
        
        entry_sisi2_layang_layang = ttk.Entry(self.layang_layang_frame, textvariable=self.sisi2_layang_layang_var)
        entry_sisi2_layang_layang.pack(pady=5)
        
        label_sisi3_layang_layang = ttk.Label(self.layang_layang_frame, text="sisi 3")
        label_sisi3_layang_layang.pack(pady=5)
        
        entry_sisi3_layang_layang = ttk.Entry(self.layang_layang_frame, textvariable=self.sisi3_layang_layang_var)
        entry_sisi3_layang_layang.pack(pady=5)
        
        label_sisi4_layang_layang = ttk.Label(self.layang_layang_frame, text="sisi 4")
        label_sisi4_layang_layang.pack(pady=5)
        
        entry_sisi4_layang_layang = ttk.Entry(self.layang_layang_frame, textvariable=self.sisi4_layang_layang_var)
        entry_sisi4_layang_layang.pack(pady=5)
        
        # Tombol untuk menghitung keliling
        btn_keliling = ttk.Button(self.layang_layang_frame, text="Hitung Keliling",
                                command=self.hitung_layang_layang_keliling)
        btn_keliling.pack(pady=5)

        # Tombol untuk menghitung luas
        btn_luas = ttk.Button(self.layang_layang_frame, text="Hitung Luas",
                            command=self.hitung_layang_layang_luas)
        btn_luas.pack(pady=5)
        
    def setup_trapesium_ui(self):
        # Variabel untuk menyimpan alas, tinggi, dan sisi sisi trapesium
        self.alas_trapesium_var = tk.DoubleVar()
        self.tinggi_trapesium_var = tk.DoubleVar()
        self.sisi1_trapesium_var = tk.DoubleVar()
        self.sisi2_trapesium_var = tk.DoubleVar()
        self.sisi3_trapesium_var = tk.DoubleVar()
        self.sisi4_trapesium_var = tk.DoubleVar()
        
        #label dan entry untuk dimensi1 belah ketupat
        label_alas_trapesium = ttk.Label(self.trapesium_frame, text="Alas:")
        label_alas_trapesium.pack(pady=5)
        
        entry_alas_trapesium = ttk.Entry(self.trapesium_frame, textvariable=self.alas_trapesium_var)
        entry_alas_trapesium.pack(pady=5)
        
        #label dan entry untuk dimensi2 belah ketupat
        label_tinggi_trapesium =ttk.Label(self.trapesium_frame, text="Tinggi :")
        label_tinggi_trapesium.pack(pady=5)
        
        entry_tinggi_trapesium = ttk.Entry(self.trapesium_frame, textvariable=self.tinggi_trapesium_var)
        entry_tinggi_trapesium.pack(pady=5)
        
        #label dan entry untuk sisi sisi belah ketupat
        label_sisi1_trapesium = ttk.Label(self.trapesium_frame, text="sisi 1")
        label_sisi1_trapesium.pack(pady=5)
        
        entry_sisi1_trapesium = ttk.Entry(self.trapesium_frame, textvariable=self.sisi1_trapesium_var)
        entry_sisi1_trapesium.pack(pady=5)
        
        label_sisi2_trapesium = ttk.Label(self.trapesium_frame, text="sisi 2")
        label_sisi2_trapesium.pack(pady=5)
        
        entry_sisi2_trapesium = ttk.Entry(self.trapesium_frame, textvariable=self.sisi2_trapesium_var)
        entry_sisi2_trapesium.pack(pady=5)
        
        label_sisi3_trapesium = ttk.Label(self.trapesium_frame, text="sisi 3")
        label_sisi3_trapesium.pack(pady=5)
        
        entry_sisi3_trapesium = ttk.Entry(self.trapesium_frame, textvariable=self.sisi3_trapesium_var)
        entry_sisi3_trapesium.pack(pady=5)
        
        label_sisi4_trapesium = ttk.Label(self.trapesium_frame, text="sisi 4")
        label_sisi4_trapesium.pack(pady=5)
        
        entry_sisi4_trapesium = ttk.Entry(self.trapesium_frame, textvariable=self.sisi4_trapesium_var)
        entry_sisi4_trapesium.pack(pady=5)
        
        # Tombol untuk menghitung keliling
        btn_keliling = ttk.Button(self.trapesium_frame, text="Hitung Keliling",
                                command=self.hitung_trapesium_keliling)
        btn_keliling.pack(pady=5)

        # Tombol untuk menghitung luas
        btn_luas = ttk.Button(self.trapesium_frame, text="Hitung Luas",
                            command=self.hitung_trapesium_luas)
        btn_luas.pack(pady=5)
        
    def setup_lingkaran_ui(self):
        # Variabel untuk menyimpan jari-jari
        self.jari_jari_var = tk.DoubleVar()
        self.jari_jari2_var = tk.DoubleVar()

        # Label dan entry untuk jari-jari
        label_jari_jari = ttk.Label(self.lingkaran_frame, text="Jari-Jari:")
        label_jari_jari.pack(pady=10)

        entry_jari_jari = ttk.Entry(self.lingkaran_frame, textvariable=self.jari_jari_var)
        entry_jari_jari.pack(pady=10)
        
        label_jari_jari2 = ttk.Label(self.lingkaran_frame, text="Jari-Jari 2:")
        label_jari_jari2.pack(pady=10)

        entry_jari_jari2 = ttk.Entry(self.lingkaran_frame, textvariable=self.jari_jari2_var)
        entry_jari_jari2.pack(pady=10)

        # Tombol untuk menghitung keliling
        btn_keliling = ttk.Button(self.lingkaran_frame, text="Hitung Keliling",
                                command=self.hitung_lingkaran_keliling)
        btn_keliling.pack(pady=5)

        # Tombol untuk menghitung luas
        btn_luas = ttk.Button(self.lingkaran_frame, text="Hitung Luas",
                            command=self.hitung_lingkaran_luas)
        btn_luas.pack(pady=5)
        
    def hitung_lingkaran_keliling(self):
        jari_jari = self.jari_jari_var.get()
        keliling = 2 * math.pi * jari_jari
        self.tampilkan_hasil_lingkaran("Keliling Lingkaran: {:.2f}".format(keliling))

    def hitung_lingkaran_luas(self):
        jari_jari = self.jari_jari_var.get()
        luas = math.pi * jari_jari ** 2
        self.tampilkan_hasil_lingkaran("Luas Lingkaran: {:.2f}".format(luas))

    def tampilkan_hasil_lingkaran(self, hasil):
        popup = tk.Toplevel(self.root)
        popup.title("Hasil Perhitungan")
        label_hasil = ttk.Label(popup, text=hasil)
        label_hasil.pack(pady=10)
        
    def hitung_trapesium_keliling(self):
        sisi1 = self.sisi1_trapesium_var.get()
        sisi2 = self.sisi2_trapesium_var.get()
        sisi3 = self.sisi3_trapesium_var.get()
        sisi4 = self.sisi4_trapesium_var.get()
        keliling = sisi1 + sisi2 + sisi3 + sisi4
        self.tampilkan_hasil_trapesium("Keliling trapesium: {:.2f}".format(keliling))
        
    def hitung_trapesium_luas(self):
        alas = self.alas_trapesium_var.get()
        tinggi = self.tinggi_trapesium_var.get()
        sisi2 = self.sisi2_trapesium_var.get()
        luas = 0.5 * (alas + sisi2) * tinggi
        self.tampilkan_hasil_trapesium("Luas trapesium: {:.2f}".format(luas))
        
    def tampilkan_hasil_trapesium(self, hasil):
        popup = tk.Toplevel(self.root)
        popup.title("Hasil Perhitungan")
        label_hasil = ttk.Label(popup, text=hasil)
        label_hasil.pack(pady=10)
        
    def hitung_layang_layang_keliling(self):
        sisi1 = self.sisi1_layang_layang_var.get()
        sisi2 = self.sisi2_layang_layang_var.get()
        sisi3 = self.sisi3_layang_layang_var.get()
        sisi4 = self.sisi4_layang_layang_var.get()
        keliling = sisi1 + sisi2 + sisi3 + sisi4
        self.tampilkan_hasil_layang_layang("Keliling layang-layang: {:.2f}".format(keliling))

    def hitung_layang_layang_luas(self):
        dimensi1 = self.dimensi1_layang_layang_var.get()
        dimensi2 = self.dimensi2_layang_layang_var.get()
        luas = 0.5 * dimensi1 * dimensi2
        self.tampilkan_hasil_layang_layang("Luas layang-layang: {:.2f}".format(luas))

    def tampilkan_hasil_layang_layang(self, hasil):
        popup = tk.Toplevel(self.root)
        popup.title("Hasil Perhitungan")
        label_hasil = ttk.Label(popup, text=hasil)
        label_hasil.pack(pady=10)

    def hitung_belah_ketupat_keliling(self):
        sisi1 = self.sisi1_belah_ketupat_var.get()
        sisi2 = self.sisi2_belah_ketupat_var.get()
        sisi3 = self.sisi3_belah_ketupat_var.get()
        sisi4 = self.sisi4_belah_ketupat_var.get()
        keliling = sisi1 + sisi2 + sisi3 + sisi4
        self.tampilkan_hasil_belah_ketupat("Keliling Belah Ketupat: {:.2f}".format(keliling))

    def hitung_belah_ketupat_luas(self):
        dimensi1 = self.dimensi1_belah_ketupat_var.get()
        dimensi2 = self.dimensi2_belah_ketupat_var.get()
        luas = 0.5 * dimensi1 * dimensi2
        self.tampilkan_hasil_belah_ketupat("Luas Belah Ketupat: {:.2f}".format(luas))

    def tampilkan_hasil_belah_ketupat(self, hasil):
        popup = tk.Toplevel(self.root)
        popup.title("Hasil Perhitungan")
        label_hasil = ttk.Label(popup, text=hasil)
        label_hasil.pack(pady=10)
        
    def hitung_persegi_keliling(self):
        panjang_sisi = self.sisi_var.get()
        keliling = 4 * panjang_sisi
        self.tampilkan_hasil_persegi("Keliling Persegi: {:.2f}".format(keliling))

    def hitung_persegi_luas(self):
        panjang_sisi = self.sisi_var.get()
        luas = panjang_sisi ** 2
        self.tampilkan_hasil_persegi("Luas Persegi: {:.2f}".format(luas))
        
    def tampilkan_hasil_persegi(self, hasil):
        popup = tk.Toplevel(self.root)
        popup.title("Hasil Perhitungan")
        label_hasil = ttk.Label(popup, text=hasil)
        label_hasil.pack(pady=10)

    def hitung_persegi_panjang_keliling(self):
        panjang = self.panjang_var.get()
        lebar = self.lebar_var.get()
        keliling = 2 * (panjang + lebar)
        self.tampilkan_hasil_persegi_panjang("Keliling Persegi Panjang: {:.2f}".format(keliling))

    def hitung_persegi_panjang_luas(self):
        panjang = self.panjang_var.get()
        lebar = self.lebar_var.get()
        luas = panjang * lebar
        self.tampilkan_hasil_persegi_panjang("Luas Persegi Panjang: {:.2f}".format(luas))
        
    def tampilkan_hasil_persegi_panjang(self, hasil):
        popup = tk.Toplevel(self.root)
        popup.title("Hasil Perhitungan")
        label_hasil = ttk.Label(popup, text=hasil)
        label_hasil.pack(pady=10)

    def hitung_jajar_genjang_keliling(self):
        sisi1 = self.sisi1_jajar_genjang_var.get()
        sisi2 = self.sisi2_jajar_genjang_var.get()
        sisi3 = self.sisi3_jajar_genjang_var.get()
        sisi4 = self.sisi4_jajar_genjang_var.get()
        keliling = sisi1 + sisi2 + sisi3 + sisi4
        self.tampilkan_hasil_jajar_genjang("Keliling Jajar Genjang: {:.2f}".format(keliling))

    def hitung_jajar_genjang_luas(self):
        alas = self.alas_jajar_genjang_var.get()
        tinggi = self.tinggi_jajar_genjang_var.get()
        luas = alas * tinggi
        self.tampilkan_hasil_jajar_genjang("Luas Jajar Genjang: {:.2f}".format(luas))
        
    def tampilkan_hasil_jajar_genjang(self, hasil):
        popup = tk.Toplevel(self.root)
        popup.title("Hasil Perhitungan")
        label_hasil = ttk.Label(popup, text=hasil)
        label_hasil.pack(pady=10)
        
    def hitung_segitiga_keliling(self):
        sisi1 = self.sisi1_segitiga_var.get()
        sisi2 = self.sisi2_segitiga_var.get()
        sisi3 = self.sisi3_segitiga_var.get()
        keliling = sisi1 + sisi2 + sisi3
        self.tampilkan_hasil_segitiga("Keliling Segitiga: {:.2f}".format(keliling))

    def hitung_segitiga_luas(self):
        alas = self.alas_segitiga_var.get()
        tinggi = self.tinggi_segitiga_var.get()
        luas = 0.5 * alas * tinggi
        self.tampilkan_hasil_segitiga("Luas Segitiga: {:.2f}".format(luas))
        
    def tampilkan_hasil_segitiga(self, hasil):
        popup = tk.Toplevel(self.root)
        popup.title("Hasil Perhitungan")
        label_hasil = ttk.Label(popup, text=hasil)
        label_hasil.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = BangunDatarCalculator(root)
    root.mainloop()
