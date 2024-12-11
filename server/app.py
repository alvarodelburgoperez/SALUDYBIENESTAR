from flask import Flask, request, render_template_string, render_template, redirect, url_for, flash, session, current_app
import psycopg2

app = Flask(__name__, template_folder='../src/html')
app.secret_key = 'clavesecreta'


# Conexión a la base de datos PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        host='db_container',  # El nombre del contenedor de PostgreSQL en docker-compose
        database='salud-y-bienestar_db',
        user='admin',
        password='admin1234'
    )
    return conn

global_name = None

@app.route('/')
def home():

    # Renderizar index.html y pasar el nombre como una variable
    current_app.logger.info('--------------------------------------')
    current_app.logger.info('Nombre de usuario en sesión:', global_name)
    current_app.logger.info('--------------------------------------')
    return render_template('index.html', global_name)


@app.route('/register', methods=['GET', 'POST'])
def register():

    global global_name

    if request.method == 'GET':
        return redirect('register.html')  # Usar render_template

    if request.method == 'POST':

        current_app.logger.info('--------------------------------------')
        current_app.logger.info('Formulario POST recibido')
        current_app.logger.info('--------------------------------------')

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        
        # Validación simple
        if not email or not password or not phone:
            flash("Todos los campos son requeridos", 'error')
            return redirect('register.html')  # Vuelve al formulario si falta algún campo

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
            return redirect('register.html')  # Redirige de nuevo al formulario de registro

        # Insertar el nuevo usuario con la contraseña encriptada
        cur.execute("INSERT INTO clientes (name, email, password, phone) VALUES (%s, %s, md5(%s), %s)", (name, email, password, phone))
        conn.commit()
        cur.close()
        conn.close()
        

        
        # Guardar el nombre en la variable global
        session['user_name'] = name
        global_name = name
        current_app.logger.info('--------------------------------------')
        current_app.logger.info(f'Nombre de usuario guardado en sesión: {name}')
        current_app.logger.info('--------------------------------------')

        flash('Usuario registrado correctamente', 'success')  # Mensaje de éxito
        
        return redirect(url_for('home'))  # Después de registrarse, redirige a la página principal

    




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

    if request.method == 'GET':
        return redirect('login.html')

    if request.method == 'POST':
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
            current_app.logger.info('--------------------------------------')
            current_app.logger.info(f'Nombre del usuario en login: {naexisting_userme}')
            current_app.logger.info('--------------------------------------')
            return redirect(url_for('home'))

        else:
            flash('Usuario no encontrado', 'error')

            return redirect(login.html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)