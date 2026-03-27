"""
This module is for nostalgic collections management system
@version 1.0.0
@author Laidy Hurtado
"""

import tkinter as tk
from tkinter import messagebox

# -----------------------------
# BASE DE DATOS (memoria)
# -----------------------------
"""
stores users, collections and objects in memory
Estoy documentando las estructuras principales
"""
usuarios = []
colecciones = []
objetos = []
usuario_actual = None

# -----------------------------
# FUNCIONES USUARIO
# -----------------------------
def registrar():
    """
    This function registers a new user
    Estoy documentando la función de registro
    """
    username = entry_user.get()
    password = entry_pass.get()
    rol = "Administrador" if username.lower() == "admin" else "Usuario"

    if username == "" or password == "":
        messagebox.showerror("Error", "Campos vacíos")
        return

    for u in usuarios:
        if u["username"] == username:
            messagebox.showerror("Error", "Usuario ya existe")
            return

    usuarios.append({
        "id": len(usuarios) + 1,
        "username": username,
        "password": password,
        "rol": rol
    })

    messagebox.showinfo("Éxito", "Usuario registrado")
    limpiar_campos()


def login():
    """
    This function validates user credentials
    Estoy documentando el inicio de sesión
    """
    global usuario_actual

    username = entry_user.get()
    password = entry_pass.get()

    for u in usuarios:
        if u["username"] == username and u["password"] == password:
            usuario_actual = u
            messagebox.showinfo("Bienvenido", f"Hola {username}")
            abrir_panel_usuario()
            return

    messagebox.showerror("Error", "Credenciales incorrectas")


# -----------------------------
# PANEL USUARIO
# -----------------------------
def abrir_panel_usuario():
    """
    This function opens the user panel window
    Estoy documentando el panel principal del usuario
    """
    panel = tk.Toplevel(root)
    panel.title("Panel de Usuario")
    panel.geometry("300x350")

    tk.Label(panel, text=f"Bienvenido {usuario_actual['username']}").pack(pady=10)

    tk.Button(panel, text="Crear Colección", command=crear_coleccion).pack(pady=5)
    tk.Button(panel, text="Ver Mis Colecciones", command=ver_colecciones).pack(pady=5)

    tk.Button(panel, text="Agregar Objeto", command=agregar_objeto).pack(pady=5)
    tk.Button(panel, text="Ver Objetos", command=ver_objetos).pack(pady=5)

    if usuario_actual["rol"] == "Administrador":
        tk.Button(panel, text="Ver Usuarios", command=mostrar_usuarios).pack(pady=5)

    tk.Button(panel, text="Cerrar Sesión", command=panel.destroy).pack(pady=10)


# -----------------------------
# COLECCIONES
# -----------------------------
def crear_coleccion():
    ventana = tk.Toplevel(root)
    ventana.title("Nueva Colección")

    tk.Label(ventana, text="Nombre de la colección").pack()
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack()

    def guardar():
        nombre = entry_nombre.get()

        if nombre == "":
            messagebox.showerror("Error", "Nombre vacío")
            return

        colecciones.append({
            "usuario": usuario_actual["username"],
            "nombre": nombre
        })

        messagebox.showinfo("Éxito", "Colección creada")
        ventana.destroy()

    tk.Button(ventana, text="Guardar", command=guardar).pack(pady=5)


def ver_colecciones():
    ventana = tk.Toplevel(root)
    ventana.title("Mis Colecciones")

    lista = [c for c in colecciones if c["usuario"] == usuario_actual["username"]]

    if not lista:
        tk.Label(ventana, text="No tienes colecciones").pack()
        return

    for c in lista:
        tk.Label(ventana, text=f"Colección: {c['nombre']}").pack()


# -----------------------------
# OBJETOS
# -----------------------------
def agregar_objeto():
    ventana = tk.Toplevel(root)
    ventana.title("Agregar Objeto")

    tk.Label(ventana, text="Nombre del objeto").pack()
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack()

    tk.Label(ventana, text="Descripción").pack()
    entry_desc = tk.Entry(ventana)
    entry_desc.pack()

    tk.Label(ventana, text="Colección").pack()
    entry_col = tk.Entry(ventana)
    entry_col.pack()

    def guardar():
        nombre = entry_nombre.get()
        desc = entry_desc.get()
        coleccion = entry_col.get()

        if nombre == "" or coleccion == "":
            messagebox.showerror("Error", "Campos obligatorios")
            return

        objetos.append({
            "id": len(objetos) + 1,
            "nombre": nombre,
            "descripcion": desc,
            "coleccion": coleccion,
            "usuario": usuario_actual["username"]
        })

        messagebox.showinfo("Éxito", "Objeto agregado")
        ventana.destroy()

    tk.Button(ventana, text="Guardar", command=guardar).pack(pady=5)


