from flask import Flask, jsonify, request

app = Flask(__name__)

atividades = [
    {
        "id": 1,
        "titulo": "Lista de Docker",
        "descricao": "Criar Dockerfile",
        "aluno_id": 1,
        "status": "pendente"
    }
]

@app.route("/atividades", methods=["GET"])
def listar_atividades():
    return jsonify(atividades)

@app.route("/atividades", methods=["POST"])
def cadastrar_atividade():
    dados = request.get_json()
    nova = {
        "id": len(atividades) + 1,
        "titulo": dados["titulo"],
        "descricao": dados["descricao"],
        "aluno_id": dados["aluno_id"],
        "status": dados.get("status", "pendente")
    }
    atividades.append(nova)
    return jsonify(nova), 201

@app.route("/atividades/aluno/<int:aluno_id>", methods=["GET"])
def listar_por_aluno(aluno_id):
    return jsonify([a for a in atividades if a["aluno_id"] == aluno_id])

@app.route("/atividades/<int:id>/concluir", methods=["PUT"])
def concluir(id):
    for a in atividades:
        if a["id"] == id:
            a["status"] = "concluida"
            return jsonify(a)
    return jsonify({"erro": "não encontrada"}), 404

app.run(host="0.0.0.0", port=5001)