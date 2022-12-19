import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from model.entidades import Beneficiarios, Dependientes, Independientes, consultar, editar, agregar_beneficiario

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
    deshabilitar_entries()
    try:
        home_frame.pack_forget()
        second_frame.pack(fill=tk.BOTH, expand=True)
    except:
        print('ERROR al cambiar de frame')

def go_second_to_home():
    deshabilitar_entries()
    try:
        second_frame.pack_forget()
        home_frame.pack(fill=tk.BOTH, expand=True)
    except:
        print('ERROR al cambiar de frame')

btn_home_to_admin.config(command=go_home_to_second)
btn_second_to_home.config(command=go_second_to_home)
# --------------------------- ADMIN FRAME ---------------------------
admin_frame = tk.Frame(main_frame, bg='#139a80')
# buttons
btn_admin_to_second = tk.Button(admin_frame)
btn_admin_to_second.place(relx=0.01, rely=0.01, relwidth=0.16, relheight=0.05)
btn_admin_to_second.config(
    text='ATRÁS', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 10), activebackground='#35BD6F')
alto_btn = 90    # original: 130
ancho_btn = 320  # original: 280
x_btn = 940      # original: 980
btn_consulta = tk.Button(admin_frame)
btn_consulta.place(x=x_btn, y=100, width=ancho_btn, height=alto_btn)
btn_consulta.config(
    text='CONSULTAR', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 28), activebackground='#35BD6F')

btn_nuevo_beneficiario = tk.Button(admin_frame)
btn_nuevo_beneficiario.place(x=x_btn, y=200, width=ancho_btn, height=alto_btn)
btn_nuevo_beneficiario.config(
    text='NUEVO\nBENEFICIARIO', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 28), activebackground='#35BD6F')

btn_nuevo_dependiente = tk.Button(admin_frame)
btn_nuevo_dependiente.place(x=x_btn, y=300, width=ancho_btn, height=alto_btn)
btn_nuevo_dependiente.config(
    text='NUEVO\nDEPENDIENTE', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 28), activebackground='#35BD6F')

btn_nuevo_independiente = tk.Button(admin_frame)
btn_nuevo_independiente.place(x=x_btn, y=400, width=ancho_btn, height=alto_btn)
btn_nuevo_independiente.config(
    text='NUEVO\nINDEPENDIENTE', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 28), activebackground='#35BD6F')

btn_guardar = tk.Button(admin_frame)
btn_guardar.place(x=x_btn, y=500, width=ancho_btn, height=alto_btn)
btn_guardar.config(
    text='GUARDAR', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 28), activebackground='#35BD6F')

btn_eliminar = tk.Button(admin_frame)
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
id_entry = tk.Entry(admin_frame, textvariable=mi_id, font=('Bold', 20))
id_entry.place(x=x_col_izq, y=100, width=ancho, height=alto)

mi_nombre = tk.StringVar()
nombre_entry = tk.Entry(admin_frame, textvariable=mi_nombre, font=('Bold', 20))
nombre_entry.place(x=x_col_izq, y=150, width=ancho, height=alto)

mi_apellido = tk.StringVar()
apellido_entry = tk.Entry(admin_frame, textvariable=mi_apellido, font=('Bold', 20))
apellido_entry.place(x=x_col_izq, y=200, width=ancho, height=alto)

mi_genero = tk.StringVar()
genero_entry = tk.OptionMenu(admin_frame, mi_genero, *['Masculino', 'Femenino'])
genero_entry.place(x=x_col_izq, y=250, width=ancho, height=alto)

mi_direccion = tk.StringVar()
direccion_entry = tk.Entry(admin_frame, textvariable=mi_direccion, font=('Bold', 20))
direccion_entry.place(x=x_col_izq, y=300, width=ancho, height=alto)

mi_email = tk.StringVar()
email_entry = tk.Entry(admin_frame, textvariable=mi_email, font=('Bold', 20))
email_entry.place(x=x_col_izq, y=350, width=ancho, height=alto)

mi_fecha_nacimiento = tk.StringVar()
fecha_nac_dateentry = DateEntry(admin_frame, textvariable=mi_fecha_nacimiento, font=('Bold', 20))
fecha_nac_dateentry.place(x=x_col_izq, y=400, width=ancho, height=alto)

