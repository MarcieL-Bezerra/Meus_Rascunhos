import sqlite3
from fotobd import Banco
import tkinter.filedialog as fdlg
import os


banco=Banco()
def convertToBinaryData():
  caminho= fdlg.askopenfilename()
  with open(caminho, 'rb') as file:
    blobData = file.read()
  return blobData

def insertBLOB(name, photo, resumeFile):
  try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite")
    sqlite_insert_blob_query = """ INSERT INTO new_employee
                        (nomes, fotos, resumos) VALUES (?, ?, ?)"""

    empPhoto = convertToBinaryData()
    resume = convertToBinaryData()
    # Convert data into tuple format
    data_tuple = (name, empPhoto, resume)
    cursor.execute(sqlite_insert_blob_query, data_tuple)

    sqliteConnection.commit()
    print("Imagem enviada com sucesso")
    cursor.close()

  except sqlite3.Error as error:
    print("Erro primeiro try", error)
  finally:
    if sqliteConnection:
      sqliteConnection.close()
      print("Fechado conexao")

insertBLOB("Marciel", "eu.jpg", "teste2.txt")
#insertBLOB("David", "eu.jpg", "teste2.txt")