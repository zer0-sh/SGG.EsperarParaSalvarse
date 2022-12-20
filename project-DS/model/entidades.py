from tkinter import messagebox
from .conexion_bd import conectarBD

class Afiliados:
    def __init__(
        self, nombres, genero, dir, email, apellidos,
        f_nac, ciudad, telf, est_civ, ips):
        
        self.id = None
        self.nombres = nombres
        self.genero = genero
        self.direccion = dir
        self.email = email
        self.apellidos = apellidos
        self.fecha_nacimiento = f_nac
        self.ciudad = ciudad
        self.telefono = telf
        self.estado_civil = est_civ
        self.ips = ips

class Beneficiarios(Afiliados):
    def __init__(
        self, nombres, genero, dir, email, apellidos, f_nac, 
        ciudad, telf, est_civ, ips, parentesco, cotizante):
        super().__init__(
            nombres, genero, dir, email, apellidos, f_nac, 
            ciudad, telf, est_civ, ips)
        self.parentesco = parentesco
        self.cotizante = cotizante

class Cotizantes(Afiliados):
    def __init__(
        self, nombres, genero, dir, email, apellidos, f_nac, ciudad,
        telf, est_civ, ips, salario, estado_afil, f_afil, rango_sal):
        super().__init__(
            nombres, genero, dir, email, apellidos, f_nac, ciudad, telf, est_civ, ips)
        self.salario = salario
        self.estado_afiliacion = estado_afil
        self.fecha_afiliacion = f_afil
        self.rango_salarial = rango_sal
        
class Dependientes(Cotizantes):
    def __init__(
        self, nombres, genero, dir, email, apellidos, f_nac, ciudad, telf, 
        est_civ, ips, salario, estado_afil, f_afil, rango_sal, empresa):
        super().__init__(
            nombres, genero, dir, email, apellidos, f_nac, ciudad, telf, est_civ, ips,
            salario, estado_afil, f_afil, rango_sal)
        self.empresa = empresa

class Independientes(Cotizantes):
    def __init__(
        self, nombres, genero, dir, email, apellidos, f_nac, ciudad, telf, est_civ, ips, 
        salario, estado_afil, f_afil, rango_sal, nom_empresa, rut, contrato):
        super().__init__(
            nombres, genero, dir, email, apellidos, f_nac, ciudad, telf, est_civ, 
            ips, salario, estado_afil, f_afil, rango_sal)
        self.nombre_empresa = nom_empresa
        self.rut = rut
        self.contrato = contrato

class Empresa:
    def __init__(
        self, razonsocial,ciudad, direccion, telefono, nombrecontacto):
        self.nit = None
        
        self.razon_social = razonsocial
        self.ciudad = ciudad
        self.direccion = direccion
        self.telefono = telefono
        self.nombre_contacto = nombrecontacto

class Reporte:
    def __init__(self, nro_radicado, fecha_recibo, afiliado, contrato):
        self.num_radicado = nro_radicado
        self.fecha_recibo = fecha_recibo
        self.afiliado = afiliado
        self.contrato = contrato

class Contratos:
    def __init__(self, num_radicado, estado, afiliado, empresa):
        self.num_radicado = num_radicado
        self.estado = estado
        self.afiliado = afiliado
        self.empresa = empresa

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
    
    quary = f"""INSERT INTO beneficiario(
	id, nombres, genero, direccion,
	correoelectronico, apellidos, fnacimiento,
	ciudadresi, telefono, estadocivil,
	ips, parentesco, cotizante)
	VALUES ({tam}, \'{objeto.nombres}\', \'{objeto.genero}\', \'{objeto.direccion}\',
			\'{objeto.email}\', \'{objeto.apellidos}\', \'{objeto.fecha_nacimiento}\',
			\'{objeto.ciudad}\', {objeto.telefono}, \'{objeto.estado_civil}\',
			{objeto.ips}, \'{objeto.parentesco}\', {objeto.cotizante});"""
    
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
    
    quary = f"""INSERT INTO empresa(
	nit, razonsocial, ciudad, direccion, telefono, nombrecontacto)
	VALUES ({tam}, \'{objeto.razon_social}\', \'{objeto.ciudad}\',
    \'{objeto.direccion}\', {objeto.telefono}, \'{objeto.nombre_contacto}\');"""
    
    try:
        conexion.cursor.execute(quary)
        conexion.cerrar()
        messagebox.showinfo(
            'SE EJECUTO AGREGAR EMPRESA',
            f'La empresa de nit: {tam}\nFue añadido a Base de\ndatos con exito!!')
    except Exception as ex:
        messagebox.showerror('ERROR EN AGREGAR EMPRESA', f'{ex}.')

