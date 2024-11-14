class Pessoa:
    # caso parametros de classe sejam definidos fora do __init__,
    # eles seram estáticos para todas as classes
    # o self é requerido em todos os inicializadores
    # o método init sempre retorna None
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa(nome="David", sobrenome="Aderaldo")
