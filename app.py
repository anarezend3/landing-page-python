from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    mensagem = None

    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        texto = request.form.get("mensagem")

        print("Nova mensagem recebida:")
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"Mensagem: {texto}")

        mensagem = "Mensagem enviada com sucesso!"

    return render_template("index.html", mensagem=mensagem)


if __name__ == "__main__":
    app.run(debug=True)