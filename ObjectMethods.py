from CFRACMethod import *
from FermatMethod import *
from PollardsMethod import *
from time import time
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox


    #Test de multiplos
def main():
    cript=tk.Tk()
    cript.title("EDO Solver")

    labO=tk.Label(cript, text="CriptoProject")
    labO.config(fg="white", bg="#440c29", font="Cambria 40")
    labO.grid(row=0, column=0, pady=10, columnspan=2)

    labR1=tk.Label(cript, text="¿Que quieres hacer?")
    labR1.config(fg="white", bg="#440c29", font="Cambria 14")
    labR1.grid(row=1, column=0, columnspan=2)

    insR1=ttk.Combobox(cript, width=50, values=["Test de Primalidad", "Factorizar Fermat", "Factorizar CFRAC", "Factorizar Pollards"], state="readonly")
    insR1.config(font="Cambria 10")
    insR1.grid(row=2, column=0, columnspan=2, pady=7)

    labX = tk.Label(cript, text="Introduce un numero: ")
    labX.config(fg="white", bg="#440c29", font="Cambria 14")
    labX.grid(row=3, column=0, columnspan=2)

    insX = tk.Entry(cript, width=53, relief="sunken")
    insX.config(font="Cambria 10")
    insX.grid(row=4, column=0, columnspan=2, pady=7)

    def mandar(ans, n):
        if ans == '' or n == '':
            messagebox.showinfo(message="Rellena todos los campos!!", title="Mensajes")
        else:
            if str(ans) == "Test de Primalidad":
                Fermat=FermatMethod(int(n))            
                if Fermat.deterPar() != True:
                    messagebox.showinfo(message="Introduce solo numeros impares!!", title="Mensajes")
                else:
                    title = tk.Label(cript, text="Resultado:", font="Cambria 12", justify=tk.RIGHT)
                    title.config(fg="white", bg="#440c29", font="Cambria 12")
                    title.grid(row=6, column=0)

                    tI=time()
                    if int(Fermat.Rabin(int(n))) == 1:
                        Prim = "Es Primo."
                    else:
                        Prim = "No es Primo."
                    tE=time()
                    tF=tE-tI

                    title = tk.Label(cript, text="Resultado:", font="Cambria 12", justify=tk.RIGHT)
                    title.config(fg="white", bg="#440c29", font="Cambria 12")
                    title.grid(row=6, column=0)

                    mostTP = tk.Text(cript, wrap=WORD)
                    mostTP.insert(tk.END, Prim)
                    mostTP.config(fg="white", bg="#440c29", font="Cambria 12", relief="sunken", border=5, width=20, height=5)
                    mostTP.grid(row=7, column=0, pady=10)

                    time1 = tk.Label(cript, text="Tiempo de procesamiento:", font="Cambria 12", justify=tk.RIGHT)
                    time1.config(fg="white", bg="#440c29", font="Cambria 12")
                    time1.grid(row=8, column=0)

                    mostTPTM = tk.Text(cript, wrap=WORD)
                    mostTPTM.insert(tk.END, tF)
                    mostTPTM.config(fg="white", bg="#440c29", font="Cambria 12", relief="sunken", border=5, width=20, height=5)
                    mostTPTM.grid(row=9, column=0, pady=10)

            if str(ans) == "Factorizar Fermat":
                Fermat = FermatMethod(n)
                if Fermat.deterPar() != True:
                    messagebox.showinfo(message="Introduce solo numeros impares!!", title="Mensajes")
                else:
                    title = tk.Label(cript, text="Resultado:", font="Cambria 12", justify=tk.RIGHT)
                    title.config(fg="white", bg="#440c29", font="Cambria 12")
                    title.grid(row=6, column=0)

                    tI1=time()
                    Fermat = FermatMethod(n)
                    Fermat.factFermat(n)
                    Fermat.sacaMOPM(Fermat.factFermat(int(n)))
                    num = Fermat.x
                    tE1=time()
                    tF1=tE1-tI1

                    most = tk.Text(cript, wrap=WORD)
                    most.insert(tk.END,num)
                    most.config(fg="white", bg="#440c29", font="Cambria 12", relief="sunken", border=5, width=20, height=5)
                    most.grid(row=7, column=0, pady=10)

                    time1 = tk.Label(cript, text="Tiempo de Procesamiento:", font="Cambria 12", justify=tk.RIGHT)
                    time1.config(fg="white", bg="#440c29", font="Cambria 12")
                    time1.grid(row=8, column=0)

                    most = tk.Text(cript, wrap=WORD)
                    most.insert(tk.END, tF1)
                    most.config(fg="white", bg="#440c29", font="Cambria 12", relief="sunken", border=5, width=20, height=5)
                    most.grid(row=9, column=0, pady=10)

            if str(ans) == "Factorizar Pollards":
                tI=time()            
                Poll=PollardsMethod()
                list=[]
                list2=[]
                list2.append(int(n))
                while Poll.oper(int(n)) > 0:
                    x=Poll.oper(int(n)) 
                    n=n/Poll.oper(int(n))
                    list2.append(int(n))                                
                    list.append(x)
                list.append(list2[-1])
                tE=time()
                tF=tE-tI

                title = tk.Label(cript, text="Resultado:", font="Cambria 12", justify=tk.RIGHT)
                title.config(fg="white", bg="#440c29", font="Cambria 12")
                title.grid(row=6, column=0)

                most = tk.Text(cript, wrap=WORD)
                most.insert(tk.END, list)
                most.config(fg="white", bg="#440c29", font="Cambria 12", relief="sunken", border=5, width=20, height=5)
                most.grid(row=7, column=0, pady=10)

                time1 = tk.Label(cript, text="Tiempo de Procesamiento:", font="Cambria 12", justify=tk.RIGHT)
                time1.config(fg="white", bg="#440c29", font="Cambria 12")
                time1.grid(row=8, column=0)

                most = tk.Text(cript, wrap=WORD)
                most.insert(tk.END, tF)
                most.config(fg="white", bg="#440c29", font="Cambria 12", relief="sunken", border=5, width=20, height=5)
                most.grid(row=9, column=0, pady=10)

    button_border = tk.Frame(cript, highlightbackground="white", highlightthickness=1, bd=0, bg="#440c29")
    manR = tk.Button(button_border, text="Calcular", command=lambda: mandar(insR1.get(), int(insX.get())))
    manR.grid(row=5, column=0)
    button_border.grid(row=13, column=0, columnspan=2, pady=15)
    manR.config(width=20, height=1, fg="white", bg="#440c29", font="Cambria 10", relief="groove")


    cript.config(background="#440c29", border=15)
    cript.geometry("457x650")
    cript.mainloop()


if __name__ == '__main__':
    main()
