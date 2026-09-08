from flask import Flask, app, render_template, request, redirect

app = Flask(__name__)
registros = []

@app.route('/')
def inicio():
    return render_template('registro.html')

@app.route('/lista')
def lista():
    return render_template('lista.html', registros = registros)

@app.route('/registro', methods=['GET'])
def registro():
    return render_template('registro.html')

@app.route('/prosesar_registro', methods=['POST'])
def prosesar_registro():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = request.form['edad']

    datos = {
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad
    }

    registros.append(datos)
    print(registros)

    return redirect('/lista')



if __name__ == '__main__':
    app.run(debug=True)