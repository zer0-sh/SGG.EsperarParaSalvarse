import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from model.entidades import Beneficiarios, Dependientes, Independientes, Empresa, consultar, eliminar
from model.entidades import agregar_beneficiario, agregar_dependiente, agregar_independiente
from model.entidades import agregar_empresa, eliminar_key_int, consultar_empresa
from model.entidades import editar_beneficiario, editar_dependiente, editar_independiente

root = tk.Tk()

root.geometry('1280x720')  # 80 * (16/9) , dimensiones
root.title('Proyecto')
root.config(bg='gray')
root.resizable(0,0)

wtotal = root.winfo_screenwidth()
htotal = root.winfo_screenheight()
wventana = 1280
hventana = 720
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)
root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight-50))

main_frame = tk.Frame(root, bg='white') 
""" Generamos un nuevo objeto frame, que se podrá remplazar por otro. 
Existe dentro de main_frame"""
valindante = 0
# --------------------------- HOME FRAME ----------------------------
home_frame = tk.Frame(main_frame, bg='#139a80')
# buttons
btn_home_to_admin = tk.Button(home_frame)
btn_home_to_admin.place(x=390, y=370)
btn_home_to_admin.config(
    text='ADMINISTRADOR', cursor='hand2', bg='#0a5245', fg='white',
    width=17, height=9, font=('Bold', 18), activebackground='#35BD6F')

btn_home_to_natural = tk.Button(home_frame)
btn_home_to_natural.place(x=660, y=370)
btn_home_to_natural.config(
    text='PRÓXIMAMENTE...', cursor='hand2', bg='#0a5245', fg='white',
    width=17, height=9, font=('Bold', 18), activebackground='#35BD6F')

home_frame.pack(fill=tk.BOTH, expand=True)
# -------------------------- SECOND FRAME ---------------------------
second_frame = tk.Frame(main_frame, bg='#139a80')
# buttons
btn_second_to_home = tk.Button(second_frame)
btn_second_to_home.place(relx=0.01, rely=0.01, relwidth=0.16, relheight=0.05)
btn_second_to_home.config(
    text='ATRÁS', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 10), activebackground='#35BD6F')

btn_second_to_gestionar_afil = tk.Button(second_frame)
btn_second_to_gestionar_afil.place(
    x=250, y=320, width=370, height=150)
btn_second_to_gestionar_afil.config(
    text='GESTIONAR\nAFILIACIÓN', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 20), activebackground='#35BD6F')

btn_second_to_gestionar_empresas = tk.Button(second_frame)
btn_second_to_gestionar_empresas.place(
    x=250, y=500, width=370, height=150)
btn_second_to_gestionar_empresas.config(
    text='GESTIONAR\nEMPRESAS', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 20), activebackground='#35BD6F')

btn_second_to_gestionar_contratos = tk.Button(second_frame)
btn_second_to_gestionar_contratos.place(
    x=650, y=320, width=370, height=150)
btn_second_to_gestionar_contratos.config(
    text='GESTIONAR\nCONTRATORS IPS', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 20), activebackground='#35BD6F')

btn_second_to_generar_reportes = tk.Button(second_frame)
btn_second_to_generar_reportes.place(
    x=650, y=500, width=370, height=150)
btn_second_to_generar_reportes.config(
    text='GENERAR\nREPORTES', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 20), activebackground='#35BD6F')

def go_home_to_second():
    deshabilitar_entries_afiliados()
    try:
        home_frame.pack_forget()
        second_frame.pack(fill=tk.BOTH, expand=True)
    except:
        print('ERROR al cambiar de frame')

def go_second_to_home():
    deshabilitar_entries_afiliados()
    try:
        second_frame.pack_forget()
        home_frame.pack(fill=tk.BOTH, expand=True)
    except:
        print('ERROR al cambiar de frame')

btn_home_to_admin.config(command=go_home_to_second)
btn_second_to_home.config(command=go_second_to_home)
# --------------------------- ADMIN FRAME ---------------------------
afiliados_frame = tk.Frame(main_frame, bg='#139a80')

# buttons
btn_admin_to_second = tk.Button(afiliados_frame)
btn_admin_to_second.place(relx=0.01, rely=0.01, relwidth=0.16, relheight=0.05)
btn_admin_to_second.config(
    text='ATRÁS', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 10), activebackground='#35BD6F')

alto_btn = 90    # original: 130
ancho_btn = 320  # original: 280
x_btn = 940      # original: 980
btn_consultar_afiliados = tk.Button(afiliados_frame)
btn_consultar_afiliados.place(x=x_btn, y=100, width=ancho_btn, height=alto_btn)
btn_consultar_afiliados.config(
    text='CONSULTAR', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 28), activebackground='#35BD6F')

btn_nuevo_beneficiario = tk.Button(afiliados_frame)
btn_nuevo_beneficiario.place(x=x_btn, y=200, width=ancho_btn, height=alto_btn)
btn_nuevo_beneficiario.config(
    text='NUEVO\nBENEFICIARIO', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 28), activebackground='#35BD6F')

