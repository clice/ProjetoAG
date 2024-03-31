import random

from colorama import Fore, Style


# Declaração do objeto Criatura
class Criatura:
    # Construtor de inicialização dos atributos da Criatura
    def __init__(self, nome, tipo, pontos_vida, pontos_ataque, descricao, regiao):
        self.nome = nome                    # Nome da Criatura
        self.tipo = tipo                    # Tipo da Criatura
        self.pontos_vida = pontos_vida      # Pontos de vida da Criatura
        self.pontos_ataque = pontos_ataque  # Pontos de ataque da Criatura
        self.descricao = descricao          # Descrição da Criatura
        self.regiao = regiao                # Região (vértice) da Criatura no mapa (grafo)

    # String representado as informações sobre a Criatura
    def __str__(self):
        print(f"Criatura: {self.nome}")
        print(f"Pontos de vida: {self.pontos_vida}")
        print(f"Pontos de ataque: {self.pontos_ataque}")
        print(f"Descrição: {self.descricao}")
        print(f"Região: {self.regiao}\n")

    # MÉTODOS PARA OS PONTOS DE VIDA DA CRIATURA

    # Método para remover pontos de vida
    def remover_pontos_vida(self, pontos):
        self.pontos_vida -= pontos

    # Método para retornar se a Criatura está viva (pontos_vida > 0)
    def esta_viva(self):
        return self.pontos_vida > 0

    # MÉTODO PARA LUTA ENTRE UMA CRIATURA E O EXPLORADOR

    # Método para o ataque da Criatura contra o Explorador
    def atacar_explorador(self, explorador):
        dano = random.randint(1, self.pontos_ataque)
        explorador.pontos_vida -= dano
        return dano

    # MÉTODOS PARA LUTA ENTRE ENTRE CRIATURAS

    # Método para o ataque de uma Criatura contra outra
    def atacar_criatura(self, criatura):
        dano = random.randint(1, self.pontos_ataque)
        criatura.remover_pontos_vida(self.pontos_ataque)
        return dano

    # Método para a luta entre as Criaturas
    def lutar_criatura(self, criatura):
        # Se a Criatura é mais fraca que a outra
        if self.pontos_ataque < criatura.pontos_ataque:
            dano = self.atacar_criatura(criatura)
            print(Fore.GREEN + f"{self.tipo} atacou! Houve {dano} de dano.")
            print(Style.RESET_ALL)  # Restaurar cores
            print(f"{criatura.tipo} agora tem {criatura.pontos_vida} pontos de vida.")
            return criatura
        # Se a Criatura é mais forte que a outra
        elif self.pontos_ataque > criatura.pontos_ataque:
            dano = self.atacar_criatura(criatura)
            print(Fore.GREEN + f"{self.tipo} atacou! Houve {dano} de dano.")
            print(f"{criatura.tipo} agora tem {criatura.pontos_vida} pontos de vida.")
            print(Style.RESET_ALL)  # Restaurar cores
            return criatura
        
    # MÉTODO PARA QUANDO A CRIATURA FOR ENCONTRADA
    
    # Método para quando o Explorador encontrar uma Criatura
    def encontrar_criatura(self, explorador):
        print(Fore.RED + f"{self.nome} encontrado(a)! CUIDADO!")
        print(Style.RESET_ALL)  # Restaurar cores
        explorador.lutar_criatura(self)
