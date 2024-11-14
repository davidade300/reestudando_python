# Métodos em instancias de classes
# Hard coded -> algo que foi escrito diretamente no código


class Carro:
    def __init__(self, nome) -> None:
        # self.nome = "Fusca" -> Hard coded
        self.nome = nome

    def acelerar(self):  # para usar os dados da instância, basta passar o self
        return "f{self.nome} está acelerando"


fusca = Carro("fusca")
print(fusca.nome)
fusca.acelerar()


celta = Carro("celta")
print(celta.nome)

Carro.acelerar(fusca)
