	# filename : Properti.py
from db import DBConnection as mydb
class Properti:
    def __init__(self):
        self.__id=None
        self.__kode_properti_id=None
        self.__nama_properti_id=None
        self.__tarif_id=None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def id(self):
        return self.__id
    @property
    def kode_properti_id(self):
        return self.__kode_properti_id
        
    @kode_properti_id.setter
    def kode_properti_id(self, value):
        self.__kode_properti_id = value
    @property
    def nama_properti_id(self):
        return self.__nama_properti_id
        
    @nama_properti_id.setter
    def nama_properti_id(self, value):
        self.__nama_properti_id = value
    @property
    def tarif_id(self):
        return self.__tarif_id
        
    @tarif_id.setter
    def tarif_id(self, value):
        self.__tarif_id = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_properti_id,self.__nama_properti_id,self.__tarif_id)
        sql="INSERT INTO Properti (kode_properti_id,nama_properti_id,tarif_id) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__kode_properti_id,self.__nama_properti_id,self.__tarif_id, id)
        sql="UPDATE properti SET kode_properti_id = %s,nama_properti_id = %s,tarif_id = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateBy(self, ):
        self.conn = mydb()
        val = (self.__kode_properti_id,self.__nama_properti_id,self.__tarif_id, )
        sql="UPDATE properti SET kode_properti_id = %s,nama_properti_id = %starif_id = %s WHERE =%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM properti WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteBy(self, ):
        self.conn = mydb()
        sql="DELETE FROM properti WHERE ='" + str() + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM properti WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__kode_properti_id = self.result[1]
        self.__nama_properti_id = self.result[2]
        self.__tarif_id = self.result[3]
        self.conn.disconnect
        return self.result
    def getBy(self, ):
        a=str()
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM properti WHERE ='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__kode_properti_id = self.result[1]
           self.__nama_properti_id = self.result[2]
           self.__tarif_id = self.result[3]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__kode_properti_id = ''
           self.__nama_properti_id = ''
           self.__tarif_id = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM properti"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,nama_properti_id FROM properti"
        self.result = self.conn.findAll(sql)
        return self.result