btn_nuevo_dependiente = tk.Button(afiliados_frame)
btn_nuevo_dependiente.place(x=x_btn, y=300, width=ancho_btn, height=alto_btn)
btn_nuevo_dependiente.config(
    text='NUEVO\nDEPENDIENTE', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 28), activebackground='#35BD6F')

btn_nuevo_independiente = tk.Button(afiliados_frame)
btn_nuevo_independiente.place(x=x_btn, y=400, width=ancho_btn, height=alto_btn)
btn_nuevo_independiente.config(
    text='NUEVO\nINDEPENDIENTE', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 28), activebackground='#35BD6F')

btn_guardar = tk.Button(afiliados_frame)
btn_guardar.place(x=x_btn, y=500, width=ancho_btn, height=alto_btn)
btn_guardar.config(
    text='GUARDAR', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 28), activebackground='#35BD6F')

btn_eliminar = tk.Button(afiliados_frame)
btn_eliminar.place(x=x_btn, y=600, width=ancho_btn, height=alto_btn)
btn_eliminar.config(
    text='ELIMINAR', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 28), activebackground='#35BD6F')

# ENTRIES and DATEENTRIES
ancho = 230  # original: 200
alto = 40    # original: 40
x_col_izq = 220  # 220
x_col_der = 690

mi_id = tk.StringVar()
id_entry = tk.Entry(afiliados_frame, textvariable=mi_id, font=('Bold', 20))
id_entry.place(x=x_col_izq, y=100, width=ancho, height=alto)

mi_nombre = tk.StringVar()
nombre_entry = tk.Entry(afiliados_frame, textvariable=mi_nombre, font=('Bold', 20))
nombre_entry.place(x=x_col_izq, y=150, width=ancho, height=alto)

mi_apellido = tk.StringVar()
apellido_entry = tk.Entry(afiliados_frame, textvariable=mi_apellido, font=('Bold', 20))
apellido_entry.place(x=x_col_izq, y=200, width=ancho, height=alto)

mi_genero = tk.StringVar()
genero_entry = tk.OptionMenu(afiliados_frame, mi_genero, *['Masculino', 'Femenino'])
genero_entry.place(x=x_col_izq, y=250, width=ancho, height=alto)

mi_direccion = tk.StringVar()
direccion_entry = tk.Entry(afiliados_frame, textvariable=mi_direccion, font=('Bold', 20))
direccion_entry.place(x=x_col_izq, y=300, width=ancho, height=alto)

mi_email = tk.StringVar()
email_entry = tk.Entry(afiliados_frame, textvariable=mi_email, font=('Bold', 20))
email_entry.place(x=x_col_izq, y=350, width=ancho, height=alto)

mi_fecha_nacimiento = tk.StringVar()
fecha_nac_dateentry = DateEntry(afiliados_frame, textvariable=mi_fecha_nacimiento, font=('Bold', 20))
fecha_nac_dateentry.place(x=x_col_izq, y=400, width=ancho, height=alto)

mi_estado_civil = tk.StringVar()
estado_civil_entry = tk.OptionMenu(
    afiliados_frame, mi_estado_civil, *['Soltero', 'Casado', 'Union Libre'])
estado_civil_entry.place(x=x_col_izq, y=450, width=ancho, height=alto)

mi_tipo_afil = tk.StringVar()
tipo_afil_entry = tk.Entry(afiliados_frame, textvariable=mi_tipo_afil, font=('Bold', 20))
tipo_afil_entry.place(x=x_col_izq, y=500, width=ancho, height=alto)

mi_telefono = tk.StringVar()
telefono_entry = tk.Entry(afiliados_frame, textvariable=mi_telefono, font=('Bold', 20))
telefono_entry.place(x=x_col_izq, y=550, width=ancho, height=alto)

mi_ciudad = tk.StringVar()
ciudad_entry = tk.Entry(afiliados_frame, textvariable=mi_ciudad, font=('Bold', 20))
ciudad_entry.place(x=x_col_izq, y=600, width=ancho, height=alto)

mi_ips = tk.StringVar()
ips_entry = tk.OptionMenu(
    afiliados_frame, mi_ips, *['40001', '40002', '40003', '40004', '40005'])
ips_entry.place(x=x_col_izq, y=650, width=ancho, height=alto)

#-------- COLUMNA DERRECHA
mi_ordenes = tk.StringVar()
ordenes_entry = tk.OptionMenu(
    afiliados_frame, mi_ordenes, *['20001', '20002', '20003', '20004', '20005', '20006'])
ordenes_entry.place(x=x_col_der, y=100, width=ancho, height=alto)

mi_parentesco = tk.StringVar()
parentesco_entry = tk.OptionMenu(
    afiliados_frame, mi_parentesco, *['Cónyuge', 'Padre', 'Madre', 'Hijo', 'Hermanos', 'Amigos'])
parentesco_entry.place(x=x_col_der, y=150, width=ancho, height=alto)

mi_cotizante = tk.StringVar()
cotizante_entry = tk.Entry(afiliados_frame, textvariable=mi_cotizante, font=('Bold', 20))
cotizante_entry.place(x=x_col_der, y=200, width=ancho, height=alto)