def ver_objetos():
    ventana = tk.Toplevel(root)
    ventana.title("Mis Objetos")

    lista = [o for o in objetos if o["usuario"] == usuario_actual["username"]]

    if not lista:
        tk.Label(ventana, text="No tienes objetos").pack()
        return

    for o in lista:
        texto = f"{o['nombre']} ({o['coleccion']})"
        tk.Label(ventana, text=texto).pack()


# -----------------------------
# ADMIN
# -----------------------------
def mostrar_usuarios():
    ventana_lista = tk.Toplevel(root)
    ventana_lista.title("Lista de Usuarios")

    for u in usuarios:
        texto = f"ID: {u['id']} | Usuario: {u['username']} | Rol: {u['rol']}"
        tk.Label(ventana_lista, text=texto).pack()


# -----------------------------
# UTILIDADES
# -----------------------------
def limpiar_campos():
    entry_user.delete(0, tk.END)
    entry_pass.delete(0, tk.END)


# -----------------------------
# INTERFAZ PRINCIPAL
# -----------------------------
root = tk.Tk()
root.title("Gestión de Colecciones Nostálgicas")
root.geometry("300x200")

tk.Label(root, text="Usuario").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Contraseña").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Registrar", command=registrar).pack(pady=5)
tk.Button(root, text="Iniciar Sesión", command=login).pack(pady=5)

root.mainloop()

# -----------------------------
# OBJETOS
# -----------------------------
def agregar_objeto():
    """
    This function adds a new object
    Estoy documentando la creación de objetos
    """
    ventana = tk.Toplevel(root)
    ventana.title("Agregar Objeto")

    tk.Label(ventana, text="Nombre del objeto").pack()
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack()

    tk.Label(ventana, text="Descripción").pack()
    entry_desc = tk.Entry(ventana)
    entry_desc.pack()

    tk.Label(ventana, text="Colección").pack()
    entry_col = tk.Entry(ventana)
    entry_col.pack()

    def guardar():
        """
        This function saves an object
        Estoy documentando el guardado del objeto
        """
        nombre = entry_nombre.get()
        desc = entry_desc.get()
        coleccion = entry_col.get()

        if nombre == "" or coleccion == "":
            messagebox.showerror("Error", "Campos obligatorios")
            return

        objetos.append({
            "id": len(objetos) + 1,
            "nombre": nombre,
            "descripcion": desc,
            "coleccion": coleccion,
            "usuario": usuario_actual["username"]
        })

        messagebox.showinfo("Éxito", "Objeto agregado")
        ventana.destroy()

    tk.Button(ventana, text="Guardar", command=guardar).pack(pady=5)


def ver_objetos():
    """
    This function shows user objects
    Estoy documentando la visualización de objetos
    """
    ventana = tk.Toplevel(root)
    ventana.title("Mis Objetos")

    lista = [o for o in objetos if o["usuario"] == usuario_actual["username"]]

    if not lista:
        tk.Label(ventana, text="No tienes objetos").pack()
        return

    for o in lista:
        texto = f"{o['nombre']} ({o['coleccion']})"
        tk.Label(ventana, text=texto).pack()


# -----------------------------
# ADMIN
# -----------------------------
def mostrar_usuarios():
    """
    This function shows all users (admin only)
    Estoy documentando la lista de usuarios
    """
    ventana_lista = tk.Toplevel(root)
    ventana_lista.title("Lista de Usuarios")

    for u in usuarios:
        texto = f"ID: {u['id']} | Usuario: {u['username']} | Rol: {u['rol']}"
        tk.Label(ventana_lista, text=texto).pack()


# -----------------------------
# UTILIDADES
# -----------------------------
def limpiar_campos():
    """
    This function clears input fields
    Estoy documentando la limpieza de campos
    """
    entry_user.delete(0, tk.END)
    entry_pass.delete(0, tk.END)


# -----------------------------
# INTERFAZ PRINCIPAL
# -----------------------------
"""
This section creates the main interface
Estoy documentando la ventana principal
"""
root = tk.Tk()
root.title("Gestión de Colecciones Nostálgicas")
root.geometry("300x200")

tk.Label(root, text="Usuario").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Contraseña").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Registrar", command=registrar).pack(pady=5)
tk.Button(root, text="Iniciar Sesión", command=login).pack(pady=5)

root.mainloop()
