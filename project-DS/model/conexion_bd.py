import psycopg2
from tkinter import messagebox

class conectarBD:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                host = "localhost",
                user = "postgres",
                password = "andres2903",
                database = "postgres",
                port = "5432"  # El puerto puede ser opcional
                )
            self.cursor = self.connection.cursor()
            print('Conexion exitosa a BD!!')
        except Exception as ex:
            messagebox.showerror('FALLO AL CONECTAR DB', f'{ex}.')
    
    def cerrar(self):
        self.connection.commit()
        self.connection.close()
