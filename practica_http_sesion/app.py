from flask import Flask, render_template, request, redirect, url_for, session, abort

app = Flask(__name__)
app.secret_key = 'clave_secreta_total_segura_iti'

USUARIOS_DB = {
    "admin": {"password": "super1234", "rol": "administrador"},
    "alumno": {"password": "iti2026", "rol": "estudiante"}
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        password = request.form.get('password')

        if usuario in USUARIOS_DB and USUARIOS_DB[usuario]["password"] == password:
            session['usuario'] = usuario
            session['rol'] = USUARIOS_DB[usuario]['rol']
            
            if session['rol'] == 'administrador':
                return redirect(url_for('panel_admin'))
            elif session['rol'] == 'estudiante':
                return redirect(url_for('panel_estudiante'))
        else: 
            return render_template('login.html', error="Usuario o contraseña incorrecta")

@app.route('/logout')
def logout():
    session.clear() 
    return redirect(url_for('login'))

@app.route('/panel-admin')
def panel_admin():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    if session.get('rol') != 'administrador':
        return "403 Prohibido: No tienes permisos suficientes", 403
    return render_template('panel_admin.html', usuario=session['usuario'])
    
@app.route('/panel-estudiante')
def panel_estudiante():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    if session.get('rol') != 'estudiante':
        return "403 Prohibido: No tienes permisos suficientes", 403
    return render_template('panel_estudiante.html', usuario=session['usuario'])

if __name__ == '__main__':
    print("Servidor corriendo en: http://127.0.0.1:5000/login")
    app.run(debug=True)