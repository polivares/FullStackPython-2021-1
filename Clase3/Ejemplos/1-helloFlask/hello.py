from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/')   
@app.route('/login')                        
def hello_world():
    # En lugar de devolver una cadena, 
    # devolvemos el resultado del metodo render_template , pasando el nombre de nuestro archivo HTML
    return render_template('index.html')  
    
@app.route('/hola/<string:nombre>')
def hola(nombre):
    return render_template("nombre.html",nombre=nombre)

if __name__=="__main__":
    app.run(debug=True)                   