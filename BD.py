import mysql.connector
class BD:
    conexion = mysql.connector.connect(host="localhost", user="root", passwd="Azteca.12345")
    cursor = conexion.cursor()
    def createDB(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS CriptoG")
    
    def useDB(self):
        self.cursor.execute("USE CriptoG")
             
    def createTables(self):
        self.cursor.execute("create table if not exists Algorithm (codAlg integer auto_increment primary key, nameAlg varchar(30))")
        self.cursor.execute("create table if not exists number(codNum integer auto_increment primary key, Numero bigint, Factores varchar(100), tiempo float, codAlg integer not null, foreign key(codAlg) references Algorithm (codAlg))")
    
    def insert(self, datos):
        self.cursor.execute("INSERT INTO number(Numero, Factores, tiempo, codAlg) values(%s, %s, %s, %s)", datos)
        self.conexion.commit()