import mysql.connector
from tkinter import messagebox

# Conectar a la base de datos MySQL
conex = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='criptograph'
)

cursor = conex.cursor()

class DataB:
    def __init__(self, n, facts, alg, time):
        self.n = n
        self.facts = facts
        self.alg = alg
        self.time = time

    def tables(self):
        try:
            cursor.execute('create table if not exists results(numero VARCHAR(255), factores TEXT, algoritmo VARCHAR(255), tiempo VARCHAR(255))')
            conex.commit()
        except mysql.connector.Error as error:
            print('MySQL dice: ', error)

    def select(self):
        try:
            cursor.execute('select count(*) from results where numero = %s and algoritmo = %s', (self.n, self.alg))
        except mysql.connector.Error as error:
            print('MySQL dice: ', error)
        finally:
            resultados = cursor.fetchone()
            for fila in resultados:
                return fila

    def selectAll(self):
        try:
            cursor.execute('select * from results')
        except mysql.connector.Error as error:
            messagebox.showerror(message='MySQL dice: {}'.format(error), title="MySQL Error :c")
        finally:
            resultados = cursor.fetchall()
            return resultados

    def insert(self):
        facts = ' '.join(map(str, self.facts))
        try:
            if self.select() == 0:
                cursor.execute('insert into results(numero, factores, algoritmo, tiempo) values(%s, %s, %s, %s)', (self.n, facts, self.alg, str(self.time)))
                conex.commit()
            else:
                cursor.execute('update results set factores = %s, tiempo = %s where numero = %s and algoritmo = %s', (facts, str(self.time), self.n, self.alg))
                conex.commit()
        except mysql.connector.Error as error:
            messagebox.showerror(message='MySQL dice: {}'.format(error), title="MySQL Error :c")
        finally:
            messagebox.showinfo(message="Datos insertados", title="Éxito!!")

    def delete(self, rowid):
        try:
            cursor.execute('delete from results where rowid = %s', (rowid,))
            conex.commit()
        except mysql.connector.Error as error:
            messagebox.showerror(message='MySQL dice: {}'.format(error), title="MySQL Error :c")
        finally:
            messagebox.showinfo(message="Dato eliminado", title="Éxito!!")
