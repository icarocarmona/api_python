from datetime import datetime
from flask import Flask, request, jsonify
import uuid
import json
from database import DAO

app = Flask(__name__)

mock_pessoa = {
    "apelido": "josé",
    "nome": "José Roberto",
    "nascimento": "2000-10-01",
    "stack": ["C#", "Node", "Oracle"]
}

MSG_ERROR = "ERROR"


class Pessoa(object):

    def __init__(self, id, apelido, nome, nascimento, stack):
        self.id = id
        self.apelido = apelido
        self.nome = nome
        self.nascimento = nascimento
        self.stack = stack

    def dumps(self):
        return json.dumps(self.__dict__, indent=4, sort_keys=True, default=str)

    def parse(data):
        apelido = data['apelido']
        nome = data['nome']
        nascimento = datetime.strptime(data["nascimento"], '%Y-%m-%d').date()
        stack = data['stack']
        return Pessoa(apelido, nome, nascimento, stack)

    def converte_para_pessoa(row):
        id, apelido, nome, nascimento, stack = row
        return Pessoa(id, apelido, nome, nascimento, json.loads(stack))


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
        pessoa = Pessoa.parse(data)
        return pessoa.dumps(), 201
    except Exception as e:
        return MSG_ERROR, 400


@app.route("/pessoas", methods=['GET'])
def busca_por_termo():
    args = request.args
    data = jsonify(args.get("t", default="", type=str))
    return data, 200


if __name__ == '__main__':
    app.run(debug=True)
