from flask import Flask, render_template, request

app = Flask(__name__)

grupos = []

@app.route('/')
@app.route('/register')
def register():
    if len(grupos) == 0:
        id = 1
    else:
        id = grupos[-1].id + 1
    x=1
    y=2
    return render_template("register.html", id=id)


@app.route('/lista_grupos', methods=["GET","POST"])
def list_groups():
    if request.method == "POST":
        if len(grupos) == 0:
            id = 1
        else:
            id = grupos[-1].id + 1
        integrante1 = request.form.get("integrante1")
        integrante2 = request.form.get("integrante2")
        integrante3 = request.form.get("integrante3")
        integrantes = [integrante1, integrante2, integrante3]
        tema = request.form.get("project_title")
        descripcion = request.form.get("project_description")
        group = Grupo(id, integrantes, tema, descripcion)
        grupos.append(group)

    
    return render_template("list_groups.html", grupos=grupos)
    
class Grupo:
    def __init__(self, id, integrantes, tema, descripcion):
        self.id = id
        self.integrantes = integrantes
        self.tema = tema
        self.descripcion = descripcion


if __name__ == '__main__':
    app.run(debug=True)
