import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='',
  database='bibliadb'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM  books")

myresult = mycursor.fetchone()

print(myresult)