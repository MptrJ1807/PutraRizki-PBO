import mysql.connector
from db import DBConnection as mydb
class Tarif_perhari:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='sql.freedb.tech',
            user='freedb_PutraRJ303',
            password='tc5PUE#@K@53?dy',
            database='freedb_PropertiHajat'
        )
        self.cursor = self.conn.cursor()

    def get_tarif_perhari_data(self):
        sql = "SELECT tarif_id, FROM properti"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result
    
    def getById(self, tarif_id):
        sql = "SELECT tarif_id FROM properti WHERE tarif_id = %s"
        self.cursor.execute(sql, (tarif_id,))
        result = self.cursor.fetchone()
        return result[0] if result else None
    
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT tarif_id FROM properti"
        result = self.conn.findAll(sql)
        return result
    


