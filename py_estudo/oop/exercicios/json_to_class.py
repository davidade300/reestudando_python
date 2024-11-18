from class_to_json import Pessoa
import json

CAMINHO_DO_ARQUIVO = "classe_para_dicionario.json"

with open("classe_para_dicionario.json", "rt") as f:
    pessoas = json.load(f)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)
