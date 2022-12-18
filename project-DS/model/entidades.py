from tkinter import messagebox
from .conexion_bd import conectarBD

class Afiliados:
    def __init__(
        self, nombres, apellidos, genero, dir, email, f_nac, 
        est_civ, tip_afil, telf, ciudad, ips, ordenes):
        
        self.id = None
        self.nombres = nombres
        self.apellidos = apellidos
        self.genero = genero
        self.direccion = dir
        self.email = email
        self.fecha_nacimiento = f_nac
        self.estado_civil = est_civ
        self.tipo_afil = tip_afil
        self.telefono = telf
        self.ciudad = ciudad
        self.ips = ips
        self.ordenes = ordenes

class Beneficiarios(Afiliados):
    def __init__(
        self, nombres, apellidos, genero, dir, email, f_nac, est_civ, 
        tip_afil, telf, ciudad, ips, ordenes, parentesco, cotizante):
        super().__init__(
            nombres, apellidos, genero, dir, email, f_nac, est_civ, 
            tip_afil, telf, ciudad, ips, ordenes)
        self.parentesco = parentesco
        self.cotizante = cotizante

class Cotizantes(Afiliados):
    def __init__(
        self, nombres, apellidos, genero, dir, email, f_nac, est_civ, tip_afil,
        telf, ciudad, ips, ordenes, salario, estado_afil, f_afil, rango_sal):
        super().__init__(
            nombres, apellidos, genero, dir, email, f_nac, est_civ, tip_afil,
            telf, ciudad, ips, ordenes)
        self.salario = salario
        self.estadoafiliacion = estado_afil
        self.fechaprieraafiliacion = f_afil
        self.rangosalarial = rango_sal
        
class Dependientes(Cotizantes):
    def __init__(
        self, nombres, apellidos, genero, dir, email, f_nac, est_civ, tip_afil, telf, 
        ciudad, ips, ordenes, salario, estado_afil, f_afil, rango_sal, estado):
        super().__init__(
            nombres, apellidos, genero, dir, email, f_nac, est_civ, tip_afil, telf, 
            ciudad, ips, ordenes, salario, estado_afil, f_afil, rango_sal)
        self.estado = estado

class Independientes(Cotizantes):
    def __init__(
        self, nombres, apellidos, genero, dir, email, f_nac, est_civ, tip_afil, telf, ciudad, ips,
        ordenes, salario, estado_afil, f_afil, rango_sal, nom_empresa, rut, contrato):
        super().__init__(
            nombres, apellidos, genero, dir, email, f_nac, est_civ, tip_afil, telf, ciudad, ips,
            ordenes, salario, estado_afil, f_afil, rango_sal)
        self.nombre_empresa = nom_empresa
        self.rut = rut
        self.contrato = contrato

class Empresa:
    def __init__(self, nit, razonsocial,ciudad, direccion, telefono, nombrecontacto, contrato):
        self.nit = nit
        self.razonsocial = razonsocial
        self.ciudad = ciudad
        self.direccion = direccion
        self.telefono = telefono
        self.nombrecontacto = nombrecontacto
        self.contrato = contrato

class Ips:
    def __init__(self, nit, razonsocial, nivelatencion):
        self.nit = nit
        self.razonsocial = razonsocial
        self.nivelatencion = nivelatencion

class Servicios:
    def __init__(self, codigo, nombre,ips):
        self.codigo = codigo
        self.nombre = nombre
        self.ips = ips

class Reporte:
    def __init__(self, nroradicado, fecharecibo, codcotizante, nit_empresa):
        self.nroradicado = nroradicado
        self.fecharecibo = fecharecibo
        self.codcotizante = codcotizante
        self.nit_empresa = nit_empresa

class ReporteContrato(Reporte):
    def __init__(self, nroradicado, fecharecibo, codcotizante, nit_empresa, salario):
        super().__init__(nroradicado, fecharecibo, codcotizante, nit_empresa)
        self.salario = salario

class ReporteRetiro(Reporte):
    def __init__(self, nroradicado, fecharecibo, codcotizante, nit_empresa, fecharetiro):
        super().__init__(nroradicado, fecharecibo, codcotizante, nit_empresa)
        self.fecharetiro = fecharetiro

class Ordenes:
    def __init__(self, codigo, fechaorden, medico, diagnostico, descripcionserv, ips, afiliado):
        self.codigo = codigo
        self.fechaorden = fechaorden
        self.medico = medico
        self.diagnostico = diagnostico
        self.descripcionserv = descripcionserv
        self.ips = ips
        self.afiliado = afiliado

def consultar(id):
    conexion = conectarBD()
    
    listar_afiliado = []
    query = f"""SELECT * FROM afiliado WHERE id=\'{id}\'"""
    
    try:
        conexion.cursor.execute(query)
        listar_afiliado = conexion.cursor.fetchall()
        conexion.cerrar()
    except Exception as ex:
        messagebox.showerror('ERROR EN LA CONSULTA', f'{ex}.')

    return listar_afiliado

def conteo():
    conexion = conectarBD()
    
    tamaño_tabla = []
    quary = """SELECT count(*) FROM afiliado"""
    
    try:
        conexion.cursor.execute(quary)
        tamaño_tabla = conexion.cursor.fetchall()
        conexion.cerrar()
    except Exception as ex:
        messagebox.showerror('ERROR EN CONTEO', f'{ex}.')
    
    return tamaño_tabla[0][0]

def agregar_beneficiario(objeto):
    conexion = conectarBD()
    objeto = Beneficiarios()
    tam = conteo()
    
    quary = f"""INSERT INTO beneficiario
        VALUES(\'{tam + 10001}\' , \'{objeto.nombres}\', \'{objeto.apellidos}\', \'{objeto.genero}\',
        \'{objeto.direccion}\', \'{objeto.email}\', \'{objeto.fecha_nacimiento}\',
        \'{objeto.estado_civil}\', \'{objeto.tipo_afil}\', {objeto.telefono}, \'{objeto.ciudad}\',
        {objeto.ips}, \'{objeto.ordenes}\', \'{objeto.parentesco}\', \'\',
        );"""
    
    try:
        conexion.cursor.execute(quary)
        conexion.cerrar()
        print('ejecutó agregar_beneficiario()')
    except Exception as ex:
        messagebox.showerror('ERROR EN AGREGAR BENEFICIARIO', f'{ex}.')  

def editar(objeto, id_pelicula):
    conexion = conectarBD()
    
    sql = f"""UPDATE beneficiario
    SET nombre = \'{objeto.nombre}\', \'{objeto.apellido}\', \'{objeto.genero}\',
    \'{objeto.direccion}\', \'{objeto.email}\', \'{objeto.f_nac}\', \'{objeto.estado_civil}\',
    \'{objeto.tipo_afil}\', {objeto.telefono}, \'{objeto.ciudad}\', {objeto.ips}, NULL)
    WHERE id = \'{id_pelicula}\'"""
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except Exception as ex:
        messagebox.showerror('ERROR AL EDITAR', f'{ex}.')

def eliminar():
    pass
