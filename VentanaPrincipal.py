from tkinter import *
import sqlite3

class miVentana():
    def __init__(self):
        
        self.root = Tk()
        ventana = self.root
        ventana.title("Cuentas")
        
        Frame_cabecera = Frame(ventana)
        Frame_cabecera.grid(row=0,column=0)
        
                
        self.button_cuenta = Button(Frame_cabecera,text="Cuenta  ",height = 11,width = 20,bg="#00BBFF",command = self.subVentana_cuenta)
        self.button_cuenta.grid(row = 0, column = 0 ,  rowspan=2,columnspan = 2)
        
        button_ingresos = Button(Frame_cabecera,text="Ingresos",height = 5,width = 20,bg="#4CB24E")
        button_ingresos.grid(row = 0, column = 2,columnspan = 2)
        
        button_gastos = Button(Frame_cabecera,text="Gastos  ",height = 5,width=20,bg="#ED0C27")
        button_gastos.grid(row = 1, column = 2, columnspan = 2)
        
        button_presupuesto = Button(Frame_cabecera,text="Presupuesto",height = 4, width=43,bg="#EDA90C")
        button_presupuesto.grid(row = 2, column = 0, columnspan = 4)
        
        button_factura = Button(Frame_cabecera,text="Factura",height = 5,width=20,bg="#ED0C8C")
        button_factura.grid(row = 3, column = 0, columnspan = 2)
        
        button_informe = Button(Frame_cabecera,text="Informes",height = 5,width=20,bg="#80FFE6")
        button_informe.grid(row = 3, column = 2, columnspan = 2)
        
        button_mas= Button(Frame_cabecera,text="ADD",height = 5,width=8,bg="#198F39")
        button_mas.grid(row = 4, column = 0 )
        
        button_LES= Button(Frame_cabecera,text="LES",height = 5,width=8,bg="#A70122")
        button_LES.grid(row = 4, column = 1)
        
        button_cambia= Button(Frame_cabecera,text="<-->",height = 5,width=8,bg="#66EAFF")
        button_cambia.grid(row = 4, column = 2)
        
        button_fact_rec= Button(Frame_cabecera,text="Fac y rec",height = 5,width=8,bg="#FF66E1")
        button_fact_rec.grid(row = 4, column = 3)
        
        button_factura = Button(Frame_cabecera,text="Estadisticas",height = 5,width=20,bg="#473E40")
        button_factura.grid(row = 5, column = 0, columnspan = 2)
        
        button_informe = Button(Frame_cabecera,text="Mas",height = 5,width=20,bg="#CBEEF6")
        button_informe.grid(row = 5, column = 2, columnspan = 2)
        self.leer_bd()
        self.root.mainloop()
        
    def agregar_cuenta(self,cuenta,saldo):
        datos = cuenta,saldo
        miConexion = sqlite3.connect("cuentas")
        micursor = miConexion.cursor()
        micursor.execute("INSERT INTO CUENTAS VALUES(NULL,?,?)",(datos))
        miConexion.commit()
        self.leer_bd()
        print(cuenta,saldo)
        miConexion.close()
        self.actualizar()
        
    def actualizar(self):
        self.texto_cuenta.delete(1.0, END)
        miConexion = sqlite3.connect("cuentas")
        micursor = miConexion.cursor()
        micursor.execute("SELECT * FROM CUENTAS " )
        datos=micursor.fetchall()
        #texto_cuenta.delete(0, "END")
        for dato in datos:            
            self.texto_cuenta.insert(INSERT, str(dato[0])+" Nombre: " +dato[1]+" Saldo: "+str(dato[2])+" "+"\n")
        miConexion.close()
        
    def subVentana_cuenta(self):
        ventana_Cuenta = Toplevel()       
        ventana_Cuenta.resizable(width=FALSE, height=FALSE)
        
        label_cuenta = Label(ventana_Cuenta,text="Nombre de la cuenta")
        label_cuenta.grid(row = 0, column = 0)
        
        label_saldo = Label(ventana_Cuenta,text="Saldo de la cuenta")
        label_saldo.grid(row = 1, column = 0)
        
        cuenta = StringVar()
        entry_cuenta = Entry(ventana_Cuenta,textvariable = cuenta)
        entry_cuenta.grid(row = 0 , column = 1)
        
        saldo = StringVar()
        entry_saldo = Entry(ventana_Cuenta,textvariable = saldo)
        entry_saldo.grid(row = 1 , column = 1)
        
        button_agregar = Button(ventana_Cuenta,text="Agregar",command = lambda :self.agregar_cuenta(cuenta.get(),saldo.get()))
        button_agregar.grid(row = 3, column=1,)
        
        button_actualizar = Button(ventana_Cuenta,text="Actualizar", command = self.actualizar)
        button_actualizar.grid(row = 3, column=0,)
        
        self.texto_cuenta = Text(ventana_Cuenta,width=60)
        self.texto_cuenta.grid(row = 4 , column=0, columnspan = 2)
        
        self.actualizar()
        ventana_Cuenta.mainloop()
        
         
    def leer_bd(self):
        miConexion = sqlite3.connect("cuentas")
        micursor = miConexion.cursor()
        micursor.execute("SELECT * FROM CUENTAS " )
        datos=micursor.fetchall()
        aux=0
        print("entrando")
        for dato in datos:
            aux = aux + dato[2]
            print(aux)
        self.button_cuenta.config(text=aux)
        miConexion.close()
        