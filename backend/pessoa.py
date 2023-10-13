from datetime import datetime
import json
import uuid
from database import DAO


class Pessoa(object):

    def __init__(self, id, apelido, nome, nascimento, stack):
        self.id = id
        self.apelido = apelido
        self.nome = nome
        self.nascimento = nascimento
        self.stack = stack

    def dumps(self):
        return json.dumps(self.__dict__, indent=4, sort_keys=True, default=str)

    def to_dict(self):
        return {
            "id": self.id,
            "apelido": self.apelido,
            "nome": self.nome,
            "nascimento": self.nascimento.strftime('%Y-%m-%d'),
            "stack": self.stack
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            str(data["id"]),
            data["apelido"],
            data["nome"],
            # Converte a string para date
            datetime.fromisoformat(data["nascimento"]),
            data["stack"]
        )

    def cria_pessoa(data):
        id = str(uuid.uuid4())
        apelido = data['apelido']
        nome = data['nome']
        nascimento = datetime.strptime(data["nascimento"], '%Y-%m-%d').date()
        stack = data['stack']
        stack_concatenado = ', '.join(stack) if stack != None else None
        pessoa = Pessoa(id, apelido, nome, nascimento, stack)
        dao = DAO()
        query = "INSERT INTO pessoas (id,apelido,nome,nascimento,stack,stack_concat)VALUES (%s,%s,%s,%s,%s,%s);"
        values = (id, apelido, nome, nascimento,
                  json.dumps(stack), stack_concatenado)
        dao.insert(query, values)
        return pessoa

    def converte_para_pessoa(row):
        id, apelido, nome, nascimento, stack = row
        return Pessoa(id, apelido, nome, nascimento, json.loads(stack))
