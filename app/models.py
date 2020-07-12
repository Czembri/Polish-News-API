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
        columns = [desc[0] for desc in self.mycursor.description]
        result = []
        
        rows = self.mycursor.fetchall()

        for row in rows:
            row = dict(zip(columns, row))
            result.append(row)
        return result

    def selectByID(self, id):
        self.mycursor.execute(f"select * from {self.tablename} where {self.tablename}_id = {id}")
        columns = [desc[0] for desc in self.mycursor.description]
        result = []
        
        rows = self.mycursor.fetchall()

        for row in rows:
            row = dict(zip(columns, row))
            result.append(row)
        return result


    def selectBySRC(self):
        self.mycursor.execute(f"select * from {self.tablename}")
        columns = [desc[0] for desc in self.mycursor.description]
        result = []
        
        rows = self.mycursor.fetchall()

        for row in rows:
            row = dict(zip(columns, row))
            result.append(row)
        return result

    def selectSRC(self):
        self.mycursor.execute("select * from source")
        columns = [desc[0] for desc in self.mycursor.description]
        result = []
        
        rows = self.mycursor.fetchall()

        for row in rows:
            row = dict(zip(columns, row))
            result.append(row)
        return result

    def selectByDate(self, date):
        self.mycursor.execute(f"select * from {self.tablename} where scraped='{date}'")
        columns = [desc[0] for desc in self.mycursor.description]
        result = []
        
        rows = self.mycursor.fetchall()

        for row in rows:
            row = dict(zip(columns, row))
            result.append(row)
        return result