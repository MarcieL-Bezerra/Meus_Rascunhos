import sqlite3

class Banco():

    def __init__(self):
        self.conexao = sqlite3.connect('SQLite_Python.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists morador (id INTEGER PRIMARY KEY, 
        	name TEXT NOT NULL, 
        	photo BLOB NOT NULL, 
        	resume BLOB NOT NULL)""")
        self.conexao.commit()
        c.close()
banco()
'''
def createTable(self):
	self.conexao = sqlite3.connect('SQLite_Python.db')
    c = self.conexao.cursor()
    c.execute("""CREATE TABLE new_employee ( id INTEGER PRIMARY KEY, name TEXT NOT NULL, photo BLOB NOT NULL, resume BLOB NOT NULL)""")
    self.conexao.commit()
    c.close()


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB(empId, name, photo, resumeFile):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        #c = banco.conexao.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO new_employee
                                  (id, name, photo, resume) VALUES (?, ?, ?, ?)"""

        empPhoto = convertToBinaryData(photo)
        resume = convertToBinaryData(resumeFile)
        # Convert data into tuple format
        data_tuple = (empId, name, empPhoto, resume)
        c.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        c.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")

insertBLOB(1, "Smith", "foto1.png", "teste1.txt")
#insertBLOB(2, "David", "eu.jpg", "teste2.txt")
'''