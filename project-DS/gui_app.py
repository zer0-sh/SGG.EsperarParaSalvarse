import tkinter as tk
from tkinter import ttk, messagebox
from model.entidades import Afiliados, consultar, editar, agregar

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
root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

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

btn_consulta = tk.Button(admin_frame)
btn_consulta.place(x=990, y=120, width=270, height=130)
btn_consulta.config(
    text='CONSULTAR', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 28), activebackground='#35BD6F')

btn_nuevo = tk.Button(admin_frame)
btn_nuevo.place(x=990, y=270, width=270, height=130)
btn_nuevo.config(
    text='NUEVO', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 28), activebackground='#35BD6F')

btn_guardar = tk.Button(admin_frame)
btn_guardar.place(x=990, y=420, width=270, height=130)
btn_guardar.config(
    text='GUARDAR', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 28), activebackground='#35BD6F')

btn_eliminar = tk.Button(admin_frame)
btn_eliminar.place(x=990, y=570, width=270, height=130)
btn_eliminar.config(
    text='ELIMINAR', cursor='hand2', bg='#0a5245', fg='white',
    font=('Bold', 28), activebackground='#35BD6F')

# entries

mi_id = tk.StringVar()
id_entry = tk.Entry(admin_frame, textvariable=mi_id, font=('Bold', 20))
id_entry.place(x=220, y=150, width=200, height=40)

mi_nombre = tk.StringVar()
nombre_entry = tk.Entry(admin_frame, textvariable=mi_nombre, font=('Bold', 20))
nombre_entry.place(x=220, y=240, width=200, height=40)

mi_apellido = tk.StringVar()
apellido_entry = tk.Entry(admin_frame, textvariable=mi_apellido, font=('Bold', 20))
apellido_entry.place(x=220, y=330, width=200, height=40)

mi_genero = tk.StringVar()
genero_entry = tk.Entry(admin_frame, textvariable=mi_genero, font=('Bold', 20))
genero_entry.place(x=220, y=420, width=200, height=40)

mi_direccion = tk.StringVar()
direccion_entry = tk.Entry(admin_frame, textvariable=mi_direccion, font=('Bold', 20))
direccion_entry.place(x=220, y=510, width=200, height=40)

mi_email = tk.StringVar()
email_entry = tk.Entry(admin_frame, textvariable=mi_email, font=('Bold', 20))
email_entry.place(x=220, y=600, width=200, height=40)
#-------- der
mi_fecha = tk.StringVar()
f_nac_entry = tk.Entry(admin_frame, textvariable=mi_fecha, font=('Bold', 20))
f_nac_entry.place(x=710, y=150, width=200, height=40)

mi_estado_civil = tk.StringVar()
estado_civil_entry = tk.Entry(admin_frame, textvariable=mi_estado_civil, font=('Bold', 20))
estado_civil_entry.place(x=710, y=240, width=200, height=40)

mi_tipo_afil = tk.StringVar()
tipo_afil_entry = tk.Entry(admin_frame, textvariable=mi_tipo_afil, font=('Bold', 20))
tipo_afil_entry.place(x=710, y=330, width=200, height=40)

mi_telefono = tk.StringVar()
telefono_entry = tk.Entry(admin_frame, textvariable=mi_telefono, font=('Bold', 20))
telefono_entry.place(x=710, y=420, width=200, height=40)

mi_ciudad = tk.StringVar()
ciudad_entry = tk.Entry(admin_frame, textvariable=mi_ciudad, font=('Bold', 20))
ciudad_entry.place(x=710, y=510, width=200, height=40)

mi_ips = tk.StringVar()
ips_entry = tk.Entry(admin_frame, textvariable=mi_ips, font=('Bold', 20))
ips_entry.place(x=710, y=600, width=200, height=40)

