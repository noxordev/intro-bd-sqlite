import sqlite3

class Conexion:
    def __init__(self, query_sql,parametro=[]):
        self.con = sqlite3.connect('inicio_bd.db')
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()
        self.res = self.cur.execute(query_sql,parametro)

def formato(respuesta):
    lista = []
    for row in respuesta:
        lista.append(dict(row))
    print(lista)

######## Select All ########
#conexion a la base de datos
conexionSelect = Conexion('SELECT * FROM persona;')
#conexionSelect.con.close() #ayuda a cerrar la conexion a la base de datos ya que es persistente

#Ejecutar la sentencia sql
respuesta = conexionSelect.res
formato(respuesta)

#Conexion con where
conexionWhere = Conexion('SELECT * FROM Persona WHERE name LIKE "vi%";')
respuesta2 = conexionWhere.res
formato(respuesta2)

#usando sqlite3.row_factory = sqlite3.Row
#cursor.execute("SELECT * FROM persona")
#persona = cursor.fetchall()
#print(persona)
#for row in persona:
#     dic = dict(row)
#     print(dic['name'], dic['lastname'], dic['dni'])  # Muestra los datos de la tabla

#answer= [dict(row) for row in cursor.execute("SELECT * FROM persona")]
#print(answer)
# for row in answer:
#     print(row['name'], row['lastname'], row['dni'])  # Muestra los datos de la tabla

######## Insert ########

conexionInsert = Conexion(
    'INSERT INTO Persona (name, lastname, dni, email) VALUES (?, ?, ?, ?);',
    ('Juan', 'Perez', '12345r789', 'juan@grail.com')
)
conexionInsert.con.commit()
print(conexionInsert.cur.lastrowid)