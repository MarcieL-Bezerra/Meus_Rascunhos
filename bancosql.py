import pymysql.cursors


def testabanco():
    servidor = "https://databases.000webhost.com/?_ga=2.111868420.1257536366.1632872888-1619446131.1617115308"
    bancodedados = "id12857619_bibliabd"
    usuario = "id12857619_marcielbiblia"
    senha = "pw3>#@9$|dShqA2"
    #conexion = pymysql.connect(database=bancodedados, user=usuario, password=senha, host=servidor)
    #conexion =  pymysql.connect(host=servidor, user=usuario, passwd=senha, db=bancodedados)
    conexion = pymysql.connect(host=servidor,
                             user=usuario,
                             password=senha,
                             database=bancodedados,
                             cursorclass=pymysql.cursors.DictCursor)
    #myCursor = conexion.cursor()
    #myCursor.execute("SELECT * FROM  books") 

testabanco()