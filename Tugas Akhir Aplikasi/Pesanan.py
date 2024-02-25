	# filename : Pesanan.py
from db import DBConnection as mydb
class Pesanan:
    def __init__(self):
        self.__id=None
        self.__nama_peminjam=None
        self.__nik_ktp=None
        self.__alamat=None
        self.__nomor_telepon=None
        self.__tanggal=None
        self.__tanggal_meminjam=None
        self.__tanggal_kembali=None
        self.__barang_dipinjam_id=None
        self.__tarif_perhari_id=None
        self.__total_bayar=None
        self.__status_bayar=None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def id(self):
        return self.__id
    @property
    def nama_peminjam(self):
        return self.__nama_peminjam
        
    @nama_peminjam.setter
    def nama_peminjam(self, value):
        self.__nama_peminjam = value
    @property
    def nik_ktp(self):
        return self.__nik_ktp
        
    @nik_ktp.setter
    def nik_ktp(self, value):
        self.__nik_ktp = value
    @property
    def alamat(self):
        return self.__alamat
        
    @alamat.setter
    def alamat(self, value):
        self.__alamat = value
    @property
    def nomor_telepon(self):
        return self.__nomor_telepon
        
    @nomor_telepon.setter
    def nomor_telepon(self, value):
        self.__nomor_telepon = value
    @property
    def tanggal(self):
        return self.__tanggal
        
    @tanggal.setter
    def tanggal(self, value):
        self.__tanggal = value
    @property
    def tanggal_meminjam(self):
        return self.__tanggal_meminjam
        
    @tanggal_meminjam.setter
    def tanggal_meminjam(self, value):
        self.__tanggal_meminjam = value
    @property
    def tanggal_kembali(self):
        return self.__tanggal_kembali
        
    @tanggal_kembali.setter
    def tanggal_kembali(self, value):
        self.__tanggal_kembali = value
    @property
    def barang_dipinjam_id(self):
        return self.__barang_dipinjam_id
        
    @barang_dipinjam_id.setter
    def barang_dipinjam_id(self, value):
        self.__barang_dipinjam_id = value
    @property
    def tarif_perhari_id(self):
        return self.__tarif_perhari_id
        
    @tarif_perhari_id.setter
    def tarif_perhari_id(self, value):
        self.__tarif_perhari_id = value
    @property
    def total_bayar(self):
        return self.__total_bayar
        
    @total_bayar.setter
    def total_bayar(self, value):
        self.__total_bayar = value
    @property
    def status_bayar(self):
        return self.__status_bayar
        
    @status_bayar.setter
    def status_bayar(self, value):
        self.__status_bayar = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__nama_peminjam,self.__nik_ktp,self.__alamat,self.__nomor_telepon,self.__tanggal,self.__tanggal_meminjam,self.__tanggal_kembali,self.__barang_dipinjam_id,self.__tarif_perhari_id,self.__total_bayar,self.__status_bayar)
        sql="INSERT INTO pesanan (nama_peminjam,nik_ktp,alamat,nomor_telepon,tanggal,tanggal_meminjam,tanggal_kembali,barang_dipinjam_id,tarif_perhari_id,total_bayar,status_bayar) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__nama_peminjam,self.__nik_ktp,self.__alamat,self.__nomor_telepon,self.__tanggal,self.__tanggal_meminjam,self.__tanggal_kembali,self.__barang_dipinjam_id,self.__tarif_perhari_id,self.__total_bayar,self.__status_bayar, id)
        sql="UPDATE pesanan SET nama_peminjam = %s,nik_ktp = %s,alamat = %s,nomor_telepon = %s,tanggal = %s,tanggal_meminjam = %s,tanggal_kembali = %s,barang_dipinjam_id = %s,tarif_perhari_id = %s,total_bayar = %s,status_bayar = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByNIK_KTP(self, nik_ktp):
        self.conn = mydb()
        val = (self.__nama_peminjam,self.__alamat,self.__nomor_telepon,self.__tanggal,self.__tanggal_meminjam,self.__tanggal_kembali,self.__barang_dipinjam_id,self.__tarif_perhari_id,self.__total_bayar,self.__status_bayar, nik_ktp)
        sql="UPDATE pesanan SET nama_peminjam = %s,alamat = %s,nomor_telepon = %s,tanggal = %s,tanggal_meminjam = %s,tanggal_kembali = %s,barang_dipinjam_id = %s,tarif_perhari_id = %s,total_bayar = %s,status_bayar = %s WHERE nik_ktp=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM pesanan WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByNIK_KTP(self, nik_ktp):
        self.conn = mydb()
        sql="DELETE FROM pesanan WHERE nik_ktp='" + str(nik_ktp) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM pesanan WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__nama_peminjam = self.result[1]
        self.__nik_ktp = self.result[2]
        self.__alamat = self.result[3]
        self.__nomor_telepon = self.result[4]
        self.__tanggal = self.result[5]
        self.__tanggal_meminjam = self.result[6]
        self.__tanggal_kembali = self.result[7]
        self.__barang_dipinjam_id = self.result[8]
        self.__tarif_perhari_id = self.result[9]
        self.__total_bayar = self.result[10]
        self.__status_bayar = self.result[11]
        self.conn.disconnect
        return self.result
    def getByNIK_KTP(self, nik_ktp):
        a=str(nik_ktp)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM pesanan WHERE nik_ktp='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__nama_peminjam = self.result[1]
           self.__nik_ktp = self.result[2]
           self.__alamat = self.result[3]
           self.__nomor_telepon = self.result[4]
           self.__tanggal = self.result[5]
           self.__tanggal_meminjam = self.result[6]
           self.__tanggal_kembali = self.result[7]
           self.__barang_dipinjam_id = self.result[8]
           self.__tarif_perhari_id = self.result[9]
           self.__total_bayar = self.result[10]
           self.__status_bayar = self.result[11]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__nama_peminjam = ''
           self.__nik_ktp = ''
           self.__alamat = ''
           self.__nomor_telepon = ''
           self.__tanggal = ''
           self.__tanggal_meminjam = ''
           self.__tanggal_kembali = ''
           self.__barang_dipinjam_id = ''
           self.__tarif_perhari_id = ''
           self.__total_bayar = ''
           self.__status_bayar = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM pesanan"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,nik_ktp FROM pesanan"
        self.result = self.conn.findAll(sql)
        return self.result        
        