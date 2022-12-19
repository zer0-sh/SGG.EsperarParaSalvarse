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
        self.estado_afiliacion = estado_afil
        self.fecha_afiliacion = f_afil
        self.rango_salarial = rango_sal
        
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
    def __init__(
        self, razonsocial,ciudad, direccion, telefono, nombrecontacto, contrato):
        self.nit = None
        
        self.razon_social = razonsocial
        self.ciudad = ciudad
        self.direccion = direccion
        self.telefono = telefono
        self.nombre_contacto = nombrecontacto
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

# CONSULT FUNTION
def consultar(id, tabla):
    conexion = conectarBD()
    
    listar_afiliado = []
    query = f"""SELECT * FROM {tabla} WHERE id=\'{id}\'"""
    
    try:
        conexion.cursor.execute(query)
        listar_afiliado = conexion.cursor.fetchall()
        conexion.cerrar()
    except Exception as ex:
        messagebox.showerror('ERROR EN LA CONSULTA', f'{ex}.')

    return listar_afiliado

def consultar_empresa(nit, tabla):
    conexion = conectarBD()
    
    lista_empresa = []
    query = f"""SELECT * FROM {tabla} WHERE nit={nit}"""
    
    try:
        conexion.cursor.execute(query)
        lista_empresa = conexion.cursor.fetchall()
        conexion.cerrar()
    except Exception as ex:
        messagebox.showerror('ERROR EN LA CONSULTA EMPRESA', f'{ex}.')

    return lista_empresa

# FUNTIONS
def max_tuplas(tabla, columna):
    conexion = conectarBD()
    
    tamaño_tabla = []
    quary = f"""SELECT max({columna}) FROM {tabla} """
    
    try:
        conexion.cursor.execute(quary)
        tamaño_tabla = conexion.cursor.fetchall()
        conexion.cerrar()
    except Exception as ex:
        messagebox.showerror('ERROR EN MAX', f'{ex}.')
    
    return tamaño_tabla[0][0]

def conteo(tabla):
    conexion = conectarBD()
    
    tamaño_tabla = []
    quary = f"""SELECT count(*) FROM {tabla} """
    
    try:
        conexion.cursor.execute(quary)
        tamaño_tabla = conexion.cursor.fetchall()
        conexion.cerrar()
    except Exception as ex:
        messagebox.showerror('ERROR EN CONTEO', f'{ex}.')
    
    return tamaño_tabla[0][0]

# ADD FUNTIONS
def agregar_beneficiario(objeto):
    conexion = conectarBD()
    #objeto = Beneficiarios()
    tam = int(max_tuplas('afiliado', 'id')) + 1
    
    quary = f"""INSERT INTO beneficiario
        VALUES(\'{tam}\', \'{objeto.nombres}\', \'{objeto.apellidos}\',
        \'{objeto.genero}\', \'{objeto.direccion}\', \'{objeto.email}\',
        \'{objeto.fecha_nacimiento}\', \'{objeto.estado_civil}\', 
        \'{objeto.tipo_afil}\', {objeto.telefono}, \'{objeto.ciudad}\',
        {objeto.ips}, {objeto.ordenes}, \'{objeto.parentesco}\'
        );"""
    
    try:
        conexion.cursor.execute(quary)
        conexion.cerrar()
        messagebox.showinfo(
            'SE EJECUTO AGREGAR AFILIADO',
            f'El beneficiario de identifición: {tam}\nFue añadido a Base de dato con exito!!')
    except Exception as ex:
        messagebox.showerror('ERROR EN AGREGAR BENEFICIARIO', f'{ex}.') 

