from flask import Flask, request, render_template_string, render_template, redirect, url_for, flash, session
import psycopg2

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necesario para usar flash()

# Conexión a la base de datos PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        host='db_container',  # El nombre del contenedor de PostgreSQL en docker-compose
        database='salud-y-bienestar_db',
        user='admin',
        password='admin1234'
    )
    return conn


@app.route("/")
def home():
    if "user" in session:
        user = session['user']
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))


@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    phone = request.form['phone']
    
    # Validación simple
    if not email or not password or not phone:
        return "Todos los campos son requeridos", 400

    # Verificar si el correo electrónico ya está registrado
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM clientes WHERE email = %s", (email,))
    existing_user = cur.fetchone()
    
    if existing_user:
        # Si el correo electrónico ya está registrado, mostrar mensaje de error personalizado
        flash('El correo electrónico ya está registrado. Por favor, utiliza otro.', 'error')
        cur.close()
        conn.close()
        return redirect(url_for('home'))  # Redirige de nuevo a la página principal


    # Inserta el nuevo usuario con la contraseña encriptada
    cur.execute("INSERT INTO clientes (name, email, password, phone) VALUES (%s, %s, md5(%s), %s)", (name, email, password, phone))
    conn.commit()
    cur.close()
    conn.close()
    
    flash('Usuario registrado correctamente', 'success')  # Mensaje de éxito
    return redirect(url_for('home'))



@app.route('/mensaje', methods=['POST'])
def mensaje():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # Validación simple
    if not name or not email or not message:
        return "Todos los campos son requeridos", 400
    

    conn = get_db_connection()
    cur = conn.cursor()
    # Si el correo electrónico no está registrado, proceder con la inserción de datos
    cur.execute("INSERT INTO mensajes (name, email, message) VALUES (%s, %s, %s)", (name, email, message))
    conn.commit()
    cur.close()
    conn.close()
    
    flash('Mensaje registrado correctamente', 'success')  # Mensaje de éxito
    return redirect(url_for('home'))


@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    # Validación simple
    if not email or not password:
        flash('Todos los campos son requeridos', 'error')
        return redirect(url_for('login'))


    # Verificar si el usuario está registrado
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT name FROM clientes WHERE email = %s and password= md5(%s)", (email, password))
    existing_user = cur.fetchone()

    if existing_user:
        session["user"] = email

        flash('Inicio de sesión exitoso', 'success')

    else:
        flash('Usuario no encontrado', 'error')

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
