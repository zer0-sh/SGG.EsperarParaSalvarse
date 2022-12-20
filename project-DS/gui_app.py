import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from model.entidades import Beneficiarios, Dependientes, Independientes, Empresa, consultar, eliminar
from model.entidades import agregar_beneficiario, agregar_dependiente, agregar_independiente
from model.entidades import agregar_empresa, consultar_empresa
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
# GLOBAL VARIABLES
valindante = 0
color_btn_normal = '#1a6a60'
color_btn_presion = '#1f7b70'
x_atras=50
y_atras=50
atras_ancho = 120
atras_alto = 60
# ------------------------------------- HOME FRAME --------------------------------------
home_frame = tk.Frame(main_frame, bg='#139a80')

def aplicar_fondo(frame):
    img = Image.open('project-DS/Administrador Banco.jpg')
    #new_imagen = img.resize((1280,720))
    render = ImageTk.PhotoImage(img)
    img1 = tk.Label(frame, image=render)
    img1.image = render
    img1.place(x=0, y=0)

aplicar_fondo(home_frame)

# buttons
btn_home_to_admin = tk.Button(home_frame)
btn_home_to_admin.place(x=390, y=370)
btn_home_to_admin.config(
    text='ADMINISTRADOR', cursor='hand2', bg=color_btn_normal, fg='white',
    width=17, height=9, font=('Bold', 18), activebackground=color_btn_presion)

btn_home_to_banco = tk.Button(home_frame)
btn_home_to_banco.place(x=660, y=370)
btn_home_to_banco.config(
    text='BANCO', cursor='hand2', bg=color_btn_normal, fg='white',
    width=17, height=9, font=('Bold', 18), activebackground=color_btn_presion)

home_frame.pack(fill=tk.BOTH, expand=True)
# ------------------------------------ SECOND FRAME -------------------------------------
second_frame = tk.Frame(main_frame, bg='#139a80')

aplicar_fondo(second_frame)

# buttons
btn_second_to_home = tk.Button(second_frame)
btn_second_to_home.place(x=x_atras, y=y_atras, width=atras_ancho, height=atras_alto)
btn_second_to_home.config(
    text='ATRÁS', cursor='hand2', bg=color_btn_normal, fg='white',
    font=('Bold', 20), activebackground=color_btn_presion)

btn_second_to_gestionar_afil = tk.Button(second_frame)
btn_second_to_gestionar_afil.place(
    x=250, y=320, width=370, height=150)
btn_second_to_gestionar_afil.config(
    text='GESTIONAR\nAFILIACIÓN', cursor='hand2', bg=color_btn_normal, fg='white',
    font=('Bold', 20), activebackground=color_btn_presion)

btn_second_to_gestionar_empresas = tk.Button(second_frame)
btn_second_to_gestionar_empresas.place(
    x=250, y=500, width=370, height=150)
btn_second_to_gestionar_empresas.config(
    text='GESTIONAR\nEMPRESAS', cursor='hand2', bg=color_btn_normal, fg='white',
    font=('Bold', 20), activebackground=color_btn_presion)

btn_second_to_gestionar_contratos = tk.Button(second_frame)
btn_second_to_gestionar_contratos.place(
    x=650, y=320, width=370, height=150)
btn_second_to_gestionar_contratos.config(
    text='GESTIONAR\nCONTRATORS IPS', cursor='hand2', bg=color_btn_normal, fg='white',
    font=('Bold', 20), activebackground=color_btn_presion)

btn_second_to_generar_reportes = tk.Button(second_frame)
btn_second_to_generar_reportes.place(
    x=650, y=500, width=370, height=150)
btn_second_to_generar_reportes.config(
    text='GENERAR\nREPORTES', cursor='hand2', bg=color_btn_normal, fg='white',
    font=('Bold', 20), activebackground=color_btn_presion)

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
# ------------------------------------- ADMIN FRAME -------------------------------------
afiliados_frame = tk.Frame(main_frame, bg='#139a80')

aplicar_fondo(afiliados_frame)

# buttons
btn_admin_to_second = tk.Button(afiliados_frame)
btn_admin_to_second.place(x=x_atras, y=y_atras, width=atras_ancho, height=atras_alto)
btn_admin_to_second.config(
    text='ATRÁS', cursor='hand2', bg=color_btn_normal, fg='white',
    font=('Bold', 20), activebackground=color_btn_presion)

alto_btn = 90
ancho_btn = 240
x_btn = 990
btn_consultar_afiliados = tk.Button(afiliados_frame)
btn_consultar_afiliados.place(x=x_btn, y=130, width=ancho_btn, height=alto_btn)
btn_consultar_afiliados.config(
    text='CONSULTAR', cursor='hand2', bg=color_btn_normal, fg='white',
    font=('Bold', 25), activebackground=color_btn_presion)

btn_nuevo_beneficiario = tk.Button(afiliados_frame)
btn_nuevo_beneficiario.place(x=x_btn, y=220, width=ancho_btn, height=alto_btn)
btn_nuevo_beneficiario.config(
    text='NUEVO\nBENEFICIARIO', cursor='hand2', bg=color_btn_normal, fg='white',
    font=('Bold', 25), activebackground=color_btn_presion)

