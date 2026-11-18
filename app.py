from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template ('index.html')
@app.route('/procesar-evaluacion', methods=['POST'])
def procesar_evaluacion():
    nombre_alumno = request.form.get('nombre')
    matricula = request.form.get('matricula')
    try:
        promedio = float (request.form.get('promedio'))
        creditos = int (request.form.get('creditos'))
    except (ValueError, TypeError):
        return "Error: los datos ingresados son inválidos.", 400
    PROMEDIO_MINIMO = 7.0
    CREDITOS_MINIMO = 250
    if promedio >= PROMEDIO_MINIMO and creditos>= CREDITOS_MINIMO:
        resultado = "APROBADO"
        mensaje = f"Felicidad, {nombre_alumno}! cumples con los requisitos para iniciar tus estancias."
        estilo = "color: green; font-weight:bold;"
    else: 
        resultado = "RECHAZADO"
        mensaje = f"Lo sentimos, {nombre_alumno}. No cumples con los criterios minimos solicitados."
        estilo = "color: red; font-weight:bold;"

    return render_template('resultado.html', nombre={nombre_alumno}, matricula={matricula}, promedio={promedio}, creditos={creditos}, resultado={resultado}, mensaje={mensaje}, estilo={estilo})

if __name__ == '__main__':
    app.run(debug=True, port=5000)