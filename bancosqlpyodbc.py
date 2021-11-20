import pyodbc

server = 'https://databases.000webhost.com/?_ga=2.134004046.111463503.1630546602-1619446131.1617115308'
database = 'id12857619_bibliabd' 
username = 'id12857619_marcielbiblia' 
password = 'pw3>#@9$|dShqA2'    
driver= '{ODBC Driver 17 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM  books")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()