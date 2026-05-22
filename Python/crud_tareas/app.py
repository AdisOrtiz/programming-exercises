#Importar Flask -> trae la herramienta Flask
from flask import Flask, render_template, request, redirect
import sqlite3 #Es el módulo de Python para hablar con SQLite

app = Flask(__name__) #Se crea la aplicación web
def conectar_db():
    conexion = sqlite3.connect('database.db')
    return conexion

def crear_tabla():
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS tareas(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       tarea TEXT NOT NULL
                   )
                ''')
    conexion.commit() #Guarda cambios
    conexion.close() #Cierra conexión
    #cursor -> Es el objeto que ejecuta SQL

crear_tabla()

def obtener_tarea():
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute('Select * from tareas')
    tareas = cursor.fetchall() # fetchall -> Obtiene todos los resultados SQL
    conexion.close()
    return tareas

@app.route('/') #Es una ruta. Sig. cuando alguien visite / -> y eso es la página principal
def inicio(): #Es la función que responde a la URL de arriba
    tareas = obtener_tarea()
    return render_template('index.html',tareas=tareas)#Flask dice: HTML, toma esta lista llamada tareas

@app.route('/agregar', methods=['POST'])#Se agregó una nueva ruta, y methods=['POST'] dice: esta ruta acepta datos enviado 
def agregar(): #Función que maneja el formulario
    tarea = request.form['tarea'] #request.form -> dame los datos enviados desde el formulario. ['tarea'] -> dame el input cuyo name='tarea', eso está en el index.html
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute(
        'Insert Into tareas (tarea) Values (?)', #? es un placeholder
        (tarea,)
    )
    conexion.commit()
    conexion.close()
    return redirect('/') #Vuelve a esta URL

@app.route('/eliminar/<int:id>') #
def eliminar(id):
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute('Delete From tareas Where id = ?', (id,))
    conexion.commit()
    conexion.close()
    return redirect('/') #Vuelve a cargar página principal

@app.route('/editar/<int:id>', methods=['GET','POST']) #GET -> Muestra el formulario. POST -> Guarda cambios
def editar(id):
    conexion = conectar_db()
    cursor = conexion.cursor()
    #Si el usuario envió el formulario
    if request.method == 'POST':
        nueva_tarea = request.form['tarea']
        cursor.execute(
            'Update tareas Set tarea = ? Where id = ?',
            (nueva_tarea, id)
        )
        conexion.commit()
        conexion.close()
        return redirect('/')
    
    #Buscar tarea actual en la BD
    cursor.execute(
        'Select * From tareas Where id = ?',
        (id,)
    )
    
    tarea = cursor.fetchone() #Devuelve una sola fila, algo así: (1, 'Comprar leche')
    conexion.close()
    
    return render_template('editar.html',tarea=tarea)

if __name__ == '__main__': #Pregunta: ¿este archivo se ejecutó directamente?
    app.run(debug=True)
    # Aquí flask:
    #     - Inicia servidor web
    #     - espera conexiones
    #     - activa modo debug
    