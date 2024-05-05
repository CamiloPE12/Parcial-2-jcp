from flask import Flask, render_template
import sqlite3
# Aplicación
app = Flask(__name__)

# Rutas
@app.route('/')
def ruta_raiz():
    return render_template('index.html')

@app.route('/index.html')
def ruta_index():
    return render_template('index.html')

@app.route('/productos.html')
def mostrar_productos():
    try:
        with sqlite3.connect('mi_base_de_datos.db') as conexion:
            cursor = conexion.cursor()
            nombre_tabla = "ProductosItienda"
            cursor.execute(f"SELECT * FROM {nombre_tabla}")
            productos = cursor.fetchall()
            return render_template('productos.html', productos=productos)
    except sqlite3.Error as error:
        print("Error al cargar los datos:", error)
        return "Error al cargar los datos"

@app.route('/contacto.html')
def ruta_contacto():
    return render_template('contacto.html')

# Programa principal
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
