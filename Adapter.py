# Implementação sem o padrão Prototype

class MagicalCreature:
    def __init__(self, name, health, magic_power, abilities):
        self.name = name
        self.health = health
        self.magic_power = magic_power
        self.abilities = abilities

    def display_info(self):
        abilities_str = ", ".join(self.abilities)
        return f"Criatura: {self.name} | Saúde: {self.health} | Poder Mágico: {self.magic_power} | Habilidades: {abilities_str}"


# Cliente - Criando criaturas mágicas
def create_game_bestiary():
    # Criando cada criatura do zero
    phoenix = MagicalCreature("Fênix", 300, 150, ["Renascimento", "Chamas Eternas", "Voo"])
    dragon = MagicalCreature("Dragão", 500, 200, ["Sopro de Fogo", "Escamas Resistentes", "Voo"])
    unicorn = MagicalCreature("Unicórnio", 200, 180, ["Cura", "Purificação", "Velocidade"])
    
    # Para criar uma variação, precisamos criar um novo objeto com parâmetros modificados
    ice_dragon = MagicalCreature("Dragão de Gelo", 550, 220, ["Sopro de Gelo", "Escamas Resistentes", "Voo", "Resistência ao Frio"])
    
    # Tentando criar uma criatura híbrida - precisamos conhecer todos os detalhes
    phoenix_dragon = MagicalCreature(
        "Dragão Fênix", 
        400,  # média dos valores
        180,  # média dos valores
        ["Renascimento", "Sopro de Fogo", "Voo", "Escamas Flamejantes"]
    )
    
    bestiary = [phoenix, dragon, unicorn, ice_dragon, phoenix_dragon]
    return bestiary


# Usando o bestiário
bestiary = create_game_bestiary()
for creature in bestiary:
    print(creature.display_info())

#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------

# Implementação com o padrão Prototype
import copy


class MagicalCreaturePrototype:
    def __init__(self, name, health, magic_power, abilities):
        self.name = name
        self.health = health
        self.magic_power = magic_power
        self.abilities = abilities

    def clone(self):
        # Usando deepcopy para garantir que listas e objetos internos também sejam clonados
        return copy.deepcopy(self)
    
    def display_info(self):
        abilities_str = ", ".join(self.abilities)
        return f"Criatura: {self.name} | Saúde: {self.health} | Poder Mágico: {self.magic_power} | Habilidades: {abilities_str}"
    
    def merge_with(self, other_creature, new_name=None):
        """Método para fundir duas criaturas, criando um híbrido."""
        merged = self.clone()
        
        if new_name:
            merged.name = new_name
        else:
            merged.name = f"{self.name}-{other_creature.name}"
            
        # Calculando as médias para os atributos numéricos
        merged.health = (self.health + other_creature.health) // 2
        merged.magic_power = (self.magic_power + other_creature.magic_power) // 2
        
        # Combinando habilidades únicas
        merged.abilities = list(set(self.abilities + other_creature.abilities))
        
        return merged


class BestiaryRegistry:
    def __init__(self):
        self.creatures = {}
    
    def register_creature(self, name, prototype):
        self.creatures[name] = prototype
    
    def get_creature(self, name):
        if name in self.creatures:
            return self.creatures[name].clone()
        return None
    
    def create_variant(self, base_name, new_name, **modifications):
        if base_name in self.creatures:
            variant = self.creatures[base_name].clone()
            variant.name = new_name
            
            # Aplicando as modificações
            for attr, value in modifications.items():
                if hasattr(variant, attr):
                    setattr(variant, attr, value)
            
            # Registrando a variante
            self.register_creature(new_name, variant)
            return variant
        return None


# Cliente - Usando o registro de bestiário com o padrão Prototype
def create_game_bestiary():
    registry = BestiaryRegistry()
    
    # Registrando protótipos base
    phoenix = MagicalCreaturePrototype("Fênix", 300, 150, ["Renascimento", "Chamas Eternas", "Voo"])
    dragon = MagicalCreaturePrototype("Dragão", 500, 200, ["Sopro de Fogo", "Escamas Resistentes", "Voo"])
    unicorn = MagicalCreaturePrototype("Unicórnio", 200, 180, ["Cura", "Purificação", "Velocidade"])
    
    registry.register_creature("phoenix", phoenix)
    registry.register_creature("dragon", dragon)
    registry.register_creature("unicorn", unicorn)
    
    # Criando variações usando protótipos
    ice_dragon = registry.create_variant(
        "dragon", 
        "Dragão de Gelo", 
        health=550, 
        magic_power=220, 
        abilities=["Sopro de Gelo", "Escamas Resistentes", "Voo", "Resistência ao Frio"]
    )
    
    # Criando um híbrido - fundindo protótipos
    phoenix_dragon = phoenix.merge_with(dragon, "Dragão Fênix")
    registry.register_creature("phoenix_dragon", phoenix_dragon)
    
    # Criando uma variação do híbrido
    elder_phoenix_dragon = registry.create_variant(
        "phoenix_dragon",
        "Dragão Fênix Ancião",
        health=450,
        magic_power=250,
        abilities=["Renascimento", "Sopro de Fogo Eterno", "Voo Majestoso", "Escamas Flamejantes", "Sabedoria Ancestral"]
    )
    
    # Agora podemos facilmente clonar qualquer criatura cadastrada
    creatures = [
        registry.get_creature("phoenix"),
        registry.get_creature("dragon"),
        registry.get_creature("unicorn"),
        ice_dragon,
        phoenix_dragon,
        elder_phoenix_dragon,
        # Criando um novo no momento - Unicórnio de Cristal
        registry.create_variant(
            "unicorn",
            "Unicórnio de Cristal",
            magic_power=250,
            abilities=["Cura Aprimorada", "Purificação", "Velocidade", "Reflexão Mágica"]
        )
    ]
    
    return creatures, registry


# Usando o bestiário
creatures, registry = create_game_bestiary()
print("=== Bestiário Mágico ===")
for creature in creatures:
    print(creature.display_info())

print("\n=== Criando uma nova criatura híbrida em tempo de execução ===")
# Criando uma combinação sob demanda
crystal_dragon = registry.get_creature("Unicórnio de Cristal").merge_with(
    registry.get_creature("Dragão de Gelo"), 
    "Dragão de Cristal Gelado"
)
print(crystal_dragon.display_info())