# @property - um getter Pythonico
# @getter - um mpetodo para obter um atributo
# @property é uma propriedade do objeto, ela é um método que se comporta como atributo,
# geralmente é usado nas seguinte situações:
# - como getter;
# - p/ evitar qebrar código cliente;
# - p/ habilitar setter;
# - p/ executar ações ao obter um atributo


# em python, getter se comporta como atributo, é chamado sem os parentesis
# codigo cliente é o codigo que usa seu codigo
class Caneta:
    def __init__(self, cor: str) -> None:
        self.cor_tinta = cor

    @property  # faz um método se comportar como atributo, ações podem ser executadas
    def cor(self):
        print("@property")
        return self.cor_tinta

    @property
    def cor_tampa(self):
        return 123456


caneta = Caneta(cor="Azul")


print(caneta.cor)
# print(caneta.cor_tampa()) -> gera erro (int object not callable)
print(caneta.cor_tampa)  # -> não gera erro
