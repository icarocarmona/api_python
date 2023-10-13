import json
from flask import Flask, request, jsonify
from database import DAO
from pessoa import Pessoa

app = Flask(__name__)

mock_pessoa = {
    "apelido": "josé",
    "nome": "José Roberto",
    "nascimento": "2000-10-01",
    "stack": ["C#", "Node", "Oracle"]
}

MSG_ERROR = "ERROR"


@app.route("/pessoas/<id>", methods=['GET'])
def get_pessoa(id):
    query = "SELECT id, apelido, nome, nascimento, stack FROM pessoas WHERE id = %s"
    dao = DAO()
    res = dao.select(query, [id])
    pessoa = Pessoa.converte_para_pessoa(res[0])
    return pessoa.dumps(), 200


@app.route("/contagem-pessoas", methods=['GET'])
def count_pessoas():
    query = "SELECT COUNT(*) FROM pessoas"
    dao = DAO()
    res = dao.select(query)
    return str(res[0][0]), 200


@app.route("/pessoas", methods=['POST'])
def set_pessa():
    try:
        data = request.get_json()
        pessoa = Pessoa.cria_pessoa(data)
        return pessoa.dumps(), 201
    except Exception as e:
        print(e)
        return MSG_ERROR, 400

# para fazer uma busca por pessoas


@app.route("/pessoas", methods=['GET'])
def busca_por_termo():
    args = request.args
    value = args.get("t", default="", type=str)
    query = 'SELECT id, apelido, nome, nascimento, stack FROM pessoas WHERE stack_concat like %s'
    dao = DAO()

    rows = dao.select(query, [f"%{value}%"])
    print(*rows)
    pessoas = []
    for row in rows:
        pessoas.append(Pessoa.from_dict(row).to_dict())

    return jsonify(pessoas), 200


if __name__ == '__main__':
    app.run(debug=True)
