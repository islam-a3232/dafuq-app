from flask import Flask, render_template

app = Flask(__name__)

# Página principal
@app.route("/")
def home():
    return render_template("index.html")

# Juego 1
@app.route("/juego1")
def juego1():
    return render_template("juego1.html")

# Juego 2
@app.route("/juego2")
def juego2():
    return render_template("juego2.html")

# Juego 3
@app.route("/juego3")
def juego3():
    return render_template("juego3.html")

# Página de descarga
@app.route("/download")
def download():
    return render_template("download.html")

# Ejecutar la app
if __name__ == "__main__":
    app.run(debug=True)