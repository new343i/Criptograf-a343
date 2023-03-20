import mysql.connector
connect=mysql.connector.connect( host='localhost', user= 'root', passwd='Azteca.12345', db='PI')
cur=connect.cursor()

def crearT():
    cur.execute("CREATE TABLE IF NOT EXISTS countM(Matricula integer, Cantidad Integer)")
    connect.commit()

def insertar(insert):
    cur.execute("SELECT Matricula FROM countM where Matricula='%s'" % insert)
    consul=str(cur.fetchall())
    if str(insert) == str(consul[2:-3]):
        print("Sesion iniciada ", insert, ". Actualizada la cantidad de inicios.\n")
        cur.execute("SELECT Cantidad FROM countM where Matricula='%s'" % insert)
        consulV=str(cur.fetchall())
        cV=consulV[2:-3]
        valF=int(cV)+1
        cur.execute("UPDATE countM SET Cantidad='%s' WHERE Matricula='%s'" % (valF, insert))
        connect.commit()
    else:
        print("Nuevo usuario registrado, bienvenido", insert, "\n")
        cur.execute("INSERT INTO countM(Matricula, Cantidad) values('%s', '%s')" % (insert, 1))
        connect.commit()

def select():
    cur.execute("SELECT * FROM countM")
    consul=str(cur.fetchall())
    print(consul, "\n")
    
def main():
    crearT()
    while True:
        op=int(input("Elige una opcion: \n1.- Iniciar Sesion \n2.-Consultar usuarios disponibles \nSalir\nTu respuesta: "))
        if op == 1:
            insert=int(input("Introduce tu matrícula: "))
            insertar(insert)
        elif op == 2:
            select()
        elif op != 1 and op != 2:
            connect.close()        
            break

if __name__ == '__main__':
    main()