def deshabilitar_entries():
    mi_id = None
    
    mi_nombre.set('')
    mi_apellido.set('')
    mi_genero.set('')
    mi_direccion.set('')
    mi_email.set('')
    mi_fecha.set('')
    mi_estado_civil.set('')
    mi_tipo_afil.set('')
    mi_telefono.set('')
    mi_ciudad.set('')
    mi_ips.set('')
    
    
    id_entry.config(state='normal')
    nombre_entry.config(state='disabled')
    apellido_entry.config(state='disabled')
    genero_entry.config(state='disabled')
    direccion_entry.config(state='disabled')
    email_entry.config(state='disabled')
    f_nac_entry.config(state='disabled')
    estado_civil_entry.config(state='disabled')
    tipo_afil_entry.config(state='disabled')
    telefono_entry.config(state='disabled')
    ciudad_entry.config(state='disabled')
    ips_entry.config(state='disabled')
    
    btn_guardar.config(state='disabled')
# labels
def etiquetas():
    admin_label = tk.Label(
        admin_frame, text='ADMINISTRADOR', font=('Bold', 30), bg='#139a80', fg='white',
        anchor='s')
    admin_label.place(x=450, y=40, width=350, height=50)

    id_label = tk.Label(
        admin_frame, text='ID:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    id_label.place(x=20, y=150, width=200, height=40)

    nombre_label = tk.Label(
        admin_frame, text='NOMBRE:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    nombre_label.place(x=20, y=240, width=200, height=40)

    apellido_label = tk.Label(
        admin_frame, text='APELLIDO:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    apellido_label.place(x=20, y=330, width=200, height=40)

    genero_label = tk.Label(
        admin_frame, text='GÉNERO:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    genero_label.place(x=20, y=420, width=200, height=40)

    direccion_label = tk.Label(
        admin_frame, text='DIRECCIÓN:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    direccion_label.place(x=20, y=510, width=200, height=40)

    email_label = tk.Label(
        admin_frame, text='EMAIL:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    email_label.place(x=20, y=600, width=200, height=40)
    #-------- der
    f_nac_label = tk.Label(
        admin_frame, text='FECHA NAC:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    f_nac_label.place(x=510, y=150, width=200, height=40)

    estado_civil_label = tk.Label(
        admin_frame, text='ESTADO CIVIL:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    estado_civil_label.place(x=510, y=240, width=200, height=40)

    tipo_afil_label = tk.Label(
        admin_frame, text='TIPO DE AFIL:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    tipo_afil_label.place(x=510, y=330, width=200, height=40)

    telefono_label = tk.Label(
        admin_frame, text='TELÉFONO:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    telefono_label.place(x=510, y=420, width=200, height=40)

    ciudad_label = tk.Label(
        admin_frame, text='CIUDAD:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    ciudad_label.place(x=510, y=510, width=200, height=40)

    ips_label = tk.Label(
        admin_frame, text='IPS:', font=('Bold', 20), bg='#139a80', fg='white', anchor='e')
    ips_label.place(x=510, y=600, width=200, height=40)

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
        
        messagebox.showinfo('Consulta', resultado)
    except:
        messagebox.showerror('ERROR', 'Valor erroneo en la \'primary key\'')

def habilitar_campos():
    deshabilitar_entries()
    
    nombre_entry.config(state='normal')
    apellido_entry.config(state='normal')
    genero_entry.config(state='normal')
    direccion_entry.config(state='normal')
    email_entry.config(state='normal')
    f_nac_entry.config(state='normal')
    estado_civil_entry.config(state='normal')
    tipo_afil_entry.config(state='normal')
    telefono_entry.config(state='normal')
    ciudad_entry.config(state='normal')
    ips_entry.config(state='normal')
    
    btn_guardar.config(state='normal')

def guardar_datos():
    
    obj_afiliado = Afiliados(
        mi_nombre.get(), mi_apellido.get(), mi_genero.get(), mi_direccion.get(),
        mi_email.get(), mi_fecha.get(), mi_estado_civil.get(), mi_tipo_afil.get(),
        mi_telefono.get(), mi_ciudad.get(), mi_ips.get()
    )
    
    if mi_id.get() == '':
        agregar(obj_afiliado)
    else:
        editar(obj_afiliado, mi_id)

btn_consulta.config(command=listar)
btn_nuevo.config(command=habilitar_campos)
btn_guardar.config(command=guardar_datos)
# --------------------------- MAIN FRAME ----------------------------
main_frame.pack(fill=tk.BOTH, expand=True)
# -------------------------------------------------------------------
root.mainloop()