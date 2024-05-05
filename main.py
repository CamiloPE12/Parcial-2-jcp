from flask import Flask, render_template, redirect
import sqlite3
# aplicación
app = Flask(__name__)

# Rutas
@app.route('/')
def ruta_raiz():
    try:
        # Establecer la conexión a la base de datos
        with sqlite3.connect('mi_base_de_datos.db') as conexion:
            cursor = conexion.cursor()
            # Nombre de la tabla
            nombre_tabla = "ProductosItienda"
            # Consulta para seleccionar todos los datos de la tabla
            cursor.execute(f"SELECT * FROM {nombre_tabla}")
            # Obtener todos los resultados
            productos = cursor.fetchall()
            # Renderizar la plantilla y pasar los datos
            return render_template('productos.html', productos=productos)
    except sqlite3.Error as error:
        print("Error al cargar los datos:", error)
        return "Error al cargar los datos"

@app.route('/producto/<int:pid>')
def ruta_producto(pid):
    try:
        # Establecer la conexión a la base de datos
        with sqlite3.connect('mi_base_de_datos.db') as conexion:
            cursor = conexion.cursor()
            # Nombre de la tabla
            nombre_tabla = "ProductosItienda"
            # Consulta para seleccionar un producto específico por su id
            cursor.execute(f"SELECT * FROM {nombre_tabla} WHERE id = ?", (pid,))
            # Obtener el resultado
            producto = cursor.fetchone()
            # Renderizar la plantilla y pasar el producto
            return render_template('producto.html', producto=producto)
    except sqlite3.Error as error:
        print("Error al cargar el producto:", error)
        return "Error al cargar el producto"

# Programa principal
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
