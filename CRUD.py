#Importaciones necesarias
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

#Desarro de la interfaz grafica
root=Tk() #Instancia principal
root.title("Aplicacion CRUD con Base de datos")
root.geometry("600x400") #Size de la ventana

#Variables de la ventana
Id=StringVar()
Nombre=StringVar()
Cargo=StringVar()
Salario=StringVar()

# Funciones para la creacion de la base de Datos
def conexionBD():
    conexion = sqlite3.connect("base") #Nombre de la base de datos
    cursor= conexion.cursor() #Creacion del cursor
    
    try:
        #Creacion de la tabla con comandos SQL
        cursor.execute('''
            CREATE TABLE empleado(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(50) NOT NULL,
                CARGO VARCHAR(50) NOT NULL,
                SALARIO INT NOT NULL)
                ''')
        messagebox.showinfo("Conexion","Tabla creada exitosamente")
    except:
        messagebox.showinfo("Conexion", "Conexion exitosa con la base de datos")

#Funcion para eliminar la base de datos
def eliminarBD():
    conexion = sqlite3.connect("base") #Nombre de la base de datos
    cursor= conexion.cursor() #Creacion del cursor
    if messagebox.askyesno(message="Los datos se perderan permanentement, Desea continuar?",title="ADVERTENCIA"):
        cursor.execute("DROP TABLE empleado")
    else:
        pass

def salirApp():
    valor=messagebox.askquestion("Salir,Desea salir?")
    if valor=="yes":
        #Cerrar ventana con destroy
        root.destroy()