btn_nuevo_dependiente = tk.Button(afiliados_frame)
btn_nuevo_dependiente.place(x=x_btn, y=310, width=ancho_btn, height=alto_btn)
btn_nuevo_dependiente.config(
    text='NUEVO\nDEPENDIENTE', cursor='hand2', bg=color_btn_normal, fg='white',
    font=('Bold', 25), activebackground=color_btn_presion)

btn_nuevo_independiente = tk.Button(afiliados_frame)
btn_nuevo_independiente.place(x=x_btn, y=400, width=ancho_btn, height=alto_btn)
btn_nuevo_independiente.config(
    text='NUEVO\nINDEPENDIENTE', cursor='hand2', bg=color_btn_normal, fg='white',
    font=('Bold', 22), activebackground=color_btn_presion)

btn_guardar = tk.Button(afiliados_frame)
btn_guardar.place(x=x_btn, y=490, width=ancho_btn, height=alto_btn)
btn_guardar.config(
    text='GUARDAR', cursor='hand2', bg=color_btn_normal, fg='white',
    font=('Bold', 25), activebackground=color_btn_presion)

btn_eliminar = tk.Button(afiliados_frame)
btn_eliminar.place(x=x_btn, y=580, width=ancho_btn, height=alto_btn)
btn_eliminar.config(
    text='ELIMINAR', cursor='hand2', bg=color_btn_normal, fg='white',
    font=('Bold', 25), activebackground=color_btn_presion)

# ENTRIES and DATEENTRIES
ancho = 225  # original: 200
alto = 40    # original: 40
x_col_izq = 275  # 220
x_col_der = 745

mi_id = tk.StringVar()
id_entry = tk.Entry(afiliados_frame, textvariable=mi_id, font=('Bold', 20))
id_entry.place(x=x_col_izq, y=130, width=ancho, height=alto)

mi_nombre = tk.StringVar()
nombre_entry = tk.Entry(afiliados_frame, textvariable=mi_nombre, font=('Bold', 20))
nombre_entry.place(x=x_col_izq, y=180, width=ancho, height=alto)

mi_apellido = tk.StringVar()
apellido_entry = tk.Entry(afiliados_frame, textvariable=mi_apellido, font=('Bold', 20))
apellido_entry.place(x=x_col_izq, y=230, width=ancho, height=alto)

mi_genero = tk.StringVar()
genero_entry = tk.OptionMenu(afiliados_frame, mi_genero, *['M', 'F'])
genero_entry.place(x=x_col_izq, y=280, width=ancho, height=alto)

mi_direccion = tk.StringVar()
direccion_entry = tk.Entry(afiliados_frame, textvariable=mi_direccion, font=('Bold', 20))
direccion_entry.place(x=x_col_izq, y=330, width=ancho, height=alto)

mi_email = tk.StringVar()
email_entry = tk.Entry(afiliados_frame, textvariable=mi_email, font=('Bold', 20))
email_entry.place(x=x_col_izq, y=380, width=ancho, height=alto)

mi_fecha_nacimiento = tk.StringVar()
fecha_nac_dateentry = DateEntry(afiliados_frame, textvariable=mi_fecha_nacimiento, font=('Bold', 20))
fecha_nac_dateentry.place(x=x_col_izq, y=430, width=ancho, height=alto)

mi_ciudad = tk.StringVar()
ciudad_entry = tk.Entry(afiliados_frame, textvariable=mi_ciudad, font=('Bold', 20))
ciudad_entry.place(x=x_col_izq, y=480, width=ancho, height=alto)

mi_telefono = tk.StringVar()
telefono_entry = tk.Entry(afiliados_frame, textvariable=mi_telefono, font=('Bold', 20))
telefono_entry.place(x=x_col_izq, y=530, width=ancho, height=alto)

mi_estado_civil = tk.StringVar()
estado_civil_entry = tk.OptionMenu(
    afiliados_frame, mi_estado_civil, *['Soltero', 'Casado', 'Union Libre'])
estado_civil_entry.place(x=x_col_izq, y=580, width=ancho, height=alto)

mi_ips = tk.StringVar()
ips_entry = tk.OptionMenu(
    afiliados_frame, mi_ips, *['40001', '40002', '40003', '40004', '40005'])
ips_entry.place(x=x_col_izq, y=630, width=ancho, height=alto)

#-------- COLUMNA DERRECHA
mi_parentesco = tk.StringVar()
parentesco_entry = tk.OptionMenu(
    afiliados_frame, mi_parentesco, *['Cónyuge', 'Padre', 'Madre', 'Hijo', 'Hermanos', 'Amigos'])
parentesco_entry.place(x=x_col_der, y=130, width=ancho, height=alto)

mi_cotizante = tk.StringVar()
cotizante_entry = tk.Entry(afiliados_frame, textvariable=mi_cotizante, font=('Bold', 20))
cotizante_entry.place(x=x_col_der, y=180, width=ancho, height=alto)

mi_salario = tk.StringVar()
salario_entry = tk.Entry(afiliados_frame, textvariable=mi_salario, font=('Bold', 20))
salario_entry.place(x=x_col_der, y=230, width=ancho, height=alto)

