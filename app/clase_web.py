from flask import Flask, jsonify

app = Flask(__name__)
PORT = 5000

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = [{"id": 1, "nombre": "Juanito Perez", "email": "juanito.perez@gmail.com"}]
    return jsonify(usuarios), 200

@app.route('/')
def home():
    return "API de usuarios funcionando"
    # return jsonify({"message:" "API de usuarios funcionando."}), 200

if __name__ == '__main__':
    app.run(port=PORT, debug=False)