mi_estado_civil = tk.StringVar()
estado_civil_entry = tk.OptionMenu(admin_frame, mi_estado_civil, *['Soltero', 'Casado', 'Union Libre'])
estado_civil_entry.place(x=x_col_izq, y=450, width=ancho, height=alto)

mi_tipo_afil = tk.StringVar()
tipo_afil_entry = tk.OptionMenu(admin_frame, mi_tipo_afil, *['Cotizante', 'Beneficiario'])
tipo_afil_entry.place(x=x_col_izq, y=500, width=ancho, height=alto)

mi_telefono = tk.StringVar()
telefono_entry = tk.Entry(admin_frame, textvariable=mi_telefono, font=('Bold', 20))
telefono_entry.place(x=x_col_izq, y=550, width=ancho, height=alto)

mi_ciudad = tk.StringVar()
ciudad_entry = tk.Entry(admin_frame, textvariable=mi_ciudad, font=('Bold', 20))
ciudad_entry.place(x=x_col_izq, y=600, width=ancho, height=alto)

mi_ips = tk.StringVar()
ips_entry = tk.OptionMenu(admin_frame, mi_ips, *['40001', '40002', '40003', '40004', '40005'])
ips_entry.place(x=x_col_izq, y=650, width=ancho, height=alto)

#-------- COLUMNA DERRECHA
mi_ordenes = tk.StringVar()
ordenes_entry = tk.OptionMenu(admin_frame, mi_ordenes, *['20001', '20002', '20003', '20004', '20005', '20006'])
ordenes_entry.place(x=x_col_der, y=100, width=ancho, height=alto)

mi_parentesco = tk.StringVar()
parentesco_entry = tk.OptionMenu(
    admin_frame, mi_parentesco, *['Cónyuge', 'Padre', 'Madre', 'Hijo', 'Hermanos', 'Amigos'])
parentesco_entry.place(x=x_col_der, y=150, width=ancho, height=alto)

mi_cotizante = tk.StringVar()
cotizante_entry = tk.Entry(admin_frame, textvariable=mi_cotizante, font=('Bold', 20))
cotizante_entry.place(x=x_col_der, y=200, width=ancho, height=alto)

mi_salario = tk.StringVar()
salario_entry = tk.Entry(admin_frame, textvariable=mi_salario, font=('Bold', 20))
salario_entry.place(x=x_col_der, y=250, width=ancho, height=alto)

mi_estado_afiliacion = tk.StringVar()
estado_afil_entry = tk.OptionMenu(admin_frame, mi_estado_afiliacion, *['Activo', 'Retirado', 'Inactivo'])
estado_afil_entry.place(x=x_col_der, y=300, width=ancho, height=alto)

mi_fecha_afiliacion = tk.StringVar()
fecha_afil_dateentry = DateEntry(admin_frame, textvariable=mi_fecha_afiliacion, font=('Bold', 20))
fecha_afil_dateentry.place(x=x_col_der, y=350, width=ancho, height=alto)

mi_rango_salarial = tk.StringVar()
rango_salarial_entry = tk.OptionMenu(admin_frame, mi_rango_salarial, *['A', 'B', 'C'])
rango_salarial_entry.place(x=x_col_der, y=400, width=ancho, height=alto)

mi_estado = tk.StringVar()
estado_entry = tk.OptionMenu(admin_frame, mi_estado, *['Activo', 'Inactivo'])
estado_entry.place(x=x_col_der, y=450, width=ancho, height=alto)

mi_nombre_empresa = tk.StringVar()
nombre_empresa_entry = tk.Entry(admin_frame, textvariable=mi_nombre_empresa, font=('Bold', 20))
nombre_empresa_entry.place(x=x_col_der, y=500, width=ancho, height=alto)

mi_rut = tk.StringVar()
rut_entry = tk.Entry(admin_frame, textvariable=mi_rut, font=('Bold', 20))
rut_entry.place(x=x_col_der, y=550, width=ancho, height=alto)

