from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    mensaje = data.get("mensaje", "")
    respuesta = f"Fernando Birri responde: {mensaje}"  # Aquí pondrás respuestas más elaboradas
    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    app.run(debug=True)

