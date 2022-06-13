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

print(get_conection)

#cur = connection.cursor()
#sql="INSERT INTO proveedor (ruc, nombre, direccion) VALUES(%s,%s,%s)"
#data= ('0978578478','Agripac S.A','Sur') 
#cur.execute(sql,data)
#connection.commit()
#cur.close()
#connection.close()
#for fila in datos:
#    print(fila)
#print(cur)