mi_estado_afiliacion = tk.StringVar()
estado_afil_entry = tk.OptionMenu(
    afiliados_frame, mi_estado_afiliacion, *['Activo', 'Retirado', 'Inactivo'])
estado_afil_entry.place(x=x_col_der, y=280, width=ancho, height=alto)

mi_fecha_afiliacion = tk.StringVar()
fecha_afil_dateentry = DateEntry(afiliados_frame, textvariable=mi_fecha_afiliacion, font=('Bold', 20))
fecha_afil_dateentry.place(x=x_col_der, y=330, width=ancho, height=alto)

mi_rango_salarial = tk.StringVar()
rango_salarial_entry = tk.Entry(afiliados_frame, textvariable=mi_rango_salarial, font=('Bold', 20))
rango_salarial_entry.place(x=x_col_der, y=380, width=ancho, height=alto)

mi_empresa_afiliado = tk.StringVar()
empresa_entry = tk.OptionMenu(
    afiliados_frame, mi_empresa_afiliado,
    *['80001', '80002', '80003', '80004', '80005', '80006'])
empresa_entry.place(x=x_col_der, y=430, width=ancho, height=alto)

mi_nombre_empresa = tk.StringVar()
nombre_empresa_entry = tk.Entry(afiliados_frame, textvariable=mi_nombre_empresa, font=('Bold', 20))
nombre_empresa_entry.place(x=x_col_der, y=480, width=ancho, height=alto)

mi_rut = tk.StringVar()
rut_entry = tk.Entry(afiliados_frame, textvariable=mi_rut, font=('Bold', 20))
rut_entry.place(x=x_col_der, y=530, width=ancho, height=alto)

mi_contrato = tk.StringVar()
contrato_entry = tk.OptionMenu(
    afiliados_frame, mi_contrato,
    *['60001', '60002', '60003', '60004', '60005', '60006', '60007', '60008'])
contrato_entry.place(x=x_col_der, y=580, width=ancho, height=alto)

