from db import DBConnection as mydb

class Rumahsakit:

    def __init__(self):
        self.__id=None
        self.__nip=None
        self.__nama=None
        self.__jenis_kelamin=None
        self.__spesialis=None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def id(self):
        return self.__id

    @property
    def nip(self):
        return self.__nip

    @nip.setter
    def nip(self, value):
        self.__nip = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def jenis_kelamin(self):
        return self.__jenis_kelamin

    @jenis_kelamin.setter
    def jenis_kelamin(self, value):
        self.__jenis_kelamin = value

    @property
    def spesialis(self):
        return self.__spesialis

    @spesialis.setter
    def spesialis(self, value):
        self.__spesialis = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__nip, self.__nama, self.__jenis_kelamin, self.__spesialis)
        sql="INSERT INTO dokter (nip, nama, jenis_kelamin, spesialis) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__nip, self.__nama, self.__jenis_kelamin, self.__spesialis, id)
        sql="UPDATE dokter SET nip = %s, nama = %s, jenis_kelamin=%s, spesialis=%s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByNIP(self, nim):
        self.conn = mydb()
        val = (self.__nama, self.__jk, self.__kode_prodi, nim)
        sql="UPDATE dokter SET nama = %s, jenis_kelamin=%s, spesialis=%s WHERE nip=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM dokter WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByNIP(self, nip):
        self.conn = mydb()
        sql="DELETE FROM dokter WHERE nip='" + str(nip) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM dokter WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__nip = self.result[1]
        self.__nama = self.result[2]
        self.__jenis_kelamin = self.result[3]
        self.__spesialis = self.result[4]
        self.conn.disconnect
        return self.result

    def getByNIP(self, nip):
        a=str(nip)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM dokter WHERE nip='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nip = self.result[1]
            self.__nama = self.result[2]
            self.__jenis_kelamin = self.result[3]
            self.__spesialis = self.result[4]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nip = ''
            self.__nama = ''
            self.__jenis_kelamin = ''
            self.__spesialis = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM dokter"
        self.result = self.conn.findAll(sql)
        return self.result

# tampil Data
A = Rumahsakit()
B = A.getAllData()
print(B)