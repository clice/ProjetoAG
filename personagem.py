# Declaração do objeto Personagem
class Personagem:
    # Construtor de inicialização dos atributos do Personagem
    def __init__(self, pontos_vida=100, pontos_ataque=20, per_tesouro=0, itens=None):
        self.pontos_vida = pontos_vida                     # Pontos de vida do Personagem
        self.pontos_ataque = pontos_ataque                 # Pontos de ataque do Personagem
        self.per_tesouro = per_tesouro                     # Porcentagem do tesouro carregado pelo personagem
        self.itens = itens if itens is not None else []    # Lista de itens carregados pelo Personagem

    # String representando as informações sobre o Personagem
    def __str__(self):
        return (f"Explorador: "
                f"Pontos de vida = {self.pontos_vida}, "
                f"Pontos de ataque = {self.pontos_ataque}, "
                f"Porcentagem do tesouro = {self.per_tesouro},"
                f"Itens = {self.itens}")

    # MÉTODOS PARA OS PONTOS DE VIDA DO PERSONAGEM

    # Método para adicionar pontos de vida
    def adicionar_pontos_vida(self, pontos):
        if self.pontos_vida == 100:
            print(f"O Explorador já tem o máximo de pontos de vida.\n")
        else:
            self.pontos_vida = self.pontos_vida + pontos

            if self.pontos_vida > 100:
                self.pontos_vida = 100

            print(f"O Explorador tem {self.pontos_vida} pontos de vida.\n")

    # Métofo para remover pontos de vida
    def remover_pontos_vida(self, pontos):
        self.pontos_vida = self.pontos_vida - pontos

        if self.pontos_vida <= 0:
            print(f"O Explorador morreu!\n")

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