def agregar_dependiente(objeto):
    conexion = conectarBD()
    #objeto = Dependientes()
    tam = int(max_tuplas('afiliado', 'id')) + 1
    
    quary = f"""INSERT INTO dependiente
        VALUES(\'{tam}\', \'{objeto.nombres}\', \'{objeto.apellidos}\',
        \'{objeto.genero}\', \'{objeto.direccion}\', \'{objeto.email}\',
        \'{objeto.fecha_nacimiento}\', \'{objeto.estado_civil}\', 
        \'{objeto.tipo_afil}\', {objeto.telefono}, \'{objeto.ciudad}\',
        {objeto.ips}, {objeto.ordenes}, {objeto.salario}, \'{objeto.estado_afiliacion}\',
        \'{objeto.fecha_afiliacion}\', \'{objeto.estado}\', \'{objeto.rango_salarial}\'
        );"""
    
    try:
        conexion.cursor.execute(quary)
        conexion.cerrar()
        messagebox.showinfo(
            'SE EJECUTO AGREGAR AFILIADO',
            f'El dependiente de identifición: {tam}\nFue añadido a Base de dato con exito!!')
    except Exception as ex:
        messagebox.showerror('ERROR EN AGREGAR DEPENDIENTE', f'{ex}.')

def agregar_independiente(objeto):
    conexion = conectarBD()
    #objeto = Independientes()
    tam = int(max_tuplas('afiliado', 'id')) + 1
    
    quary = f"""INSERT INTO independiente
        VALUES(\'{tam}\', \'{objeto.nombres}\', \'{objeto.apellidos}\',
        \'{objeto.genero}\', \'{objeto.direccion}\', \'{objeto.email}\',
        \'{objeto.fecha_nacimiento}\', \'{objeto.estado_civil}\', 
        \'{objeto.tipo_afil}\', {objeto.telefono}, \'{objeto.ciudad}\',
        {objeto.ips}, {objeto.ordenes}, {objeto.salario},
        \'{objeto.estado_afiliacion}\', \'{objeto.fecha_afiliacion}\',
        \'{objeto.nombre_empresa}\', {objeto.rut}, \'{objeto.contrato}\', 
        \'{objeto.rango_salarial}\'
        );"""
    
    try:
        conexion.cursor.execute(quary)
        conexion.cerrar()
        messagebox.showinfo(
            'SE EJECUTO AGREGAR AFILIADO',
            f'El independiente de identifición: {tam}\nFue añadido a Base de dato con exito!!')
    except Exception as ex:
        messagebox.showerror('ERROR EN AGREGAR INDEPENDIENTE', f'{ex}.') 

def agregar_empresa(objeto):
    conexion = conectarBD()
    #objeto = Empresa()
    tam = int(max_tuplas('empresa', 'nit')) + 1
    
    quary = f"""INSERT INTO empresa
        VALUES({tam}, \'{objeto.razon_social}\', \'{objeto.ciudad}\',
        \'{objeto.direccion}\', {objeto.telefono},
        \'{objeto.nombre_contacto}\', {objeto.contrato}
        );"""
    
    try:
        conexion.cursor.execute(quary)
        conexion.cerrar()
        messagebox.showinfo(
            'SE EJECUTO AGREGAR EMPRESA',
            f'La empresa de nit: {tam}\nFue añadido a Base de\ndatos con exito!!')
    except Exception as ex:
        messagebox.showerror('ERROR EN AGREGAR INDEPENDIENTE', f'{ex}.') 

# EDIT FUNTIONS
def editar_beneficiario(objeto, id):
    conexion = conectarBD()
    objeto = Beneficiarios()
    
    quary = f"""UPDATE beneficiario
	SET nombre=\'{objeto.nombres}\', apellido=\'{objeto.apellidos}\', genero=\'{objeto.genero}\', 
	direccion=\'{objeto.direccion}\', email=\'{objeto.email}\', fnacimiento=\'{objeto.fecha_nacimiento}\',
	estadocivil=\'{objeto.estado_civil}\', tipoafiliacion=\'{objeto.tipo_afil}\', 
	telefono={objeto.telefono}, ciudad=\'{objeto.ciudad}\', ips={objeto.ips}, 
	ordenes={objeto.ordenes}, parentesco=\'{objeto.parentesco}\'
	WHERE id=\'{id}\';  """
    
    try:
        conexion.cursor.execute(quary)
        conexion.cerrar()
        messagebox.showinfo('FUNCION EDITAR BENEFICIARIO', 'La edición fue exitosa!!')
    except Exception as ex:
        messagebox.showerror('ERROR AL EDITAR BENEFICIARIO', f'{ex}.')

