from flask import Flask, render_template  # added render_template!

app = Flask(__name__)                     
    
@app.route('/hola/como/estas')       
@app.route('/hello/how/are/you')                
def hello_world():
    # En lugar de devolver una cadena, 
    # devolvemos el resultado del metodo render_template , pasando el nombre de nuestro archivo HTML
    return render_template('index.html')  

@app.route("/bienvenido/<string:nombre>")
def bienvenido(nombre):
    return render_template("bienvenido.html",name=nombre)

if __name__=="__main__":
    app.run(debug=True)     



# Tu código va a contener los siguientes elementos
#
# Vistas: Van los elementos que serán cargados en el lado del cliente
# Enrutadores: Son las funciones encargadas de responder a las consultas de páginas en base a las solicitudes del lado del cliente 
# (son los encargados de determinar qué vista se muestra en cada momento)
# Modelos: Clases python encargadas de modificar y acceder a los datos almacenados en tu base de datos

