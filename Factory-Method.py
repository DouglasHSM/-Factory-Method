from abc import ABC, abstractmethod

# Interface do Produto
class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

# Implementações concretas do Produto
class ConcreteProductA(Product):
    def operation(self) -> str:
        return "Resultado de ConcreteProductA"

class ConcreteProductB(Product):
    def operation(self) -> str:
        return "Resultado de ConcreteProductB"

# Classe Criadora (Creator)
class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        """Método fábrica que deve ser implementado pelas subclasses"""
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        return f"O criador usou o produto: {product.operation()}"

# Criadores Concretos
class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()

# Código Cliente
def client_code(creator: Creator) -> None:
    print("Cliente: Não preciso saber a classe concreta do criador, apenas uso sua interface.")
    print(creator.some_operation())

if __name__ == "__main__":
    print("App: Executando com ConcreteCreatorA.")
    client_code(ConcreteCreatorA())
    
    print("\nApp: Executando com ConcreteCreatorB.")
    client_code(ConcreteCreatorB())
