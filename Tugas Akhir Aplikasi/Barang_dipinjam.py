import mysql.connector
from db import DBConnection as mydb
class Barang_dipinjam:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='sql.freedb.tech',
            user='freedb_PutraRJ303',
            password='tc5PUE#@K@53?dy',
            database='freedb_PropertiHajat'
        )
        self.cursor = self.conn.cursor()

    def get_barang_dipinjam_data(self):
        sql = "SELECT nama_properti_id FROM properti"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result
    
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT nama_properti_id FROM properti"
        result = self.conn.findAll(sql)
        return result

