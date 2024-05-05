import sqlite3
# Establecer la conexión a la base de datos
with sqlite3.connect('mi_base_de_datos.db') as conexion:
    cursor = conexion.cursor()

    # Nombre de la tabla
    nombre_tabla = "ProductosItienda"

    try:
        # Eliminar la tabla si existe
        cursor.execute(f"DROP TABLE IF EXISTS {nombre_tabla}")

        # Crear la tabla
        cursor.execute(f'''CREATE TABLE {nombre_tabla} (
                            id INTEGER PRIMARY KEY,
                            categoria TEXT,
                            marca TEXT,
                            modelo TEXT,
                            descripcion TEXT,
                            precio INTEGER
                        )''')

        # Insertar los datos iniciales
        datos = [
            (101, 'Celular', 'Apple', 'iPhone 11', '128GB+6GB RAM, Chip A13', 1100000),
            (104, 'Celular', 'Apple', 'iPhone 12', '256GB+8GB RAM, Chip A14', 1400000),
            (201, 'Celular', 'Apple', 'iPhone 13', '256GB+8GB RAM, chip A15 BIONIC', 2000000),
            (203, 'Celular', 'Apple', 'iPhone 14', '256GB+8GB RAM, A15 BIONIC', 2500000),
            (207, 'Celular', 'Apple', 'iPhone 15', '1TB+8GB RAM, A16 BIONIC ', 3400000),
        ]

        cursor.executemany(f"INSERT INTO {nombre_tabla} VALUES (?, ?, ?, ?, ?, ?)", datos)

        print("La tabla y los datos se han insertado correctamente.")

    except sqlite3.Error as error:
        print("Error al trabajar con la base de datos:", error)