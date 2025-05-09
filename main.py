from flask import Flask, render_template, request
import os
# Define a pasta onde estão os arquivos HTML (neste caso, a raiz do projeto)
template_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder=template_dir)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculadora", methods=["GET", "POST"])
def calculadora():
    resultado = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacao = request.form["operacao"]

            if operacao == "soma":
                resultado = num1 + num2
            elif operacao == "subtracao":
                resultado = num1 - num2
            elif operacao == "multiplicacao":
                resultado = num1 * num2
            elif operacao == "divisao":
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    resultado = "Erro: Divisão por zero"
        except:
            resultado = "Erro nos dados fornecidos"

    return render_template("calculadora.html", resultado=resultado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)