import tkinter as tk
import sqlite3

# Crear la ventana
ventana = tk.Tk()
ventana.title("Ejemplo de conexión a SQLite")

# Función para conectar a la base de datos SQLite
def conectar_db():
    try:
        # Establecer la conexión a la base de datos
        conexion = sqlite3.connect("mi_base_de_datos.db")
        print("Conexión a la base de datos establecida correctamente.")
        # Aquí puedes realizar operaciones con la base de datos
        # Por ejemplo, crear una tabla:
        cursor = conexion.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER)")
        conexion.commit()
        print("Tabla creada correctamente.")
        # Cerrar la conexión cuando hayas terminado
        conexion.close()
    except sqlite3.Error as error:
        print("Error al conectar a la base de datos:", error)

# Crear un botón para conectar a la base de datos
boton_conectar = tk.Button(ventana, text="Conectar a la base de datos", command=conectar_db)
boton_conectar.pack(padx=10, pady=5)

# Ejecutar el bucle de eventos
ventana.mainloop()