mi_salario = tk.StringVar()
salario_entry = tk.Entry(afiliados_frame, textvariable=mi_salario, font=('Bold', 20))
salario_entry.place(x=x_col_der, y=250, width=ancho, height=alto)

mi_estado_afiliacion = tk.StringVar()
estado_afil_entry = tk.OptionMenu(
    afiliados_frame, mi_estado_afiliacion, *['Activo', 'Retirado', 'Inactivo'])
estado_afil_entry.place(x=x_col_der, y=300, width=ancho, height=alto)

mi_fecha_afiliacion = tk.StringVar()
fecha_afil_dateentry = DateEntry(afiliados_frame, textvariable=mi_fecha_afiliacion, font=('Bold', 20))
fecha_afil_dateentry.place(x=x_col_der, y=350, width=ancho, height=alto)

mi_rango_salarial = tk.StringVar()
rango_salarial_entry = tk.OptionMenu(afiliados_frame, mi_rango_salarial, *['A', 'B', 'C'])
rango_salarial_entry.place(x=x_col_der, y=400, width=ancho, height=alto)

mi_estado = tk.StringVar()
estado_entry = tk.OptionMenu(afiliados_frame, mi_estado, *['Activo', 'Inactivo'])
estado_entry.place(x=x_col_der, y=450, width=ancho, height=alto)

mi_nombre_empresa = tk.StringVar()
nombre_empresa_entry = tk.Entry(afiliados_frame, textvariable=mi_nombre_empresa, font=('Bold', 20))
nombre_empresa_entry.place(x=x_col_der, y=500, width=ancho, height=alto)

mi_rut = tk.StringVar()
rut_entry = tk.Entry(afiliados_frame, textvariable=mi_rut, font=('Bold', 20))
rut_entry.place(x=x_col_der, y=550, width=ancho, height=alto)

mi_contrato = tk.StringVar()
contrato_entry = tk.OptionMenu(
    afiliados_frame, mi_contrato, *['60001', '60002', '60003', '60004', '60005', '60006'])
contrato_entry.place(x=x_col_der, y=600, width=ancho, height=alto)

