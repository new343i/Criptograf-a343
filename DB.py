import sqlite3
conex = sqlite3.connect('crypto.db')
from tkinter import messagebox
cursor =conex.cursor()
class DataB:
    def __init__(self, n, facts, alg, time):
        self.n = n
        self.facts = facts
        self.alg = alg
        self.time = time
        
    def tables(self):
        try:
            cursor.execute('create table if not exists results(numero integer, factores text, algoritmo text, tiempo text)')
            conex.commit()
        except sqlite3.Error as error:
            print('SQLite dice: ', error)

    def select(self):
        try:
            cursor.execute('select count(*) from results where numero = ? and algoritmo = ?', [self.n, self.alg])
        except sqlite3.Error as error:
            print('SQLite dice: ', error)
        finally:
            resultados = cursor.fetchone()
            for fila in resultados:
                return fila

    def selectAll(self):
        try:
            cursor.execute('select * from results')
        except sqlite3.Error as error:
            messagebox.showerror(message='SQLite dice: {}'.format(error), title="SQL Error :c")
        finally:
            resultados = cursor.fetchall()
            return resultados
    
    def insert(self):
        facts = ' '.join(map(str, self.facts))
        try:
            if self.select() == 0:
                cursor.execute('insert into results(numero, factores, algoritmo, tiempo) values(?, ?, ?, ?)', [self.n, facts, self.alg, str(self.time)])
                conex.commit()
            else:
                cursor.execute('update results set factores = ?, tiempo = ? where numero = ? and algoritmo = ?', [facts, str(self.time), self.n, self.alg])
                conex.commit()
        except sqlite3.Error as error:
            messagebox.showerror(message='SQLite dice: {}'.format(error), title="SQL Error :c")        
        finally:
            messagebox.showinfo(message="Datos insertados", title="Exito!!")

    def delete(self, rowid):
        try:
            cursor.execute('delete from results where rowid = ?', (rowid,))
            conex.commit()
        except sqlite3.Error as error:
            messagebox.showerror(message='SQLite dice: {}'.format(error), title="SQL Error :c")
        finally:
            messagebox.showinfo(message="Dato eliminado", title="Exito!!")
