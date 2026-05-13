from flask import Flask, render_template, request

app = Flask(__name__)


#  Menú con los dos botones
@app.route('/')
def index():
    return render_template('index.html')


# Ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    promedio = None
    estado = None
    if request.method == 'POST':
        # Captura los datos del formulario y los conviente a decimales
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        # Calcula el promedio
        promedio = (nota1 + nota2 + nota3) / 3

        # aprobación
        if promedio >= 40 and asistencia >= 75:
            estado = 'APROBADO'
        else:
            estado = 'REPROBADO'

    return render_template('ejercicio1.html', promedio=promedio, estado=estado)


# Ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre_mayor = None
    caracteres = None
    if request.method == 'POST':
        # Guardar los nombres en una lista
        nombres = [
            request.form['nombre1'],
            request.form['nombre2'],
            request.form['nombre3']
        ]

        # Encontrar el nombre nas largo
        nombre_mayor = max(nombres, key=len)
        caracteres = len(nombre_mayor)

    return render_template('ejercicio2.html', nombre_mayor=nombre_mayor, caracteres=caracteres)


if __name__ == '__main__':
    app.run(debug=True)