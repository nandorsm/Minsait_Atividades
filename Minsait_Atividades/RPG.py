class SerVivo:
    def __init__(self, pontos_vida, pontos_atk):
        self.pontos_vida = pontos_vida
        self.pontos_atk = pontos_atk

    def atacar(self, alvo): 
        alvo.pontos_vida -= self.pontos_atk
        print("===================")
        print(f'Seu alvo sofreu {self.pontos_atk} de dano')
        print("===================")
        
    def status(self, ):
        print("Vida: ", self.pontos_vida)


class Personagem(SerVivo):
    def __init__(self, nome):
        super().__init__(pontos_vida=35, pontos_atk=8)
        self.nome = nome
    
    def status(self, ):
        print("--Personagem--")
        print(f'NOME: {self.nome}')
        print(f'VIDA: {self.pontos_vida}')
        print(f'ATK: {self.pontos_atk}')


class Monstro(SerVivo):
    def __init__(self, tipo):
        super().__init__(pontos_vida=25, pontos_atk=5)
        self.tipo = tipo

    def status(self):
        print("--Monstro--")
        print("VIDA: ", self.pontos_vida)
        print("ATK: ", self.pontos_atk)
        print("TIPO:", self.tipo)
        

class Lobo(Monstro):
    def __init__(self, forca):
        super().__init__(tipo="Grande")
        self.pontos_vida = 30
        self.pontos_atk = 6
        self.forca = forca
        
    def status(self):
        print("--LOBO--")
        print("VIDA: ", self.pontos_vida)
        print("ATK: ", self.pontos_atk)
        print("TIPO:", self.tipo)
        print("FORÇA: ", self.forca)
    
    
class Goblin(Monstro):
    def __init__(self, inteligencia):
        super().__init__(tipo="Pequeno")
        self.pontos_vida = 20
        self.pontos_atk = 10
        self.inteligencia = inteligencia
        
    def status(self):
        print("--GOBLIN--")
        print("VIDA: ", self.pontos_vida)
        print("ATK: ", self.pontos_atk)
        print("TIPO:", self.tipo)
        print("INTELIGÊNCIA: ", self.inteligencia)

# monster = Monstro(tipo="pequeno")
# monster.status()

# guerreiro = Personagem(nome="Fernando")
# guerreiro.status()

# guerreiro.atacar(alvo=monster)
# monster.status()


wolf = Lobo(forca="Forte")
wolf.status()

goblin = Goblin(inteligencia="Mágico")
goblin.status()

wolf.atacar(alvo=goblin)
goblin.status()

goblin.atacar(alvo=wolf)
wolf.status()
