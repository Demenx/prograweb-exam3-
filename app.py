from flask import Flask, render_template, request

app = Flask(__name__)

# Página principal con el menú
@app.route('/')
def index():
    return render_template('index.html')

# Ejercicio 1: Cálculo de total con descuento
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad'])

        precio_unitario = 9000
        total_sin_descuento = cantidad_tarros * precio_unitario
        descuento = 0

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        total_con_descuento = total_sin_descuento * (1 - descuento)

        resultado = {
            'nombre': nombre,
            'total_sin_descuento': total_sin_descuento,
            'total_con_descuento': total_con_descuento
        }
    return render_template('ejercicio1.html', resultado=resultado)

# Ejercicio 2: Login de usuarios
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']

        usuarios = {
            'juan': 'admin',
            'pepe': 'user'
        }

        if usuario in usuarios and usuarios[usuario] == password:
            if usuario == 'juan':
                mensaje = f"Bienvenido administrador {usuario}"
            else:
                mensaje = f"Bienvenido usuario {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"
    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
