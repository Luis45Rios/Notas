from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

nombre_db = "notas.db"

ventana = Tk()
ventana.title("Bloc de Notas")
ventana.iconbitmap("notes.ico")

lbl_nombre_app = Label(ventana, text="MIS NOTAS",
                       bg="#000", fg="#fff", font="Arial 60")
lbl_nombre_app.grid(row=0, column=1, padx=10, pady=20)

tabla_notas = ttk.Treeview(ventana, columns=("Titulo", "Nota"))

tabla_notas.heading("#0", text="ID")
tabla_notas.heading("#1", text="Titulo")
tabla_notas.heading("#2", text="Contenido")

tabla_notas.column("#0", width=50)
tabla_notas.column("#1", width=200)
tabla_notas.column("#2", width=600)

tabla_notas.grid(row=1, column=1)

# FUNCIONES

# Funcion AGREGAR


def vent_agregar():
    ventana1 = Toplevel(ventana)
    ventana1.title("Agregar Nota")

    lbl_titulo = Label(ventana1, text="Nombre de la Nota: ")
    lbl_titulo.grid(row=1, column=1)
    entry_titulo = Entry(ventana1)
    entry_titulo.grid(row=1, column=2)

    nota_contenido = Label(ventana1, text="Contenido: ")
    nota_contenido.grid(row=2, column=1)
    entry_contenido = Entry(ventana1)
    entry_contenido.grid(row=2, column=2)

    def añadir_nota():
        titulo = entry_titulo.get()
        contenido = entry_contenido.get()
        tabla_notas.insert("", "end", values=(titulo, contenido,))
    btn_añadirNota = Button(ventana1, text="Añadir nota", command=añadir_nota)
    btn_añadirNota.grid(row=3, column=1, sticky=W+E)

# Funcion ELIMINAR


def eliminar():
    try:
        item_seleccionado = tabla_notas.selection()[0]
        tabla_notas.delete(item_seleccionado)
    except IndexError as e:
        print("Seleccione una nota")
        
def conectar_db():
    conexion = sqlite3.connect(nombre_db)
    cursos= conexion.cursor()

# BOTONES


# BOTON AGREGAR
btn_agregar = Button(ventana, text="Agregar Nota", command=vent_agregar)
btn_agregar.grid(row=2, column=1, padx=5, pady=5, columnspan=2, sticky=W)

# BOTON ELIMINAR
btn_eliminar = Button(ventana, text="Eliminar", command=eliminar)
btn_eliminar.grid(row=2, column=1, padx=5, pady=5, columnspan=2, sticky=E)

ventana.mainloop()
