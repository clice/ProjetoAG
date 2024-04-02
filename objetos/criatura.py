import random

from colorama import Fore, Back, Style
from helpers.sorteios import lista_criaturas


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
        print(Back.RED + Fore.BLACK + f" Criatura: {self.nome} " + Style.RESET_ALL)
        print(Back.RED + Fore.BLACK + f" Pontos de vida: {self.pontos_vida} " + Style.RESET_ALL)
        print(Back.RED + Fore.BLACK + f" Pontos de ataque: {self.pontos_ataque} " + Style.RESET_ALL)
        print(Back.RED + Fore.BLACK + f" Descrição: {self.descricao} " + Style.RESET_ALL + "\n")

    # MÉTODOS PARA OS PONTOS DE VIDA DA CRIATURA

    # Método para remover pontos de vida
    def remover_pontos_vida(self, pontos):
        self.pontos_vida -= pontos

    # Método para retornar se a Criatura está viva (pontos_vida > 0)
    def esta_viva(self):
        return self.pontos_vida > 0

    # Método para reviver a Criatura
    def reviver(self, ilha):
        print(Fore.YELLOW + f"\n{self.nome.upper()} MORREU!\n")
        self.regiao.remover_criatura(self)  # Remover Criatura da Região atual
        ilha.remover_criatura(self)         # Remover Criatura da Ilha

        # Buscar a Criatura desejada para reviver em outra Região
        for criatura in lista_criaturas():
            if criatura["nome"] == self.nome:
                # Reviver a mesma Criatura em outra região
                regiao = random.choice(ilha.regioes[1:-1])
                nova_criatura = Criatura(
                    criatura['nome'], criatura['tipo'], criatura['pontos_vida'],
                    criatura['pontos_ataque'], criatura['descricao'], regiao
                )  # Objeto Criatura
                regiao.adicionar_criatura(nova_criatura)  # Adicionar Criatura na Região
                ilha.adicionar_criatura(nova_criatura)    # Adicionar Criatura na Ilha

                print(Fore.RED + f"{self.nome.upper()} FOI REVIVIDO(A)!\n")
                break
    
    # MÉTODO PARA A REGIÃO DA CRIATURA

    # Método para mostrar a localização atual
    def mostrar_regiao(self):
        print(Fore.MAGENTA + f"Localização atual: {self.regiao.tipo}.\n")
