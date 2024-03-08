import random


# Declaração do objeto Personagem
class Personagem(object):
    # Construtor de inicialização dos atributos do Personagem
    def __init__(self):
        self.pontos_vida = 100   # Pontos de vida do Personagem
        self.pontos_ataque = 20  # Pontos de ataque do Personagem
        self.perc_tesouro = 0    # Porcentagem do tesouro carregado pelo Personagem
        self.regiao = 0          # Posição do Personagem no mapa (grafo)
        self.itens = None        # Lista de itens carregados pelo Personagem

    # String representando as informações sobre o Personagem
    def __str__(self):
        print(f"Explorador\n"
              f"Pontos de vida: {self.pontos_vida}\n"
              f"Pontos de ataque: {self.pontos_ataque}\n"
              f"Porcentagem do tesouro: {self.perc_tesouro}\n"
              f"Posição no mapa: {self.posicao}\n"
              f"Itens: {self.itens}\n")

    # MÉTODOS PARA OS PONTOS DE VIDA DO PERSONAGEM

    # Método para adicionar pontos de vida
    def adicionar_pontos_vida(self, pontos):
        if self.pontos_vida == 100:
            print(f"Você já tem o máximo de pontos de vida.\n")
        else:
            self.pontos_vida += pontos

            if self.pontos_vida > 100:
                self.pontos_vida = 100

            print(f"Você tem {self.pontos_vida} pontos de vida.\n")

    # Método para remover pontos de vida
    def remover_pontos_vida(self, pontos):
        self.pontos_vida -= pontos

        # Se os pontos de vida do Personagem chegarem a zero
        if self.pontos_vida <= 0:
            print(f"Você morreu!\n")

    # Método para retornar se o Personagem está vivo (pontos_vida > 0)
    def esta_vivo(self):
        return self.pontos_vida > 0

    # MÉTODOS PARA OS PONTOS DE ATAQUE DO PERSONAGEM

    # Método para adicionar pontos de ataque
    def adicionar_pontos_ataque(self, pontos):
        self.pontos_ataque += pontos

    # Método para remover pontos de ataque
    def remover_pontos_ataque(self, pontos):
        self. pontos_ataque -= pontos

        # Se os pontos de ataque do Personagem forem reduzidos a menor valor que o mínimo
        if self.pontos_ataque < 20:
            self.pontos_ataque = 20

    # MÉTODOS PARA OS ITENS CARREGADOS PELO PERSONAGEM

    # Método para adicionar item a lista
    def adicionar_item(self, item):
        self.itens.append(item)

    # Método para remover item da lista
    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)
        else:
            print(f"{item} não foi encontrado.\n")

    # MÉTODOS PARA A PORCENTAGEM DO TESOURO CARREGADA PELO PERSONAGEM

    # Método para adicionar a porcentagem do tesouro
    def adicionar_perc_tesouro(self, percentual):
        self.perc_tesouro = percentual

    # Método para remover a porcentagem do tesouro
    def remover_perc_tesouro(self, valor):
        self.perc_tesouro -= valor

        # Se o percentual do tesouro chegou a menos que 0
        if self.perc_tesouro <= 0:
            self.perc_tesouro = 0
            print(f"Você perdeu todo o tesouro que tinha resgatado.\n")

    # MÉTODOS PARA MOVIMENTAÇÃO DO PERSONAGEM

    # Método para o ataque do Personagem
    def atacar(self, criatura):
        dano = random.randint(1, self.pontos_ataque)
        criatura.pontos_vida -= dano
        print(f"Você atacou! Houve {dano} de dano.\n")
        print(f"{criatura.tipo} agora tem {criatura.pontos_vida} pontos de vida.\n")

