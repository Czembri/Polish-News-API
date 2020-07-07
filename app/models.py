import mysql.connector as mc
import configparser


class DB:
    Config = configparser.ConfigParser()
    Config.read("app\config.ini")
    mydb = mc.connect (
        host = Config.get('database', 'host'),
        user=Config.get('database', 'user'),
        password=Config.get('database', 'password'),
        database=Config.get('database', 'database')
    )

    mycursor = mydb.cursor()

    def __init__(self, tablename):
        self.tablename = tablename

    def selectAll(self):
        self.mycursor.execute(f"select * from {self.tablename}")

        myresult = self.mycursor.fetchall()
        return myresult

    def selectByID(self, id):
        self.mycursor.execute(f"select * from {self.tablename} where {self.tablename}_id = {id}")
        myresult = self.mycursor.fetchall() 
        return myresult

    def selectBySRC(self):
        self.mycursor.execute(f"select * from {self.tablename}")
        myresult = self.mycursor.fetchall() 
        return myresult

    def selectSRC(self):
        self.mycursor.execute("select * from source")
        myresult = self.mycursor.fetchall() 
        return myresult