mi_contrato = tk.StringVar()
contrato_entry = tk.OptionMenu(admin_frame, mi_contrato, *['60001', '60002', '60003', '60004', '60005', '60006'])
contrato_entry.place(x=x_col_der, y=600, width=ancho, height=alto)

def deshabilitar_entries():
    mi_id = None
    
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

# Labels
def etiquetas():
    ancho = 220  # original: 200
    alto = 40    # original: 40
    x_col_izq = 0   # original: 20
    x_col_der = 470  # original: 510
    title_label = tk.Label(
        admin_frame, text='AFILIADOS', font=('Bold', 40), bg='#139a80', fg='white',
        anchor='s')
    title_label.place(x=450, y=20, width=300, height=60)

    id_label = tk.Label(
        admin_frame, text='ID:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    id_label.place(x=x_col_izq, y=100, width=ancho, height=alto)

    nombre_label = tk.Label(
        admin_frame, text='NOMBRE:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    nombre_label.place(x=x_col_izq, y=150, width=ancho, height=alto)

    apellido_label = tk.Label(
        admin_frame, text='APELLIDO:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    apellido_label.place(x=x_col_izq, y=200, width=ancho, height=alto)

    genero_label = tk.Label(
        admin_frame, text='GÉNERO:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    genero_label.place(x=x_col_izq, y=250, width=ancho, height=alto)

    direccion_label = tk.Label(
        admin_frame, text='DIRECCIÓN:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    direccion_label.place(x=x_col_izq, y=300, width=ancho, height=alto)

    email_label = tk.Label(
        admin_frame, text='EMAIL:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    email_label.place(x=x_col_izq, y=350, width=ancho, height=alto)

    fecha_nac_label = tk.Label(
        admin_frame, text='FECHA NAC:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    fecha_nac_label.place(x=x_col_izq, y=400, width=ancho, height=alto)

    estado_civil_label = tk.Label(
        admin_frame, text='ESTADO CIVIL:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    estado_civil_label.place(x=x_col_izq, y=450, width=ancho, height=alto)

    tipo_afil_label = tk.Label(
        admin_frame, text='TIPO DE AFIL:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    tipo_afil_label.place(x=x_col_izq, y=500, width=ancho, height=alto)

    telefono_label = tk.Label(
        admin_frame, text='TELÉFONO:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    telefono_label.place(x=x_col_izq, y=550, width=ancho, height=alto)
    
    ciudad_label = tk.Label(
        admin_frame, text='CIUDAD:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    ciudad_label.place(x=x_col_izq, y=600, width=ancho, height=alto)

    ips_label = tk.Label(
        admin_frame, text='IPS:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    ips_label.place(x=x_col_izq, y=650, width=ancho, height=alto)
        
    #-------- COLUMNA DERECHA
    ordenes_label = tk.Label(
        admin_frame, text='ORDENES:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    ordenes_label.place(x=x_col_der, y=100, width=ancho, height=alto)
    
    parentesco_label = tk.Label(
        admin_frame, text='PARENTESCO:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    parentesco_label.place(x=x_col_der, y=150, width=ancho, height=alto)
    
    beneficiario_label = tk.Label(
        admin_frame, text='BENEFICIARIO:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    beneficiario_label.place(x=x_col_der, y=200, width=ancho, height=alto)
    
    salario_label = tk.Label(
        admin_frame, text='SALARIO:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    salario_label.place(x=x_col_der, y=250, width=ancho, height=alto)
    
    estado_afil_label = tk.Label(
        admin_frame, text='ESTADO AFIL:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    estado_afil_label.place(x=x_col_der, y=300, width=ancho, height=alto)
    
    fecha_afil_label = tk.Label(
        admin_frame, text='FECHA AFIL:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    fecha_afil_label.place(x=x_col_der, y=350, width=ancho, height=alto)
    
    rango_salarial_label = tk.Label(
        admin_frame, text='RAN SALARIAL:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    rango_salarial_label.place(x=x_col_der, y=400, width=ancho, height=alto)
   
    estado_label = tk.Label(
        admin_frame, text='ESTADO:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    estado_label.place(x=x_col_der, y=450, width=ancho, height=alto)
    
    nombre_empresa_label = tk.Label(
        admin_frame, text='NOM EMPRESA:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    nombre_empresa_label.place(x=x_col_der, y=500, width=ancho, height=alto)
    
    rut_label = tk.Label(
        admin_frame, text='RUT:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    rut_label.place(x=x_col_der, y=550, width=ancho, height=alto)
    
    contrato_label = tk.Label(
        admin_frame, text='CONTRATO:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    contrato_label.place(x=x_col_der, y=600, width=ancho, height=alto)
    
etiquetas()

def go_second_to_admin():
    deshabilitar_entries()
    try:
        second_frame.pack_forget()
        admin_frame.pack(fill=tk.BOTH, expand=True)
    except:
        print('ERROR al cambiar de frame')

def go_admin_to_second():
    deshabilitar_entries()
    try:
        admin_frame.pack_forget()
        second_frame.pack(fill=tk.BOTH, expand=True)
    except:
        print('ERROR al cambiar de frame')

btn_second_to_gestionar_afil.config(command=go_second_to_admin)
btn_admin_to_second.config(command=go_admin_to_second)

def listar():
    print(f'-----> opcion genero: {mi_fecha_nacimiento.get()}, type: {type(mi_fecha_nacimiento.get())}')
    deshabilitar_entries()
    # recupero el array haciendo el llamado
    llave = str(mi_id.get())
    try:
        afiliado = consultar(llave)
        resultado = f"""
        id = {afiliado[0][0]}
        nombre = {afiliado[0][1]}
        apellido = {afiliado[0][2]}
        genero = {afiliado[0][3]}
        direccion = {afiliado[0][4]}
        email = {afiliado[0][5]}
        fecha de nacimiento = {afiliado[0][6]}
        estado civil = {afiliado[0][7]}
        tipo afiliacion = {afiliado[0][8]}
        telefono = {afiliado[0][9]}
        ciudad = {afiliado[0][10]}
        ips = {afiliado[0][11]}
        """
        
        messagebox.showinfo('Consulta de Afiliado', resultado)
    except Exception as ex:
        messagebox.showerror('Fallo al listar', f'{ex}.')

def habilitar_campos_beneficiario():
    deshabilitar_entries()

    nombre_entry.config(state='normal', bg='white')
    apellido_entry.config(state='normal', bg='white')
    genero_entry.config(state='normal', bg='white')
    direccion_entry.config(state='normal', bg='white')
    email_entry.config(state='normal', bg='white')
    fecha_nac_dateentry.config(state='normal')
    estado_civil_entry.config(state='normal', bg='white')
    tipo_afil_entry.config(state='normal', bg='white')
    telefono_entry.config(state='normal', bg='white')
    ciudad_entry.config(state='normal', bg='white')
    ips_entry.config(state='normal', bg='white')
    ordenes_entry.config(state='normal', bg='white')
    parentesco_entry.config(state='normal', bg='white')
    cotizante_entry.config(state='normal', bg='white')
    #salario_entry.config(state='normal')
    #estado_afil_entry.config(state='normal')
    #fecha_afil_dateentry.config(state='normal')
    #rango_salarial_entry.config(state='normal')
    #estado_entry.config(state='normal')
    #nombre_empresa_entry.config(state='normal')
    #rut_entry.config(state='normal')
    #contrato_entry.config(state='normal')
    
    btn_guardar.config(state='normal')

def habilitar_campos_dependiente():
    deshabilitar_entries()
    
    nombre_entry.config(state='normal', bg='white')
    apellido_entry.config(state='normal', bg='white')
    genero_entry.config(state='normal', bg='white')
    direccion_entry.config(state='normal', bg='white')
    email_entry.config(state='normal', bg='white')
    fecha_nac_dateentry.config(state='normal')
    estado_civil_entry.config(state='normal', bg='white')
    tipo_afil_entry.config(state='normal', bg='white')
    telefono_entry.config(state='normal', bg='white')
    ciudad_entry.config(state='normal', bg='white')
    ips_entry.config(state='normal', bg='white')
    ordenes_entry.config(state='normal', bg='white')
    #parentesco_entry.config(state='normal')
    #cotizante_entry.config(state='normal', bg='white')
    salario_entry.config(state='normal', bg='white')
    estado_afil_entry.config(state='normal', bg='white')
    fecha_afil_dateentry.config(state='normal')
    rango_salarial_entry.config(state='normal', bg='white')
    estado_entry.config(state='normal', bg='white')
    #nombre_empresa_entry.config(state='normal')
    #rut_entry.config(state='normal')
    #contrato_entry.config(state='normal')
    
    btn_guardar.config(state='normal')

def habilitar_campos_independiente():
    deshabilitar_entries()
    
    nombre_entry.config(state='normal', bg='white')
    apellido_entry.config(state='normal', bg='white')
    genero_entry.config(state='normal', bg='white')
    direccion_entry.config(state='normal', bg='white')
    email_entry.config(state='normal', bg='white')
    fecha_nac_dateentry.config(state='normal')
    estado_civil_entry.config(state='normal', bg='white')
    tipo_afil_entry.config(state='normal', bg='white')
    telefono_entry.config(state='normal', bg='white')
    ciudad_entry.config(state='normal', bg='white')
    ips_entry.config(state='normal', bg='white')
    ordenes_entry.config(state='normal', bg='white')
    #parentesco_entry.config(state='normal')
    #cotizante_entry.config(state='normal', bg='white')
    salario_entry.config(state='normal', bg='white')
    estado_afil_entry.config(state='normal', bg='white')
    fecha_afil_dateentry.config(state='normal')
    rango_salarial_entry.config(state='normal', bg='white')
    #estado_entry.config(state='normal')
    nombre_empresa_entry.config(state='normal', bg='white')
    rut_entry.config(state='normal', bg='white')
    contrato_entry.config(state='normal', bg='white')
    
    btn_guardar.config(state='normal')

def guardar_datos():
    
    obj_beneficiario = Beneficiarios(
        mi_nombre.get(), mi_apellido.get(), mi_genero.get(), mi_direccion.get(),
        mi_email.get(), fecha_nac_dateentry.get_date(), mi_estado_civil.get(),
        mi_tipo_afil.get(), mi_telefono.get(), mi_ciudad.get(), mi_ips.get(),
        mi_ordenes.get(), mi_parentesco.get(), mi_cotizante.get()
    )
    
    obj_dependiente = Dependientes(
        mi_nombre.get(), mi_apellido.get(), mi_genero.get(), mi_direccion.get(),
        mi_email.get(), fecha_nac_dateentry.get_date(), mi_estado_civil.get(),
        mi_tipo_afil.get(), mi_telefono.get(), mi_ciudad.get(), mi_ips.get(),
        mi_ordenes.get(), mi_salario.get, mi_estado_afiliacion.get(),
        fecha_afil_dateentry.get_date(), mi_rango_salarial.get(), mi_estado.get()
    )
    
    obj_independiente = Independientes(
        mi_nombre.get(), mi_apellido.get(), mi_genero.get(), mi_direccion.get(),
        mi_email.get(), fecha_nac_dateentry.get_date(), mi_estado_civil.get(),
        mi_tipo_afil.get(), mi_telefono.get(), mi_ciudad.get(), mi_ips.get(),
        mi_ordenes.get(), mi_salario.get, mi_estado_afiliacion.get(),
        fecha_afil_dateentry.get_date(), mi_rango_salarial.get(), 
        mi_nombre_empresa.get(), mi_rut.get(), mi_contrato.get()
    )
    
    if mi_id.get() == '':
        agregar_beneficiario(obj_beneficiario)
    else:
        editar(obj_beneficiario, mi_id)

btn_consulta.config(command=listar)
btn_nuevo_beneficiario.config(command=habilitar_campos_beneficiario)
btn_nuevo_dependiente.config(command=habilitar_campos_dependiente)
btn_nuevo_independiente.config(command=habilitar_campos_independiente)
btn_guardar.config(command=guardar_datos)
# --------------------------- MAIN FRAME ----------------------------
main_frame.pack(fill=tk.BOTH, expand=True)
# -------------------------------------------------------------------
root.mainloop()