# Labels
def etiquetas_afiliados():
    ancho = 225  # original: 200
    alto = 40    # original: 40
    x_col_izq = 50   # original: 20
    x_col_der = 520  # original: 510
    title_label = tk.Label(
        afiliados_frame, text='AFILIADOS', font=('Bold', 40), bg='#139a80', fg='white',
        anchor='s')
    title_label.place(x=440, y=50, width=400, height=60)

    id_label = tk.Label(
        afiliados_frame, text='ID:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    id_label.place(x=x_col_izq, y=130, width=ancho, height=alto)

    nombre_label = tk.Label(
        afiliados_frame, text='NOMBRE:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    nombre_label.place(x=x_col_izq, y=180, width=ancho, height=alto)

    apellido_label = tk.Label(
        afiliados_frame, text='APELLIDO:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    apellido_label.place(x=x_col_izq, y=230, width=ancho, height=alto)

    genero_label = tk.Label(
        afiliados_frame, text='GÉNERO:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    genero_label.place(x=x_col_izq, y=280, width=ancho, height=alto)

    direccion_label = tk.Label(
        afiliados_frame, text='DIRECCIÓN:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    direccion_label.place(x=x_col_izq, y=330, width=ancho, height=alto)

    email_label = tk.Label(
        afiliados_frame, text='EMAIL:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    email_label.place(x=x_col_izq, y=380, width=ancho, height=alto)

    fecha_nac_label = tk.Label(
        afiliados_frame, text='FECHA NAC:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    fecha_nac_label.place(x=x_col_izq, y=430, width=ancho, height=alto)

    ciudad_label = tk.Label(
        afiliados_frame, text='CIUDAD:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    ciudad_label.place(x=x_col_izq, y=480, width=ancho, height=alto)

    telefono_label = tk.Label(
        afiliados_frame, text='TELÉFONO:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    telefono_label.place(x=x_col_izq, y=530, width=ancho, height=alto)

    estado_civil_label = tk.Label(
        afiliados_frame, text='ESTADO CIVIL:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    estado_civil_label.place(x=x_col_izq, y=580, width=ancho, height=alto)

    ips_label = tk.Label(
        afiliados_frame, text='IPS:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    ips_label.place(x=x_col_izq, y=630, width=ancho, height=alto)
        
    #-------- COLUMNA DERECHA
    parentesco_label = tk.Label(
        afiliados_frame, text='PARENTESCO:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    parentesco_label.place(x=x_col_der, y=130, width=ancho, height=alto)
    
    cotizante_label = tk.Label(
        afiliados_frame, text='COTIZANTE:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    cotizante_label.place(x=x_col_der, y=180, width=ancho, height=alto)
    
    salario_label = tk.Label(
        afiliados_frame, text='SALARIO:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    salario_label.place(x=x_col_der, y=230, width=ancho, height=alto)
    
    estado_afil_label = tk.Label(
        afiliados_frame, text='ESTADO AFIL:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    estado_afil_label.place(x=x_col_der, y=280, width=ancho, height=alto)
    
    fecha_afil_label = tk.Label(
        afiliados_frame, text='FECHA AFIL:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    fecha_afil_label.place(x=x_col_der, y=330, width=ancho, height=alto)
    
    rango_salarial_label = tk.Label(
        afiliados_frame, text='RAN SALARIAL:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    rango_salarial_label.place(x=x_col_der, y=380, width=ancho, height=alto)
    
    empresa_label = tk.Label(
        afiliados_frame, text='EMPRESA:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    empresa_label.place(x=x_col_der, y=430, width=ancho, height=alto)
    
    nombre_empresa_label = tk.Label(
        afiliados_frame, text='NOM EMPRESA:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    nombre_empresa_label.place(x=x_col_der, y=480, width=ancho, height=alto)
    
    rut_label = tk.Label(
        afiliados_frame, text='RUT:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    rut_label.place(x=x_col_der, y=530, width=ancho, height=alto)
    
    contrato_label = tk.Label(
        afiliados_frame, text='CONTRATO:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    contrato_label.place(x=x_col_der, y=580, width=ancho, height=alto)

etiquetas_afiliados()

# FUNTIONS
def deshabilitar_entries_afiliados():
    global valindante
    valindante = 0
    
    mi_id.set('')
    mi_nombre.set('')
    mi_genero.set('')
    mi_direccion.set('')
    mi_email.set('')
    mi_apellido.set('')
    mi_fecha_nacimiento.set('')
    mi_ciudad.set('')
    mi_telefono.set('')
    mi_estado_civil.set('')
    mi_ips.set('')
    mi_parentesco.set('')
    mi_cotizante.set('')
    mi_salario.set('')
    mi_estado_afiliacion.set('')
    mi_fecha_afiliacion.set('')
    mi_rango_salarial.set('')
    mi_empresa_afiliado.set('')
    mi_nombre_empresa.set('')
    mi_rut.set('')
    mi_contrato.set('')
    
    id_entry.config(state='normal')
    nombre_entry.config(state='disabled', background=color_btn_normal)
    genero_entry.config(state='disabled', bg=color_btn_normal)
    direccion_entry.config(state='disabled', bg=color_btn_normal)
    email_entry.config(state='disabled', bg=color_btn_normal)
    apellido_entry.config(state='disabled', bg=color_btn_normal)
    fecha_nac_dateentry.config(state='disabled')
    ciudad_entry.config(state='disabled', bg=color_btn_normal)
    telefono_entry.config(state='disabled', bg=color_btn_normal)
    estado_civil_entry.config(state='disabled', bg=color_btn_normal)
    ips_entry.config(state='disabled', bg=color_btn_normal)
    parentesco_entry.config(state='disabled', bg=color_btn_normal)
    cotizante_entry.config(state='disabled', bg=color_btn_normal)
    salario_entry.config(state='disabled', bg=color_btn_normal)
    estado_afil_entry.config(state='disabled', bg=color_btn_normal)
    fecha_afil_dateentry.config(state='disabled')
    rango_salarial_entry.config(state='disabled', bg=color_btn_normal)
    empresa_entry.config(state='disabled', bg=color_btn_normal)
    nombre_empresa_entry.config(state='disabled', bg=color_btn_normal)
    rut_entry.config(state='disabled', bg=color_btn_normal)
    contrato_entry.config(state='disabled', bg=color_btn_normal)
    
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

    nombre_entry.config(state='normal', bg='white')
    apellido_entry.config(state='normal', bg='white')
    direccion_entry.config(state='normal', bg='white')
    email_entry.config(state='normal', bg='white')
    genero_entry.config(state='normal', bg='white')
    fecha_nac_dateentry.config(state='normal')
    ciudad_entry.config(state='normal', bg='white')
    telefono_entry.config(state='normal', bg='white')
    estado_civil_entry.config(state='normal', bg='white')
    ips_entry.config(state='normal', bg='white')
    parentesco_entry.config(state='normal', bg='white')
    cotizante_entry.config(state='normal', bg='white')
    
    btn_guardar.config(state='normal')

def habilitar_campos_dependiente():
    global valindante
    deshabilitar_entries_afiliados()
    valindante = 2
    
    nombre_entry.config(state='normal', bg='white')
    apellido_entry.config(state='normal', bg='white')
    direccion_entry.config(state='normal', bg='white')
    email_entry.config(state='normal', bg='white')
    genero_entry.config(state='normal', bg='white')
    fecha_nac_dateentry.config(state='normal')
    ciudad_entry.config(state='normal', bg='white')
    telefono_entry.config(state='normal', bg='white')
    estado_civil_entry.config(state='normal', bg='white')
    ips_entry.config(state='normal', bg='white')
    salario_entry.config(state='normal', bg='white')
    estado_afil_entry.config(state='normal', bg='white')
    fecha_afil_dateentry.config(state='normal')
    rango_salarial_entry.config(state='normal', bg='white')
    empresa_entry.config(state='normal', bg='white')
    
    btn_guardar.config(state='normal')

def habilitar_campos_independiente():
    global valindante
    deshabilitar_entries_afiliados()
    valindante = 3
    
    nombre_entry.config(state='normal', bg='white')
    apellido_entry.config(state='normal', bg='white')
    direccion_entry.config(state='normal', bg='white')
    email_entry.config(state='normal', bg='white')
    genero_entry.config(state='normal', bg='white')
    fecha_nac_dateentry.config(state='normal')
    ciudad_entry.config(state='normal', bg='white')
    telefono_entry.config(state='normal', bg='white')
    estado_civil_entry.config(state='normal', bg='white')
    ips_entry.config(state='normal', bg='white')
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
    print(f'llave: {llave}')
    deshabilitar_entries_afiliados()
    try:
        
        try:  # Beneficiario
            beneficiario = consultar(llave, 'beneficiario')
            
            mi_id.set(beneficiario[0][0])
            mi_nombre.set(beneficiario[0][1])
            mi_genero.set(beneficiario[0][2])
            mi_direccion.set(beneficiario[0][3])
            mi_email.set(beneficiario[0][4])
            mi_apellido.set(beneficiario[0][5])
            mi_fecha_nacimiento.set(beneficiario[0][6])
            mi_ciudad.set(beneficiario[0][7])
            mi_telefono.set(beneficiario[0][8])
            mi_estado_civil.set(beneficiario[0][9])
            mi_ips.set(beneficiario[0][10])
            mi_parentesco.set(beneficiario[0][11])
            mi_cotizante.set(beneficiario[0][12])    
        except Exception as e:
            pass
        
        try:  # Dependiente
            dependiente = consultar(llave, 'dependiente')
            
            mi_id.set(beneficiario[0][0])
            mi_nombre.set(beneficiario[0][1])
            mi_genero.set(beneficiario[0][2])
            mi_direccion.set(beneficiario[0][3])
            mi_email.set(beneficiario[0][4])
            mi_apellido.set(beneficiario[0][5])
            mi_fecha_nacimiento.set(beneficiario[0][6])
            mi_ciudad.set(beneficiario[0][7])
            mi_telefono.set(beneficiario[0][8])
            mi_estado_civil.set(beneficiario[0][9])
            mi_ips.set(beneficiario[0][10])
            mi_salario.set(dependiente[0][11])
            mi_estado_afiliacion.set(dependiente[0][12])
            mi_fecha_afiliacion.set(dependiente[0][13])
            mi_rango_salarial.set(dependiente[0][14])
            mi_empresa_afiliado.set(dependiente[0][15])
        except Exception as e:
            pass
        
        try:  # Independiente
            independiente = consultar(llave, 'independiente')
            
            mi_id.set(beneficiario[0][0])
            mi_nombre.set(beneficiario[0][1])
            mi_genero.set(beneficiario[0][2])
            mi_direccion.set(beneficiario[0][3])
            mi_email.set(beneficiario[0][4])
            mi_apellido.set(beneficiario[0][5])
            mi_fecha_nacimiento.set(beneficiario[0][6])
            mi_ciudad.set(beneficiario[0][7])
            mi_telefono.set(beneficiario[0][8])
            mi_estado_civil.set(beneficiario[0][9])
            mi_ips.set(beneficiario[0][10])
            mi_salario.set(dependiente[0][11])
            mi_estado_afiliacion.set(dependiente[0][12])
            mi_fecha_afiliacion.set(dependiente[0][13])
            mi_rango_salarial.set(dependiente[0][14])
            mi_nombre_empresa.set(dependiente[0][15])
            mi_rut.set(dependiente[0][16])
            mi_contrato.set(dependiente[0][17])
        except Exception as e:
            pass
        
    except Exception as ex:
        messagebox.showerror('Fallo al listar', f'{ex}.')

def guardar_datos():
    
    f_nac = fecha_nac_dateentry.get_date().strftime("%y-%m-%d")
    
    if valindante == 1:
        
        obj_beneficiario = Beneficiarios(
            mi_nombre.get(), mi_genero.get(), mi_direccion.get(),
            mi_email.get(), mi_apellido.get(), f_nac, mi_ciudad.get(),
            mi_telefono.get(),  mi_estado_civil.get(), mi_ips.get(),
            mi_parentesco.get(), mi_cotizante.get()
        )
        if mi_id.get() == '':
            agregar_beneficiario(obj_beneficiario)
        else:
            editar_beneficiario(obj_beneficiario, mi_id.get())
    elif valindante == 2:
        
        f_afil = fecha_afil_dateentry.get_date().strftime("%y-%m-%d")
        
        obj_dependiente = Dependientes(
            mi_nombre.get(), mi_genero.get(), mi_direccion.get(),
            mi_email.get(), mi_apellido.get(), f_nac, mi_estado_civil.get(),
            mi_ciudad.get(), mi_telefono.get(), mi_ips.get(),
            mi_salario.get(), mi_estado_afiliacion.get(), f_afil, 
            mi_rango_salarial.get(), mi_empresa_afiliado.get()
        )
        if mi_id.get() == '':
            agregar_dependiente(obj_dependiente)
        else:
            editar_dependiente(obj_dependiente, mi_id.get())
    elif valindante == 3:
        
        f_afil = fecha_afil_dateentry.get_date().strftime("%y-%m-%d")
        
        obj_independiente = Independientes(
            mi_nombre.get(), mi_genero.get(), mi_direccion.get(),
            mi_email.get(), mi_apellido.get(), f_nac, mi_estado_civil.get(),
            mi_ciudad.get(), mi_telefono.get(), mi_ips.get(),
            mi_salario.get(), mi_estado_afiliacion.get(), f_afil, 
            mi_rango_salarial.get(), mi_nombre_empresa.get(),
            mi_rut.get(), mi_contrato.get()
        )
        if mi_id.get() == '':
            agregar_independiente(obj_independiente)
        else:
            editar_independiente(obj_independiente, mi_id.get())

def eliminar_tupla():
    llave = str(mi_id.get())
    try:
        listar()
        eliminar(llave, 'afiliado', 'id')
    except Exception as ex:
        messagebox.showerror('Fallo al eliminar', f'{ex}.')

btn_consultar_afiliados.config(command=listar)
btn_nuevo_beneficiario.config(command=habilitar_campos_beneficiario)
btn_nuevo_dependiente.config(command=habilitar_campos_dependiente)
btn_nuevo_independiente.config(command=habilitar_campos_independiente)
btn_guardar.config(command=guardar_datos)
btn_eliminar.config(command=eliminar_tupla)

# ----------------------------------- EMPRESAS FRAME ------------------------------------
empresas_frame = tk.Frame(main_frame, bg='#139a80')

aplicar_fondo(empresas_frame)

# BUTTONS
btn_empresas_to_second = tk.Button(empresas_frame)
btn_empresas_to_second.place(x=x_atras, y=y_atras, width=atras_ancho, height=atras_alto)
btn_empresas_to_second.config(
    text='ATRÁS', cursor='hand2', bg=color_btn_normal, fg='white',
    font=('Bold', 20), activebackground=color_btn_presion)

alto_btn = 80    # original: 90
ancho_btn = 295  # original: 320
y_btn = 570      # original: 650
btn_consultar_empresas = tk.Button(empresas_frame)
btn_consultar_empresas.place(x=20, y=y_btn, width=ancho_btn, height=alto_btn)
btn_consultar_empresas.config(
    text='CONSULTAR', cursor='hand2', bg=color_btn_normal, fg='white',
    font=('Bold', 28), activebackground=color_btn_presion)

btn_agregar_empresas = tk.Button(empresas_frame)
btn_agregar_empresas.place(x=335, y=y_btn, width=ancho_btn, height=alto_btn)
btn_agregar_empresas.config(
    text='AGREGAR', cursor='hand2', bg=color_btn_normal, fg='white',
    font=('Bold', 28), activebackground=color_btn_presion)

btn_guardar_empresas = tk.Button(empresas_frame)
btn_guardar_empresas.place(x=650, y=y_btn, width=ancho_btn, height=alto_btn)
btn_guardar_empresas.config(
    text='GUARDAR', cursor='hand2', bg=color_btn_normal, fg='white',
    font=('Bold', 28), activebackground=color_btn_presion)

btn_eliminar_empresas = tk.Button(empresas_frame)
btn_eliminar_empresas.place(x=965, y=y_btn, width=ancho_btn, height=alto_btn)
btn_eliminar_empresas.config(
    text='ELIMINAR', cursor='hand2', bg=color_btn_normal, fg='white',
    font=('Bold', 28), activebackground=color_btn_presion)

#ENTRIES
ancho = 310
alto = 60
x_col_izq = 300
x_col_der = 930

# izquierda ------------
mi_nit = tk.StringVar()
nit_entry_emp = tk.Entry(empresas_frame, textvariable=mi_nit, font=('Bold', 20))
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
    title_label = tk.Label(
        empresas_frame, text='EMPRESAS', font=('Bold', 40), bg='#139a80', fg='white',
        anchor='center')
    title_label.place(x=520, y=70, width=300, height=60) # tittle

    ancho = 300  # original: 200
    alto = 60    # original: 40
    x_col_izq = 0   # original: 20
    x_col_der = 630   # original: 510
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
    
    mi_nit.set('')
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
        llave = str(mi_nit.get())
        empresa = consultar_empresa(llave, 'empresa')
        
        mi_nit.set(empresa[0][0])
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
    
    if mi_nit.get() == '':
        agregar_empresa(obj_empresa)
    else:
        print(f'no pasó al agregar_empresas()')

def eliminar_empresa():
    llave = str(mi_nit.get())
    try:
        listar()
        eliminar(llave, 'empresa', 'nit')
    except Exception as ex:
        messagebox.showerror('FALLO AL ELIMINAR', f'{ex}.')

btn_consultar_empresas.config(command=listar_empresa)
btn_agregar_empresas.config(command=habilitar_campos_empresa)
btn_guardar_empresas.config(command=empresa_agregar)
btn_eliminar_empresas.config(command=eliminar_empresa)
# ---------------------------------- CONTRATOS FRAME ------------------------------------
contratos_frame = tk.Frame(main_frame, bg='#139a80')

aplicar_fondo(contratos_frame)

# BUTTONS
btn_contratos_to_second = tk.Button(contratos_frame)
btn_contratos_to_second.place(x=x_atras, y=y_atras, width=atras_ancho, height=atras_alto)
btn_contratos_to_second.config(
    text='ATRÁS', cursor='hand2', bg=color_btn_normal, fg='white',
    font=('Bold', 20), activebackground=color_btn_presion)

alto_btn = 100    # original: 90
ancho_btn = 310  # original: 320
y_btn = 550      # original: 650
btn_consultar_empresas = tk.Button(contratos_frame)
btn_consultar_empresas.place(x=20, y=y_btn, width=ancho_btn, height=alto_btn)
btn_consultar_empresas.config(
    text='CONSULTAR', cursor='hand2', bg=color_btn_normal, fg='white',
    font=('Bold', 28), activebackground=color_btn_presion)

btn_agregar_empresas = tk.Button(contratos_frame)
btn_agregar_empresas.place(x=330, y=y_btn, width=ancho_btn, height=alto_btn)
btn_agregar_empresas.config(
    text='AGREGAR', cursor='hand2', bg=color_btn_normal, fg='white',
    font=('Bold', 28), activebackground=color_btn_presion)

btn_guardar_empresas = tk.Button(contratos_frame)
btn_guardar_empresas.place(x=640, y=y_btn, width=ancho_btn, height=alto_btn)
btn_guardar_empresas.config(
    text='GUARDAR', cursor='hand2', bg=color_btn_normal, fg='white',
    font=('Bold', 28), activebackground=color_btn_presion)

btn_eliminar_empresas = tk.Button(contratos_frame)
btn_eliminar_empresas.place(x=950, y=y_btn, width=ancho_btn, height=alto_btn)
btn_eliminar_empresas.config(
    text='ELIMINAR', cursor='hand2', bg=color_btn_normal, fg='white',
    font=('Bold', 28), activebackground=color_btn_presion)

#ENTRIES
ancho = 310
alto = 80
x_col_izq = 300
x_col_der = 930
# izquierda ------------
mi_num_radicado_contrado = tk.StringVar()
num_radicado_entry_contrato = tk.Entry(
    contratos_frame, textvariable=mi_num_radicado_contrado, font=('Bold', 25))
num_radicado_entry_contrato.place(x=x_col_izq, y=240, width=ancho, height=alto)

mi_estado = tk.StringVar()
estado_entry_contratos = tk.Entry(contratos_frame, textvariable=mi_estado, font=('Bold', 25))
estado_entry_contratos.place(x=x_col_izq, y=340, width=ancho, height=alto)
# derecha --------------
nit_entry_contratos = tk.Entry(contratos_frame, textvariable=mi_nit, font=('Bold', 25))
nit_entry_contratos.place(x=x_col_der, y=240, width=ancho, height=alto)

mi_reporte_contratos = tk.StringVar()
reporte_entry_contratos = tk.Entry(contratos_frame, textvariable=mi_nombre_contacto, font=('Bold', 25))
reporte_entry_contratos.place(x=x_col_der, y=340, width=ancho, height=alto)

# LABELS
def etiquetas_contratos():
    title_label = tk.Label(
        contratos_frame, text='CONTRATOS', font=('Bold', 35), bg='#139a80', fg='white',
        anchor='center')
    title_label.place(x=520, y=70, width=300, height=60)
    
    ancho = 300  # original: 200
    alto = 80    # original: 40
    x_col_izq = 0   # original: 20
    x_col_der = 630   # original: 510
    # izquierda ------------
    num_radicado_label_contratos = tk.Label(
        contratos_frame, text='NÚMERO DE\n  RADICADO:', font=('Bold', 30), bg='#139a80', fg='white', anchor='e')
    num_radicado_label_contratos.place(x=x_col_izq, y=240, width=ancho, height=alto)

    estado_label_contratos = tk.Label(
        contratos_frame, text='ESTADO:', font=('Bold', 30), bg='#139a80', fg='white', anchor='e')
    estado_label_contratos.place(x=x_col_izq, y=340, width=ancho, height=alto)
    # derecha --------------
    nit_label_contratos = tk.Label(
        contratos_frame, text='NIT:', font=('Bold', 30), bg='#139a80', fg='white', anchor='e')
    nit_label_contratos.place(x=x_col_der, y=240, width=ancho, height=alto)

    reporte_label_contrato = tk.Label(
        contratos_frame, text='CÓDIGO DE\n   REPORTE:', font=('Bold', 30), bg='#139a80', fg='white', anchor='e')
    reporte_label_contrato.place(x=x_col_der, y=340, width=ancho, height=alto)

etiquetas_contratos()

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
# ---------------------------------- REPORTES FRAME -------------------------------------
reportes_frame = tk.Frame(main_frame, bg='#139a80')

aplicar_fondo(reportes_frame)

# BUTTONS
btn_reportes_to_second = tk.Button(reportes_frame)
btn_reportes_to_second.place(x=x_atras, y=y_atras, width=atras_ancho, height=atras_alto)
btn_reportes_to_second.config(
    text='ATRÁS', cursor='hand2', bg=color_btn_normal, fg='white',
    font=('Bold', 20), activebackground=color_btn_presion)

alto_btn = 100
ancho_btn = 310
y_btn = 540
btn_consultar_empresas = tk.Button(reportes_frame)
btn_consultar_empresas.place(x=20, y=y_btn, width=ancho_btn, height=alto_btn)
btn_consultar_empresas.config(
    text='CONSULTAR', cursor='hand2', bg=color_btn_normal, fg='white',
    font=('Bold', 30), activebackground=color_btn_presion)

btn_agregar_empresas = tk.Button(reportes_frame)
btn_agregar_empresas.place(x=330, y=y_btn, width=ancho_btn, height=alto_btn)
btn_agregar_empresas.config(
    text='AGREGAR', cursor='hand2', bg=color_btn_normal, fg='white',
    font=('Bold', 30), activebackground=color_btn_presion)

btn_guardar_empresas = tk.Button(reportes_frame)
btn_guardar_empresas.place(x=640, y=y_btn, width=ancho_btn, height=alto_btn)
btn_guardar_empresas.config(
    text='GUARDAR', cursor='hand2', bg=color_btn_normal, fg='white',
    font=('Bold', 30), activebackground=color_btn_presion)

btn_eliminar_empresas = tk.Button(reportes_frame)
btn_eliminar_empresas.place(x=950, y=y_btn, width=ancho_btn, height=alto_btn)
btn_eliminar_empresas.config(
    text='ELIMINAR', cursor='hand2', bg=color_btn_normal, fg='white',
    font=('Bold', 30), activebackground=color_btn_presion)

#ENTRIES
ancho = 810
alto = 80
x_col_der = 370   # original: 510

num_radicado_label_reportes = tk.StringVar()
num_radicado_entry_reportes = tk.Entry(
    reportes_frame, textvariable=mi_num_radicado_contrado, font=('Bold', 25))
num_radicado_entry_reportes.place(x=x_col_der, y=260, width=ancho, height=alto)

fecha_entry_reportes = tk.Entry(reportes_frame, textvariable=mi_estado, font=('Bold', 25))
fecha_entry_reportes.place(x=x_col_der, y=370, width=ancho, height=alto)

# LABELS
def etiquetas_reportes():
    title_label = tk.Label(
        reportes_frame, text='REPORTES', font=('Bold', 35), bg='#139a80', fg='white',
        anchor='center')
    title_label.place(x=520, y=70, width=300, height=60)
    
    ancho = 250
    alto = 80
    x_col_izq = 120
    
    num_radicado_label_reportes = tk.Label(
        reportes_frame, text='NÚMERO DE\n  RADICADO:', 
        font=('Bold', 30), bg='#139a80', fg='white', anchor='e')
    num_radicado_label_reportes.place(x=x_col_izq, y=260, width=ancho, height=alto)

    fecha_label_reportes = tk.Label(
        reportes_frame, text='FECHA DE\n    RETIRO:', 
        font=('Bold', 30), bg='#139a80', fg='white', anchor='e')
    fecha_label_reportes.place(x=x_col_izq, y=370, width=ancho, height=alto)

etiquetas_reportes()

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
# ------------------------------------ BANCO FRAME --------------------------------------
banco_frame = tk.Frame(main_frame, bg='#139a80')

aplicar_fondo(banco_frame)

# BUTTONS
btn_banco_to_home = tk.Button(banco_frame)
btn_banco_to_home.place(x=x_atras, y=y_atras, width=atras_ancho, height=atras_alto)
btn_banco_to_home.config(
    text='ATRÁS', cursor='hand2', bg=color_btn_normal, fg='white',
    font=('Bold', 20), activebackground=color_btn_presion)

# LABELS
def etiquetas_banco():
    title_label = tk.Label(
        banco_frame, text='BANCO', font=('Bold', 35), bg='#139a80', fg='white',
        anchor='center')
    title_label.place(x=520, y=70, width=300, height=60)
    
    ancho = 250
    alto = 80
    x_col_izq = 120
    
    num_radicado_label_reportes = tk.Label(
        banco_frame, text='      NIT DE\nEMPRESA:', 
        font=('Bold', 30), bg='#139a80', fg='white', anchor='e')
    num_radicado_label_reportes.place(x=x_col_izq, y=260, width=ancho, height=alto)

    fecha_label_reportes = tk.Label(
        banco_frame, text='       ID DE\nAFILIADO:', 
        font=('Bold', 30), bg='#139a80', fg='white', anchor='e')
    fecha_label_reportes.place(x=x_col_izq, y=370, width=ancho, height=alto)

etiquetas_banco()

def go_banco_to_home():
    try:
        banco_frame.pack_forget()
        home_frame.pack(fill=tk.BOTH, expand=True)
    except:
        print('ERROR al cambiar de frame')

def go_home_to_banco():
    try:
        home_frame.pack_forget()
        banco_frame.pack(fill=tk.BOTH, expand=True)
    except:
        print('ERROR al cambiar de frame')

btn_home_to_banco.config(command=go_home_to_banco)
btn_banco_to_home.config(command=go_banco_to_home)
# ------------------------------------- MAIN FRAME --------------------------------------
main_frame.pack(fill=tk.BOTH, expand=True)
# ---------------------------------------------------------------------------------------
root.mainloop()