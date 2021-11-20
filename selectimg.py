import sqlite3

def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Restaurado e salvo em: ", filename, "\n")

def readBlobData(empId):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Conectado ao SQLite")

        sql_fetch_blob_query = """SELECT * from new_employee where id = ?"""
        cursor.execute(sql_fetch_blob_query, (empId,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[3], "Name = ", row[0])
            name = row[0]
            photo = row[1]
            resumeFile = row[2]

            print("Sanvando no disco \n")
            photoPath = "./arq_fotos\\" + name + ".jpg"
            #resumePath = "./arq_fotos\\" + name + "_resume.txt"
            writeTofile(photo, photoPath)
            #writeTofile(resumeFile, resumePath)

        cursor.close()

    except sqlite3.Error as error:
        print("Aconteceu o erro: ", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("Fechada a conecxao ")

readBlobData(9)
#readBlobData(8)