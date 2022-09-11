import mysql.connector
class ScraperBdd:
    def __init__(self, cnx):
        self.cnx = cnx
        self.cursor = self.cnx.cursor()


    def SelectDb(self, search):
        self.cursor.execute("SELECT id FROM search WHERE search = '" + search + "'")
        return self.cursor.fetchone()

    def InsertDb(self, search):
        self.cursor.execute("INSERT INTO search(search) VALUES('" + search + "')")
        self.cnx.commit()
        return self.SelectDb(search)