def editar_dependiente(objeto, id):
    conexion = conectarBD()
    
    quary = f"""UPDATE dependiente
	SET nombre=\'{objeto.nombres}\', apellido=\'{objeto.apellidos}\', genero=\'{objeto.genero}\', 
	direccion=\'{objeto.direccion}\', email=\'{objeto.email}\', fnacimiento=\'{objeto.fecha_nacimiento}\',
	estadocivil=\'{objeto.estado_civil}\', tipoafiliacion=\'{objeto.tipo_afil}\', 
	telefono={objeto.telefono}, ciudad=\'{objeto.ciudad}\', ips={objeto.ips}, 
	ordenes={objeto.ordenes}, salario={objeto.salario}, estadoafiliacion=\'{objeto.estado_afiliacion}\', 
	fechaafiliacion=\'{objeto.fecha_afiliacion}\', estado=\'{objeto.estado}\',
	rangosalarial=\'{objeto.rango_salarial}\'
	WHERE id=\'{id}\';  """
    
    try:
        conexion.cursor.execute(quary)
        conexion.cerrar()
        messagebox.showinfo('FUNCION EDITAR DEPENDIENTE', 'La edición fue exitosa!!')
    except Exception as ex:
        messagebox.showerror('ERROR AL EDITAR DEPENDIENTE', f'{ex}.')

def editar_independiente(objeto, id):
    conexion = conectarBD()
    
    quary = f"""UPDATE independiente
	SET nombre=\'{objeto.nombres}\', apellido=\'{objeto.apellidos}\', genero=\'{objeto.genero}\', 
	direccion=\'{objeto.direccion}\', email=\'{objeto.email}\', fnacimiento=\'{objeto.fecha_nacimiento}\',
	estadocivil=\'{objeto.estado_civil}\', tipoafiliacion=\'{objeto.tipo_afil}\', 
	telefono={objeto.telefono}, ciudad=\'{objeto.ciudad}\', ips={objeto.ips}, 
	ordenes={objeto.ordenes}, salario={objeto.salario}, estadoafiliacion=\'{objeto.estado_afiliacion}\', 
	fechaafiliacion=\'{objeto.fecha_afiliacion}\', nombreempresa=\'{objeto.nombre_empresa}\', 
	rut={objeto.rut}, contrato=\'{objeto.contrato}\', rangosalarial=\'{objeto.rango_salarial}\'
	WHERE id=\'{id}\';  """
    
    try:
        conexion.cursor.execute(quary)
        conexion.cerrar()
        messagebox.showinfo('FUNCION EDITAR INDEPENDIENTE', 'La edición fue exitosa!!')
    except Exception as ex:
        messagebox.showerror('ERROR AL EDITAR INDEPENDIENTE', f'{ex}.')

# DELETE FUNTION
def eliminar(id):
    conexion = conectarBD()
    quary = f"""DELETE FROM afiliado WHERE id=\'{id}\';"""
    
    try:
        conexion.cursor.execute(quary)
        conexion.cerrar()
        messagebox.showinfo(
            'SE EJECUTO ELMINAR()',
            f'El afiliado de identifición {id}\nFue eliminado con exito!!')
    except Exception as ex:
        messagebox.showerror('ERROR AL ELIMINAR', f'{ex}.')

def eliminar_key_int(tabla, nit):
    conexion = conectarBD()
    quary = f"""DELETE FROM {tabla} WHERE nit={nit};"""
    
    try:
        conexion.cursor.execute(quary)
        conexion.cerrar()
        messagebox.showinfo(
            'SE EJECUTO ELMINAR()',
            f'El afiliado de identifición {nit}\nde la tabla \'{tabla}\'.\nFue eliminado con exito!!')
    except Exception as ex:
        messagebox.showerror('ERROR AL ELIMINAR', f'{ex}.')