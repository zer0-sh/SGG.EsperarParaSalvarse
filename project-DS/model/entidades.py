from tkinter import messagebox
from .conexion_bd import conectarBD

class Afiliados:
    def __init__(
        self, nombre, apellido, genero, dir, email, f_nac, 
        est_civ, tip_afil, telf, ciudad, ips):
        
        self.id_afiliado = None
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        self.direccion = dir
        self.email = email
        self.f_nac = f_nac
        self.estado_civil = est_civ
        self.tipo_afil = tip_afil
        self.telefono = telf
        self.ciudad = ciudad
        self.ips = ips
    
class Beneficiarios(Afiliados):
    def __init__(
        self, nombre, apellido, genero, dir, email, f_nac, est_civ,
        tip_afil, telf, ciudad, parentesco, ips):
        super().__init__(
            nombre, apellido, genero, dir, email, f_nac,est_civ, 
            tip_afil, telf, ciudad, ips)
        self.parentesco = parentesco

class Cotizantes(Afiliados):
    def __init__(
        self, nombre, apellido, genero, dir, email, f_nac, est_civ, tip_afil,
        telf, ciudad, salario, estado_afil, f_afil, rango_sal, ips):
        super().__init__(
            nombre, apellido, genero, dir, email, f_nac, est_civ,
            tip_afil, telf, ciudad, ips)
        self.salario = salario
        self.estado_afiliacion = estado_afil
        self.fecha_afiliacion = f_afil
        self.rango_salarial = rango_sal

class Dependientes(Cotizantes):
    def __init__(
        self, nombre, apellido, genero, dir, email, f_nac, est_civ, tip_afil,telf,
        ciudad, ips, salario, estado_afil, f_afil, rango_sal, estado):
        super().__init__(
            nombre, apellido, genero, dir, email, f_nac, est_civ, tip_afil, telf,
            ciudad, ips, salario, estado_afil, f_afil, rango_sal)
        self.estado = estado

class Independientes(Cotizantes):
    def __init__(
        self, nombre, apellido, genero, dir, email, f_nac, est_civ, tip_afil, telf,
        ciudad, ips, salario, estado_afil, f_afil, rango_sal, nom_empresa, rut, contrato):
        super().__init__(
            nombre, apellido, genero, dir, email, f_nac, est_civ, tip_afil, telf,
            ciudad, ips, salario, estado_afil, f_afil, rango_sal)
        self.nombre_empresa = nom_empresa
        self.rut = rut
        self.contrato = contrato

def consultar(id):
    conexion = conectarBD()
    
    listar_afiliado = []
    query = f"""SELECT * FROM afiliado WHERE id=\'{id}\'"""
    
    try:
        conexion.cursor.execute(query)
        listar_afiliado = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        messagebox.showerror(
            'ERROR EN LA CONSULTA',
            'Debe ingresar la llave.\nO tal vez no existe.')

    return listar_afiliado

def agregar(objeto):
    conexion = conectarBD()
    
    tamaño_tabla = """SELECT count(*) FROM afiliado"""
    
    try:
        pass
    except Exception as ex:
        pass
    
    quary = f"""INSERT INTO afiliado
        VALUES(\'\' , \'{objeto.nombre}\', \'{objeto.apellido}\', \'{objeto.genero}\',
        \'{objeto.direccion}\', \'{objeto.email}\', \'{objeto.f_nac}\', \'{objeto.estado_civil}\',
        \'{objeto.tipo_afil}\', {objeto.telefono}, \'{objeto.ciudad}\', {objeto.ips}, NULL);"""
    """
    try:
        conexion.cursor.execute(quary)
        conexion.cerrar()
        print('ejecutó agregar()')
    except Exception as ex:
        titulo = 'ERROR EN AGREGAR'
        mensaje = f'{ex}.'
        messagebox.showerror(titulo, mensaje)
    """

def editar(objeto, id_pelicula):
    conexion = conectarBD()
    
    sql = f"""UPDATE peliculas
    SET nombre = \'{objeto.nombre}\', \'{objeto.apellido}\', \'{objeto.genero}\',
    \'{objeto.direccion}\', \'{objeto.email}\', \'{objeto.f_nac}\', \'{objeto.estado_civil}\',
    \'{objeto.tipo_afil}\', {objeto.telefono}, \'{objeto.ciudad}\', {objeto.ips}, NULL)
    WHERE id = \'{id_pelicula}\'"""
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except Exception as ex:
        titulo = 'ERROR AL EDITAR'
        mensaje = f'{ex}.'
        messagebox.showerror(titulo,mensaje)

def eliminar():
    pass
