# Declaração do objeto Personagem
class Personagem:
    # Construtor de inicialização dos atributos do Personagem
    def __init__(self, pontos_vida=100, pontos_ataque=20, perc_tesouro=0, itens=None):
        self.pontos_vida = pontos_vida                     # Pontos de vida do Personagem
        self.pontos_ataque = pontos_ataque                 # Pontos de ataque do Personagem
        self.perc_tesouro = perc_tesouro                     # Porcentagem do tesouro carregado pelo personagem
        self.itens = itens if itens is not None else []    # Lista de itens carregados pelo Personagem

    # String representando as informações sobre o Personagem
    def __str__(self):
        return (f"Explorador: "
                f"Pontos de vida = {self.pontos_vida}, "
                f"Pontos de ataque = {self.pontos_ataque}, "
                f"Porcentagem do tesouro = {self.perc_tesouro},"
                f"Itens = {self.itens}")

    # MÉTODOS PARA OS PONTOS DE VIDA DO PERSONAGEM

    # Método para adicionar pontos de vida
    def adicionar_pontos_vida(self, pontos):
        if self.pontos_vida == 100:
            print(f"Você já tem o máximo de pontos de vida.\n")
        else:
            self.pontos_vida = self.pontos_vida + pontos

            if self.pontos_vida > 100:
                self.pontos_vida = 100

            print(f"Você tem {self.pontos_vida} pontos de vida.\n")

    # Métofo para remover pontos de vida
    def remover_pontos_vida(self, pontos):
        self.pontos_vida = self.pontos_vida - pontos

        if self.pontos_vida <= 0:
            print(f"Você morreu!\n")

    # MÉTODOS PARA OS PONTOS DE ATAQUE DO PERSONAGEM

    # Método para adicionar pontos de ataque
    def adicionar_pontos_ataque(self, pontos):
        self.pontos_ataque = self.pontos_ataque + pontos

    # Método para remover pontos de ataque
    def remover_pontos_ataque(self, pontos):
        self. pontos_ataque = self.pontos_ataque - pontos

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
        self.perc_tesouro = self.perc_tesouro - valor

        # Se o percentual do tesouro chegou a menos que 0
        if self.perc_tesouro <= 0:
            self.perc_tesouro = 0
            print(f"Você perdeu todo o tesouro que tinha resgatado.\n")
