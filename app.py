from flask import Flask, app, render_template, request, redirect, url_for
from registros import Registro
app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def inicio():
    return redirect('/registro')

@app.route('/registro', methods=['POST', 'GET'])
def prosesar_registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']

        data = {
            'nombre': nombre,
            'apellido': apellido,
            'edad': edad
        }

        Registro.save(data)
        return redirect(url_for('lista'))
    return render_template('registro.html')

@app.route('/lista')
def lista():
    registros = Registro.get_all()
    return render_template('lista.html', registros = registros)

if __name__ == '__main__':
    app.run(debug=True)