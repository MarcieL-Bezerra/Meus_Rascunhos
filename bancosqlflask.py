from flask import Flask, jsonify
import pyodbc 
import json



def table():
    server = 'https://databases.000webhost.com/?_ga=2.134004046.111463503.1630546602-1619446131.1617115308'
    database = 'id12857619_bibliabd' 
    username = 'id12857619_marcielbiblia' 
    password = 'pw3>#@9$|dShqA2' 
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()

    cursor.execute("SELECT * FROM  books") 
    row = cursor.fetchone() 
    html = '<table border="1" style="width:50%"><tr><th>Nome</th><th>Sobrenome</th><th>Email</th></tr>'
    while row: 
        html += '<tr><td>'+row.nome+'</td><td>'+row.sobrenome+'</td><td>'+row.email+'</td></tr>'
        row = cursor.fetchone()
    html += '</table>'
    return html

if _name_ == '_main_':
    app.run(debug=True)

app = Flask(_name_)
#@app.route('/',methods=['GET'])