def agregar_contratos(objeto):
    conexion = conectarBD()
    #objeto = Contratos()
    tam = int(max_tuplas('contrato', 'nroradicado')) + 1
    
    quary = f"""INSERT INTO contrato(
	nroradicado, estado, afiliado, empresa)
	VALUES ({tam}, \'{objeto.estado}\', {objeto.afiliado}, {objeto.empresa});"""
    
    try:
        conexion.cursor.execute(quary)
        conexion.cerrar()
        messagebox.showinfo(
            'SE EJECUTO AGREGAR CONTRATO',
            f'El contrato de número: {tam}\nFue añadido a Base de\ndatos con exito!!')
    except Exception as ex:
        messagebox.showerror('ERROR EN AGREGAR CONTRATO', f'{ex}.')

def agregar_reporte(objeto):
    conexion = conectarBD()
    objeto = Reporte()
    tam = int(max_tuplas('reporte', 'radicadorepor')) + 1
    
    quary = f"""INSERT INTO reporteretiro(
	nroradicado, fecharetiro, afiliado, contrato)
	VALUES ({tam}, \'{objeto.fecha_recibo}\', {objeto.afiliado}, {objeto.contrato});"""
    
    try:
        conexion.cursor.execute(quary)
        conexion.cerrar()
        messagebox.showinfo(
            'SE EJECUTO AGREGAR REPORTE',
            f'El reporte de número: {tam}\nFue añadido a Base de\ndatos con exito!!')
    except Exception as ex:
        messagebox.showerror('ERROR EN AGREGAR REPORTE', f'{ex}.')

# EDIT FUNTIONS
def editar_beneficiario(objeto, id):
    conexion = conectarBD()
    #objeto = Beneficiarios()
    
    quary = f"""UPDATE beneficiario
	SET nombres=\'{objeto.nombres}\', genero=\'{objeto.genero}\',
    direccion=\'{objeto.direccion}\', correoelectronico=\'{objeto.email}\', 
    apellidos=\'{objeto.apellidos}\', fnacimiento=\'{objeto.fecha_nacimiento}\', 
    ciudadresi=\'{objeto.ciudad}\', telefono={objeto.telefono}, 
    estadocivil=\'{objeto.estado_civil}\', ips={objeto.ips}, 
    parentesco=\'{objeto.parentesco}\', cotizante={objeto.cotizante}
	WHERE id={id};"""
    
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

def editar_empresa(objeto, nit):
    conexion = conectarBD()
    #objeto = Empresa()
    
    quary = f"""UPDATE empresa
	SET razonsocial=\'{objeto.razon_social}\', ciudad=\'{objeto.ciudad}\',
    direccion=\'{objeto.direccion}\', telefono={objeto.telefono},
    nombrecontacto=\'{objeto.nombre_contacto}\'
	WHERE nit={nit};"""
    
    try:
        conexion.cursor.execute(quary)
        conexion.cerrar()
        messagebox.showinfo('FUNCION EDITAR EMPRESA', 'La edición fue exitosa!!')
    except Exception as ex:
        messagebox.showerror('ERROR AL EDITAR EMPRESA', f'{ex}.')

def editar_contratos(objeto, num_radicado):
    conexion = conectarBD()
    #objeto = Contratos()
    
    quary = f"""UPDATE contrato
	SET estado=\'{objeto.estado}\', afiliado={objeto.afiliado}, empresa={objeto.empresa}
	WHERE nroradicado={num_radicado};"""
    
    try:
        conexion.cursor.execute(quary)
        conexion.cerrar()
        messagebox.showinfo('FUNCION EDITAR CONTRATOS', 'La edición fue exitosa!!')
    except Exception as ex:
        messagebox.showerror('ERROR AL EDITAR CONTRATOS', f'{ex}.')

def editar_reporte(objeto, num_radicado):
    conexion = conectarBD()
    objeto = Reporte()
    
    quary = f"""UPDATE reporteretiro
	SET fecharetiro=\'{objeto.fecha_recibo}\', afiliado={objeto.afiliado},
    contrato={objeto.contrato}	WHERE nroradicado={num_radicado};"""
    
    try:
        conexion.cursor.execute(quary)
        conexion.cerrar()
        messagebox.showinfo('FUNCION EDITAR REPORTE', 'La edición fue exitosa!!')
    except Exception as ex:
        messagebox.showerror('ERROR AL EDITAR REPORTE', f'{ex}.')

# DELETE FUNTION
def eliminar(id, tabla, tipo):
    conexion = conectarBD()
    quary = f"""DELETE FROM {tabla} WHERE {tipo}={id};"""
    
    try:
        conexion.cursor.execute(quary)
        conexion.cerrar()
        messagebox.showinfo(
            'SE EJECUTO ELMINAR()',
            f'El afiliado de identifición: {id}\nFue eliminado con exito!!')
    except Exception as ex:
        messagebox.showerror('ERROR AL ELIMINAR', f'{ex}.')