# Labels
def etiquetas_afiliados():
    ancho = 220  # original: 200
    alto = 40    # original: 40
    x_col_izq = 0   # original: 20
    x_col_der = 470  # original: 510
    title_label = tk.Label(
        afiliados_frame, text='AFILIADOS', font=('Bold', 40), bg='#139a80', fg='white',
        anchor='s')
    title_label.place(x=450, y=20, width=300, height=60)

    id_label = tk.Label(
        afiliados_frame, text='ID:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    id_label.place(x=x_col_izq, y=100, width=ancho, height=alto)

    nombre_label = tk.Label(
        afiliados_frame, text='NOMBRE:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    nombre_label.place(x=x_col_izq, y=150, width=ancho, height=alto)

    apellido_label = tk.Label(
        afiliados_frame, text='APELLIDO:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    apellido_label.place(x=x_col_izq, y=200, width=ancho, height=alto)

    genero_label = tk.Label(
        afiliados_frame, text='GÉNERO:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    genero_label.place(x=x_col_izq, y=250, width=ancho, height=alto)

    direccion_label = tk.Label(
        afiliados_frame, text='DIRECCIÓN:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    direccion_label.place(x=x_col_izq, y=300, width=ancho, height=alto)

    email_label = tk.Label(
        afiliados_frame, text='EMAIL:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    email_label.place(x=x_col_izq, y=350, width=ancho, height=alto)

    fecha_nac_label = tk.Label(
        afiliados_frame, text='FECHA NAC:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    fecha_nac_label.place(x=x_col_izq, y=400, width=ancho, height=alto)

    estado_civil_label = tk.Label(
        afiliados_frame, text='ESTADO CIVIL:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    estado_civil_label.place(x=x_col_izq, y=450, width=ancho, height=alto)

    tipo_afil_label = tk.Label(
        afiliados_frame, text='TIPO DE AFIL:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    tipo_afil_label.place(x=x_col_izq, y=500, width=ancho, height=alto)

    telefono_label = tk.Label(
        afiliados_frame, text='TELÉFONO:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    telefono_label.place(x=x_col_izq, y=550, width=ancho, height=alto)
    
    ciudad_label = tk.Label(
        afiliados_frame, text='CIUDAD:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    ciudad_label.place(x=x_col_izq, y=600, width=ancho, height=alto)

    ips_label = tk.Label(
        afiliados_frame, text='IPS:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    ips_label.place(x=x_col_izq, y=650, width=ancho, height=alto)
        
    #-------- COLUMNA DERECHA
    ordenes_label = tk.Label(
        afiliados_frame, text='ORDENES:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    ordenes_label.place(x=x_col_der, y=100, width=ancho, height=alto)
    
    parentesco_label = tk.Label(
        afiliados_frame, text='PARENTESCO:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    parentesco_label.place(x=x_col_der, y=150, width=ancho, height=alto)
    
    beneficiario_label = tk.Label(
        afiliados_frame, text='BENEFICIARIO:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    beneficiario_label.place(x=x_col_der, y=200, width=ancho, height=alto)
    
    salario_label = tk.Label(
        afiliados_frame, text='SALARIO:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    salario_label.place(x=x_col_der, y=250, width=ancho, height=alto)
    
    estado_afil_label = tk.Label(
        afiliados_frame, text='ESTADO AFIL:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    estado_afil_label.place(x=x_col_der, y=300, width=ancho, height=alto)
    
    fecha_afil_label = tk.Label(
        afiliados_frame, text='FECHA AFIL:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    fecha_afil_label.place(x=x_col_der, y=350, width=ancho, height=alto)
    
    rango_salarial_label = tk.Label(
        afiliados_frame, text='RAN SALARIAL:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    rango_salarial_label.place(x=x_col_der, y=400, width=ancho, height=alto)
   
    estado_label = tk.Label(
        afiliados_frame, text='ESTADO:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    estado_label.place(x=x_col_der, y=450, width=ancho, height=alto)
    
    nombre_empresa_label = tk.Label(
        afiliados_frame, text='NOM EMPRESA:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    nombre_empresa_label.place(x=x_col_der, y=500, width=ancho, height=alto)
    
    rut_label = tk.Label(
        afiliados_frame, text='RUT:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    rut_label.place(x=x_col_der, y=550, width=ancho, height=alto)
    
    contrato_label = tk.Label(
        afiliados_frame, text='CONTRATO:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    contrato_label.place(x=x_col_der, y=600, width=ancho, height=alto)

etiquetas_afiliados()

# FUNTIONS
def deshabilitar_entries_afiliados():
    global valindante
    valindante = 0
    
    mi_id.set('')
    mi_nombre.set('')
    mi_apellido.set('')
    mi_genero.set('')
    mi_direccion.set('')
    mi_email.set('')
    mi_fecha_nacimiento.set('')
    mi_estado_civil.set('')
    mi_tipo_afil.set('')
    mi_telefono.set('')
    mi_ciudad.set('')
    mi_ips.set('')
    mi_ordenes.set('')
    mi_parentesco.set('')
    mi_cotizante.set('')
    mi_salario.set('')
    mi_estado_afiliacion.set('')
    mi_fecha_afiliacion.set('')
    mi_rango_salarial.set('')
    mi_estado.set('')
    mi_nombre_empresa.set('')
    mi_rut.set('')
    mi_contrato.set('')
    
    color = '#139a80'
    
    id_entry.config(state='normal')
    nombre_entry.config(state='disabled', background=color, )
    apellido_entry.config(state='disabled', bg=color)
    genero_entry.config(state='disabled', bg=color)
    direccion_entry.config(state='disabled', bg=color)
    email_entry.config(state='disabled', bg=color)
    fecha_nac_dateentry.config(state='disabled')
    estado_civil_entry.config(state='disabled', bg=color)
    tipo_afil_entry.config(state='disabled', bg=color)
    telefono_entry.config(state='disabled', bg=color)
    ciudad_entry.config(state='disabled', bg=color)
    ips_entry.config(state='disabled', bg=color)
    ordenes_entry.config(state='disabled', bg=color)
    parentesco_entry.config(state='disabled', bg=color)
    cotizante_entry.config(state='disabled', bg=color)
    salario_entry.config(state='disabled', bg=color)
    estado_afil_entry.config(state='disabled', bg=color)
    fecha_afil_dateentry.config(state='disabled')
    rango_salarial_entry.config(state='disabled', bg=color)
    estado_entry.config(state='disabled', bg=color)
    nombre_empresa_entry.config(state='disabled', bg=color)
    rut_entry.config(state='disabled', bg=color)
    contrato_entry.config(state='disabled', bg=color)
    
    btn_guardar.config(state='disabled')

def go_second_to_admin():
    deshabilitar_entries_afiliados()
    try:
        second_frame.pack_forget()
        afiliados_frame.pack(fill=tk.BOTH, expand=True)
    except:
        print('ERROR al cambiar de frame')

def go_admin_to_second():
    deshabilitar_entries_afiliados()
    try:
        afiliados_frame.pack_forget()
        second_frame.pack(fill=tk.BOTH, expand=True)
    except:
        print('ERROR al cambiar de frame')

btn_second_to_gestionar_afil.config(command=go_second_to_admin)
btn_admin_to_second.config(command=go_admin_to_second)

def habilitar_campos_beneficiario():
    global valindante
    deshabilitar_entries_afiliados()
    valindante = 1
    mi_tipo_afil.set('Beneficiario')

    nombre_entry.config(state='normal', bg='white')
    apellido_entry.config(state='normal', bg='white')
    genero_entry.config(state='normal', bg='white')
    direccion_entry.config(state='normal', bg='white')
    email_entry.config(state='normal', bg='white')
    fecha_nac_dateentry.config(state='normal')
    estado_civil_entry.config(state='normal', bg='white')
    tipo_afil_entry.config(state='disabled', bg='white')
    telefono_entry.config(state='normal', bg='white')
    ciudad_entry.config(state='normal', bg='white')
    ips_entry.config(state='normal', bg='white')
    ordenes_entry.config(state='normal', bg='white')
    parentesco_entry.config(state='normal', bg='white')
    cotizante_entry.config(state='normal', bg='white')
    
    btn_guardar.config(state='normal')

def habilitar_campos_dependiente():
    global valindante
    deshabilitar_entries_afiliados()
    valindante = 2
    mi_tipo_afil.set('Cotizante')
    
    nombre_entry.config(state='normal', bg='white')
    apellido_entry.config(state='normal', bg='white')
    genero_entry.config(state='normal', bg='white')
    direccion_entry.config(state='normal', bg='white')
    email_entry.config(state='normal', bg='white')
    fecha_nac_dateentry.config(state='normal')
    estado_civil_entry.config(state='normal', bg='white')
    tipo_afil_entry.config(state='disabled', bg='white')
    telefono_entry.config(state='normal', bg='white')
    ciudad_entry.config(state='normal', bg='white')
    ips_entry.config(state='normal', bg='white')
    ordenes_entry.config(state='normal', bg='white')
    salario_entry.config(state='normal', bg='white')
    estado_afil_entry.config(state='normal', bg='white')
    fecha_afil_dateentry.config(state='normal')
    rango_salarial_entry.config(state='normal', bg='white')
    estado_entry.config(state='normal', bg='white')
    
    btn_guardar.config(state='normal')

def habilitar_campos_independiente():
    global valindante
    deshabilitar_entries_afiliados()
    valindante = 3
    mi_tipo_afil.set('Cotizante')
    
    nombre_entry.config(state='normal', bg='white')
    apellido_entry.config(state='normal', bg='white')
    genero_entry.config(state='normal', bg='white')
    direccion_entry.config(state='normal', bg='white')
    email_entry.config(state='normal', bg='white')
    fecha_nac_dateentry.config(state='normal')
    estado_civil_entry.config(state='normal', bg='white')
    tipo_afil_entry.config(state='disabled', bg='white')
    telefono_entry.config(state='normal', bg='white')
    ciudad_entry.config(state='normal', bg='white')
    ips_entry.config(state='normal', bg='white')
    ordenes_entry.config(state='normal', bg='white')
    salario_entry.config(state='normal', bg='white')
    estado_afil_entry.config(state='normal', bg='white')
    fecha_afil_dateentry.config(state='normal')
    rango_salarial_entry.config(state='normal', bg='white')
    nombre_empresa_entry.config(state='normal', bg='white')
    rut_entry.config(state='normal', bg='white')
    contrato_entry.config(state='normal', bg='white')
    
    btn_guardar.config(state='normal')

def listar():
    
    llave = str(mi_id.get())
    deshabilitar_entries_afiliados()
    
    try:
        
        try:  # Beneficiario
            beneficiario = consultar(llave, 'beneficiario')
            
            mi_id.set(beneficiario[0][0])
            mi_nombre.set(beneficiario[0][1])
            mi_apellido.set(beneficiario[0][2])
            mi_genero.set(beneficiario[0][3])
            mi_direccion.set(beneficiario[0][4])
            mi_email.set(beneficiario[0][5])
            mi_fecha_nacimiento.set(beneficiario[0][6])
            mi_estado_civil.set(beneficiario[0][7])
            mi_tipo_afil.set(beneficiario[0][8])
            mi_telefono.set(beneficiario[0][9])
            mi_ciudad.set(beneficiario[0][10])
            mi_ips.set(beneficiario[0][11])
            mi_ordenes.set(beneficiario[0][12])
            mi_parentesco.set(beneficiario[0][13])
            mi_cotizante.set('')
            
        except Exception as e:
            pass
        
        try:  # Dependiente
            dependiente = consultar(llave, 'dependiente')
            
            mi_id.set(dependiente[0][0])
            mi_nombre.set(dependiente[0][1])
            mi_apellido.set(dependiente[0][2])
            mi_genero.set(dependiente[0][3])
            mi_direccion.set(dependiente[0][4])
            mi_email.set(dependiente[0][5])
            mi_fecha_nacimiento.set(dependiente[0][6])
            mi_estado_civil.set(dependiente[0][7])
            mi_tipo_afil.set(dependiente[0][8])
            mi_telefono.set(dependiente[0][9])
            mi_ciudad.set(dependiente[0][10])
            mi_ips.set(dependiente[0][11])
            mi_ordenes.set(dependiente[0][12])
            mi_salario.set(dependiente[0][13])
            mi_estado_afiliacion.set(dependiente[0][14])
            mi_fecha_afiliacion.set(dependiente[0][15])
            mi_estado.set(dependiente[0][16])
            mi_rango_salarial.set(dependiente[0][17])
        except Exception as e:
            pass
        
        try:  # Independiente
            independiente = consultar(llave, 'independiente')
            
            mi_id.set(independiente[0][0])
            mi_nombre.set(independiente[0][1])
            mi_apellido.set(independiente[0][2])
            mi_genero.set(independiente[0][3])
            mi_direccion.set(independiente[0][4])
            mi_email.set(independiente[0][5])
            mi_fecha_nacimiento.set(independiente[0][6])
            mi_estado_civil.set(independiente[0][7])
            mi_tipo_afil.set(independiente[0][8])
            mi_telefono.set(independiente[0][9])
            mi_ciudad.set(independiente[0][10])
            mi_ips.set(independiente[0][11])
            mi_ordenes.set(independiente[0][12])
            mi_salario.set(independiente[0][13])
            mi_estado_afiliacion.set(independiente[0][14])
            mi_fecha_afiliacion.set(independiente[0][15])
            mi_nombre_empresa.set(independiente[0][16])
            mi_rut.set(independiente[0][17])
            mi_contrato.set(independiente[0][18])
            mi_rango_salarial.set(independiente[0][19])
        except Exception as e:
            pass
        
    except Exception as ex:
        messagebox.showerror('Fallo al listar', f'{ex}.')

def guardar_datos():
    
    f_nac = fecha_nac_dateentry.get_date().strftime("%y-%m-%d")
    
    if valindante == 1:
        
        obj_beneficiario = Beneficiarios(
            mi_nombre.get(), mi_apellido.get(), mi_genero.get(), mi_direccion.get(),
            mi_email.get(), f_nac, mi_estado_civil.get(), mi_tipo_afil.get(),
            mi_telefono.get(), mi_ciudad.get(), mi_ips.get(), mi_ordenes.get(), 
            mi_parentesco.get(), mi_cotizante.get(), 
        )
        if mi_id.get() == '':
            agregar_beneficiario(obj_beneficiario)
        else:
            editar_beneficiario(obj_beneficiario, mi_id.get())
    elif valindante == 2:
        
        f_afil = fecha_afil_dateentry.get_date().strftime("%y-%m-%d")
        
        obj_dependiente = Dependientes(
            mi_nombre.get(), mi_apellido.get(), mi_genero.get(), mi_direccion.get(),
            mi_email.get(), f_nac, mi_estado_civil.get(), mi_tipo_afil.get(),
            mi_telefono.get(), mi_ciudad.get(), mi_ips.get(), mi_ordenes.get(),
            mi_salario.get(), mi_estado_afiliacion.get(), f_afil, 
            mi_rango_salarial.get(), mi_estado.get()
        )
        if mi_id.get() == '':
            agregar_dependiente(obj_dependiente)
        else:
            editar_dependiente(obj_dependiente, mi_id.get())
    elif valindante == 3:
        
        f_afil = fecha_afil_dateentry.get_date().strftime("%y-%m-%d")
        
        obj_independiente = Independientes(
            mi_nombre.get(), mi_apellido.get(), mi_genero.get(), mi_direccion.get(),
            mi_email.get(), f_nac, mi_estado_civil.get(), mi_tipo_afil.get(), 
            mi_telefono.get(), mi_ciudad.get(), mi_ips.get(), mi_ordenes.get(),
            mi_salario.get(), mi_estado_afiliacion.get(), f_afil, mi_rango_salarial.get(),
            mi_nombre_empresa.get(), mi_rut.get(), mi_contrato.get()
        )
        if mi_id.get() == '':
            agregar_independiente(obj_independiente)
        else:
            editar_independiente(obj_independiente, mi_id.get())

def eliminar_tupla():
    llave = str(mi_id.get())
    try:
        listar()
        eliminar(llave)
    except Exception as ex:
        messagebox.showerror('Fallo al eliminar', f'{ex}.')

btn_consultar_afiliados.config(command=listar)
btn_nuevo_beneficiario.config(command=habilitar_campos_beneficiario)
btn_nuevo_dependiente.config(command=habilitar_campos_dependiente)
btn_nuevo_independiente.config(command=habilitar_campos_independiente)
btn_guardar.config(command=guardar_datos)
btn_eliminar.config(command=eliminar_tupla)
# ------------------------- EMPRESAS FRAME --------------------------
empresas_frame = tk.Frame(main_frame, bg='#139a80')

# BUTTONS
btn_empresas_to_second = tk.Button(empresas_frame)
btn_empresas_to_second.place(relx=0.01, rely=0.01, relwidth=0.16, relheight=0.05)
btn_empresas_to_second.config(
    text='ATRÁS', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 10), activebackground='#35BD6F')

alto_btn = 80    # original: 90
ancho_btn = 295  # original: 320
y_btn = 570      # original: 650
btn_consultar_empresas = tk.Button(empresas_frame)
btn_consultar_empresas.place(x=20, y=y_btn, width=ancho_btn, height=alto_btn)
btn_consultar_empresas.config(
    text='CONSULTAR', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 28), activebackground='#35BD6F')

btn_agregar_empresas = tk.Button(empresas_frame)
btn_agregar_empresas.place(x=335, y=y_btn, width=ancho_btn, height=alto_btn)
btn_agregar_empresas.config(
    text='AGREGAR', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 28), activebackground='#35BD6F')

btn_guardar_empresas = tk.Button(empresas_frame)
btn_guardar_empresas.place(x=650, y=y_btn, width=ancho_btn, height=alto_btn)
btn_guardar_empresas.config(
    text='GUARDAR', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 28), activebackground='#35BD6F')

btn_eliminar_empresas = tk.Button(empresas_frame)
btn_eliminar_empresas.place(x=965, y=y_btn, width=ancho_btn, height=alto_btn)
btn_eliminar_empresas.config(
    text='ELIMINAR', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 28), activebackground='#35BD6F')

#ENTRIES
ancho = 310
alto = 60
x_col_izq = 300
x_col_der = 930

# izquierda ------------
mi_nit_empresa = tk.StringVar()
nit_entry_emp = tk.Entry(empresas_frame, textvariable=mi_nit_empresa, font=('Bold', 20))
nit_entry_emp.place(x=x_col_izq, y=200, width=ancho, height=alto)

mi_razon_social = tk.StringVar()
razon_social_entry = tk.Entry(empresas_frame, textvariable=mi_razon_social, font=('Bold', 20))
razon_social_entry.place(x=x_col_izq, y=280, width=ancho, height=alto)

ciudad_entry_emp = tk.Entry(empresas_frame, textvariable=mi_ciudad, font=('Bold', 20))
ciudad_entry_emp.place(x=x_col_izq, y=360, width=ancho, height=alto)

direccion_entry_emp = tk.Entry(empresas_frame, textvariable=mi_direccion, font=('Bold', 20))
direccion_entry_emp.place(x=x_col_izq, y=440, width=ancho, height=alto)

# derecha --------------
telefono_entry_emp = tk.Entry(empresas_frame, textvariable=mi_telefono, font=('Bold', 20))
telefono_entry_emp.place(x=x_col_der, y=200, width=ancho, height=alto)

mi_nombre_contacto = tk.StringVar()
nombre_contacto_entry = tk.Entry(empresas_frame, textvariable=mi_nombre_contacto, font=('Bold', 20))
nombre_contacto_entry.place(x=x_col_der, y=280, width=ancho, height=alto)
    
contrato_entry_emp = tk.OptionMenu(
    empresas_frame, mi_contrato, *['60001', '60002', '60003', '60004', '60005', '60006'])
contrato_entry_emp.place(x=x_col_der, y=360, width=ancho, height=alto)

# LABELS
def etiquetas_empresas():
    ancho = 300  # original: 200
    alto = 60    # original: 40
    x_col_izq = 0   # original: 20
    x_col_der = 630   # original: 510
    title_label = tk.Label(
        empresas_frame, text='EMPRESAS', font=('Bold', 40), bg='#139a80', fg='white',
        anchor='center')
    title_label.place(x=520, y=70, width=300, height=60) # tittle

    # izquierda ------------
    nit_label = tk.Label(
        empresas_frame, text='NIT:', font=('Bold', 25), bg='#139a80', fg='white', anchor='e')
    nit_label.place(x=x_col_izq, y=200, width=ancho, height=alto)

    razon_social_label = tk.Label(
        empresas_frame, text='RAZON SOCIAL:', font=('Bold', 25), bg='#139a80', fg='white', anchor='e')
    razon_social_label.place(x=x_col_izq, y=280, width=ancho, height=alto)
    
    ciudad_label = tk.Label(
        empresas_frame, text='CIUDAD:', font=('Bold', 25), bg='#139a80', fg='white', anchor='e')
    ciudad_label.place(x=x_col_izq, y=360, width=ancho, height=alto)

    direccion_label = tk.Label(
        empresas_frame, text='DIRECCIÓN:', font=('Bold', 25), bg='#139a80', fg='white', anchor='e')
    direccion_label.place(x=x_col_izq, y=440, width=ancho, height=alto)
    
    # derecha --------------
    telefono_label = tk.Label(
        empresas_frame, text='TELÉFONO:', font=('Bold', 25), bg='#139a80', fg='white', anchor='e')
    telefono_label.place(x=x_col_der, y=200, width=ancho, height=alto)

    nombre_contacto_label = tk.Label(
        empresas_frame, text='NOM CONTACTO:', font=('Bold', 25), bg='#139a80', fg='white', anchor='e')
    nombre_contacto_label.place(x=x_col_der, y=280, width=ancho, height=alto)
    
    contrato_label = tk.Label(
        empresas_frame, text='CONTRATO:', font=('Bold', 25), bg='#139a80', fg='white', anchor='e')
    contrato_label.place(x=x_col_der, y=360, width=ancho, height=alto)
    
etiquetas_empresas()

# FUNTIONS
def deshabilitar_entries_empresas():
    
    btn_guardar_empresas.config(state='disabled')
    
    mi_nit_empresa.set('')
    mi_razon_social.set('')
    mi_ciudad.set('')
    mi_direccion.set('')
    mi_telefono.set('')
    mi_nombre_contacto.set('')
    mi_contrato.set('')
    
    nit_entry_emp.config(state='normal')
    razon_social_entry.config(state='disabled')
    ciudad_entry_emp.config(state='disabled')
    direccion_entry_emp.config(state='disabled')
    telefono_entry_emp.config(state='disabled')
    nombre_contacto_entry.config(state='disabled')
    contrato_entry_emp.config(state='disabled')

def listar_empresa():
    try:
        llave = str(mi_nit_empresa.get())
        empresa = consultar_empresa(llave, 'empresa')
        
        mi_nit_empresa.set(empresa[0][0])
        mi_razon_social.set(empresa[0][1])
        mi_ciudad.set(empresa[0][2])
        mi_direccion.set(empresa[0][3])
        mi_telefono.set(empresa[0][4])
        mi_nombre_contacto.set(empresa[0][5])
        mi_contrato.set(empresa[0][6])
        
    except Exception as ex:
        messagebox.showerror('Fallo al listar', f'{ex}.')

def go_second_to_empresas():
    
    deshabilitar_entries_empresas()
    
    try:
        second_frame.pack_forget()
        empresas_frame.pack(fill=tk.BOTH, expand=True)
    except:
        print('ERROR al cambiar de frame')

def go_empresas_to_second():
    
    deshabilitar_entries_empresas()
    
    try:
        empresas_frame.pack_forget()
        second_frame.pack(fill=tk.BOTH, expand=True)
    except:
        print('ERROR al cambiar de frame')

btn_second_to_gestionar_empresas.config(command=go_second_to_empresas)
btn_empresas_to_second.config(command=go_empresas_to_second)

def habilitar_campos_empresa():
    
    btn_guardar_empresas.config(state='normal')
    
    razon_social_entry.config(state='normal')
    ciudad_entry_emp.config(state='normal')
    direccion_entry_emp.config(state='normal')
    telefono_entry_emp.config(state='normal')
    nombre_contacto_entry.config(state='normal')
    contrato_entry_emp.config(state='normal')

def empresa_agregar():
    obj_empresa = Empresa(
        mi_razon_social.get(), mi_ciudad.get(), mi_direccion.get(), mi_telefono.get(),
        mi_nombre_contacto.get(), mi_contrato.get()
    )
    
    if mi_nit_empresa.get() == '':
        agregar_empresa(obj_empresa)
    else:
        print(f'no pasó al agregar_empresas()')

def eliminar_empresa():
    llave = str(mi_nit_empresa.get())
    try:
        listar()
        eliminar_key_int('empresa', llave)
    except Exception as ex:
        messagebox.showerror('FALLO AL ELIMINAR', f'{ex}.')

btn_consultar_empresas.config(command=listar_empresa)
btn_agregar_empresas.config(command=habilitar_campos_empresa)
btn_guardar_empresas.config(command=empresa_agregar)
btn_eliminar_empresas.config(command=eliminar_empresa)
# ------------------------ CONTRATOS FRAME --------------------------
contratos_frame = tk.Frame(main_frame, bg='#139a80')

# BUTTONS
btn_contratos_to_second = tk.Button(contratos_frame)
btn_contratos_to_second.place(relx=0.01, rely=0.01, relwidth=0.16, relheight=0.05)
btn_contratos_to_second.config(
    text='ATRÁS', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 10), activebackground='#35BD6F')

# LABELS
title_label = tk.Label(
    contratos_frame, text='CONTRATOS', font=('Bold', 35), bg='#139a80', fg='white',
    anchor='center')
title_label.place(x=520, y=70, width=300, height=60)


def go_second_to_contratos():
    try:
        second_frame.pack_forget()
        contratos_frame.pack(fill=tk.BOTH, expand=True)
    except:
        print('ERROR al cambiar de frame')

def go_contratos_to_second():
    try:
        contratos_frame.pack_forget()
        second_frame.pack(fill=tk.BOTH, expand=True)
    except:
        print('ERROR al cambiar de frame')

btn_second_to_gestionar_contratos.config(command=go_second_to_contratos)
btn_contratos_to_second.config(command=go_contratos_to_second)
# ------------------------ REPORTES FRAME ---------------------------
reportes_frame = tk.Frame(main_frame, bg='#139a80')

# BUTTONS
btn_reportes_to_second = tk.Button(reportes_frame)
btn_reportes_to_second.place(relx=0.01, rely=0.01, relwidth=0.16, relheight=0.05)
btn_reportes_to_second.config(
    text='ATRÁS', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 10), activebackground='#35BD6F')

# LABELS
title_label = tk.Label(
    reportes_frame, text='REPORTES', font=('Bold', 35), bg='#139a80', fg='white',
    anchor='center')
title_label.place(x=520, y=70, width=300, height=60)

def go_second_to_reportes():
    try:
        second_frame.pack_forget()
        reportes_frame.pack(fill=tk.BOTH, expand=True)
    except:
        print('ERROR al cambiar de frame')

def go_reportes_to_second():
    try:
        reportes_frame.pack_forget()
        second_frame.pack(fill=tk.BOTH, expand=True)
    except:
        print('ERROR al cambiar de frame')

btn_second_to_generar_reportes.config(command=go_second_to_reportes)
btn_reportes_to_second.config(command=go_reportes_to_second)
# --------------------------- MAIN FRAME ----------------------------
main_frame.pack(fill=tk.BOTH, expand=True)
# -------------------------------------------------------------------
root.mainloop()