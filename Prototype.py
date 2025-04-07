# |Sem Prototype

class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return f"Carro(modelo='{self.modelo}', ano={self.ano})"


def main_sem_prototype():
    carro1 = Carro("Modelo A", 2020)
    carro2 = Carro("Modelo A", 2020)  # criação repetitiva
    print(carro1)
    print(carro2)


if __name__ == "__main__":
    main_sem_prototype()


# Com Prototype
class Prototype:
    def clone(self):
        raise NotImplementedError("Subclasses devem implementar o método clone.")


class CarroPrototype(Prototype):
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def clone(self):
        # Retorna uma nova instância com os mesmos atributos
        return CarroPrototype(self.modelo, self.ano)

    def __str__(self):
        return f"CarroPrototype(modelo='{self.modelo}', ano={self.ano})"


def main_com_prototype():
    # Criação do protótipo
    prototipo = CarroPrototype("Modelo B", 2021)

    # Clonagem para criar novos objetos
    carro_clonado1 = prototipo.clone()
    carro_clonado2 = prototipo.clone()

    print(carro_clonado1)
    print(carro_clonado2)


if __name__ == "__main__":
    main_com_prototype()
