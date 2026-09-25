from conexion import Conexion
import sqlite3

def formato(respuesta):
    lista = []
    for row in respuesta.fetchall():
        lista.append(dict(row))
    # print(lista)
    return lista

def select_all():
    conexionSelect = Conexion('SELECT * FROM persona;')
    respuesta = conexionSelect.res
    resp = formato(respuesta)
    conexionSelect.con.close()
    return resp

def select_by_id(id:int):
    conexionSelectbyid = Conexion(f'SELECT * FROM persona WHERE id ={id};')
    respuesta = conexionSelectbyid.res
    resp = formato(respuesta)
    conexionSelectbyid.con.close()
    return respuesta

def insert_data(data):
    try:
        conexionInsert = Conexion(
            'INSERT INTO Persona (name, lastname, dni, email) VALUES (?, ?, ?, ?);',
            (data)
        )
        conexionInsert.con.commit()
        return conexionInsert.cur.lastrowid
    except sqlite3.Error as e:
        print(f"Error al insertar datos: {e}")
        return None
    finally:
        conexionInsert.con.close()

def update_data(data):
    try:
        conexionUpdate = Conexion(
            'UPDATE Persona SET name = ?, lastname = ?, dni = ?, email = ? WHERE id = ?;',
            data
        )
        conexionUpdate.con.commit()
        return conexionUpdate.cur.rowcount
    except sqlite3.Error as e:
        print(f"Error al actualizar datos: {e}")
        return None
    finally:
        conexionUpdate.con.close()

def delete_data(id:int):
    try:
        conexionDelete = Conexion(
            'DELETE FROM Persona WHERE id = ?;',
            (id,)
        )
        conexionDelete.con.commit()
        return conexionDelete.cur.rowcount
    except sqlite3.Error as e:
        print(f"Error al eliminar datos: {e}")
        return None
    finally:
        conexionDelete.con.close()

