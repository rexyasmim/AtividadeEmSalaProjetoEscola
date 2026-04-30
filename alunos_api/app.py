from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

alunos = [
    {"id": 1, "nome": "Joao Silva", "curso": "Sistemas de Informação"},
    {"id": 2, "nome": "Maria Oliveira", "curso": "Engenharia de Computação"}
]

@app.route("/alunos", methods=["GET"])
def listar_alunos():
    return jsonify(alunos)

@app.route("/alunos", methods=["POST"])
def cadastrar_aluno():
    dados = request.get_json()
    novo_aluno = {
        "id": len(alunos) + 1,
        "nome": dados["nome"],
        "curso": dados["curso"]
    }
    alunos.append(novo_aluno)
    return jsonify(novo_aluno), 201

@app.route("/alunos/<int:id>", methods=["GET"])
def buscar_aluno(id):
    for aluno in alunos:
        if aluno["id"] == id:
            return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404

app.run(host="0.0.0.0", port=5000)