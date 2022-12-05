from tkinter import *
from tkinter import messagebox
'''import psycopg2'''
import psycopg2

'''Crear una ventana de login con usuario y contraseña con Tkinter'''
def usuarioypass():
    print("Usuario: ", usuario.get())
    print("Contraseña: ", contraseña.get())

def validacion():
    if usuario.get() == "1" and contraseña.get() == "1":
        ventana.destroy()
        ventana2 = Tk()
        ventana2.title("Bienvenido")
        ventana2.geometry("400x300")
        frame2 = Frame(ventana2)
        frame2.pack()
        label = Label(frame2, text="Bienvenido administrador")
        label.grid(row=0, column=0, sticky="e", padx=10, pady=10)
        conexionBD()
        ventana2.mainloop()
        
        
    elif usuario.get() == "afiliado" and contraseña.get() == "1":
        ventana.destroy()
        ventana3 = Tk()
        ventana3.title("Bienvenido afiliado")
        ventana3.geometry("400x300")
        frame2 = Frame(ventana3)
        frame2.pack()
        label = Label(frame2, text="Bienvenido afiliado")
        label.grid(row=0, column=0, sticky="e", padx=10, pady=10)
        ventana3.mainloop()
    else:
        '''messagebox whit tkinter'''
        messagebox.showinfo("Error", "Usuario o contraseña incorrectos")
 
def conexionBD():
    try:
        conexion = psycopg2.connect(user='postgres',password='0000',database='bdesperarparasalvarse')
        print("Conexión exitosa")
        cursor = conexion.cursor()
        cursor.execute("select * from afiliado")
        afiliado = cursor.fetchall()
        for fila in afiliado:
            print(fila[0])
    except:
        print("Error de conexión")







# Crear la ventana
ventana = Tk()
ventana.title("Login")
ventana.geometry("400x300")
# Crear un frame
frame = Frame(ventana)
frame.pack()
# Crear un label
labeluser = Label(frame, text="Usuario")
labeluser.grid(row=0, column=0, sticky="e", padx=10, pady=10)
# Crear un entry
usuario = Entry(frame)
usuario.grid(row=0, column=1, padx=10, pady=10)
# Crear un label
labelpass = Label(frame, text="Contraseña")
labelpass.grid(row=1, column=0, sticky="e", padx=10, pady=10)
# Crear un entry
contraseña = Entry(frame, show="*")
contraseña.grid(row=1, column=1, padx=10, pady=10)
# Crear un botón
boton = Button(frame, text="Iniciar sesión",command=validacion)
boton.grid(row=2, column=1, sticky="e", padx=10, pady=10)
# Mostrar la ventana
ventana.mainloop()

'''hacer select from postgresql y retornar en string'''


