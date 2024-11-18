# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

CAMINHO_DO_ARQUIVO = "classe_para_dicionario.json"


class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade


p1 = Pessoa("Joao", 33)
p2 = Pessoa("Helena", 21)
p3 = Pessoa("Joana", 11)

pessoas = [p1.__dict__, p2.__dict__, p3.__dict__]

with open(CAMINHO_DO_ARQUIVO, "w") as f:
    json.dump(pessoas, f, ensure_ascii=True, indent=2)
