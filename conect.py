import mysql.connector
#class Conecction():
#    def __init__(self) -> None:
#        super().__init__()
def get_conection():
    try:
        connection=mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            db='camaronera')
        if connection.is_connected():
            print("Conexión exitosa")
        return connection
    except Exception as ex:
        print(ex)

print(get_conection())