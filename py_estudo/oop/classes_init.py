class Pessoa:
    # o self é requerido em todos os inicializadores
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa(nome="David", sobrenome="Aderaldo")
