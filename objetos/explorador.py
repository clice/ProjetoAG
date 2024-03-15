import random


# Declaração do objeto Explorador
class Explorador:
    # Construtor de inicialização dos atributos do Explorador
    def __init__(self):
        self.pontos_vida = 100   # Pontos de vida do Explorador
        self.pontos_ataque = 20  # Pontos de ataque do Explorador
        self.perc_tesouro = 0    # Porcentagem do tesouro carregado pelo Explorador
        self.regiao = 0          # Posição do Explorador no mapa (grafo)
        self.armas = None        # Lista de Armas carregadas pelo Explorador

    # String representando as informações sobre o Explorador
    def __str__(self):
        print(f"Pontos de vida: {self.pontos_vida}")
        print(f"Pontos de ataque: {self.pontos_ataque}")
        print(f"Porcentagem do tesouro: {self.perc_tesouro}")
        print(f"Região no mapa: {self.regiao}")

        if self.armas is None:
            print(f"Armas: Nenhuma arma coletada\n")
        else:
            print(f"Armas: {self.armas}\n")

    # MÉTODOS PARA OS PONTOS DE VIDA DO EXPLORADOR

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

        # Se os pontos de vida do Explorador chegarem a zero
        if self.pontos_vida <= 0:
            print(f"Você morreu!\n")

    # Método para retornar se o Explorador está vivo (pontos_vida > 0)
    def esta_vivo(self):
        return self.pontos_vida > 0

    # MÉTODOS PARA OS PONTOS DE ATAQUE DO EXPLORADOR

    # Método para adicionar pontos de ataque
    def adicionar_pontos_ataque(self, pontos):
        self.pontos_ataque += pontos

    # Método para remover pontos de ataque
    def remover_pontos_ataque(self, pontos):
        self. pontos_ataque -= pontos

        # Se os pontos de ataque do Explorador forem reduzidos a menor valor que o mínimo
        if self.pontos_ataque < 20:
            self.pontos_ataque = 20

    # MÉTODOS PARA OS ITENS CARREGADOS PELO EXPLORADOR

    # Método para adicionar Arma a lista
    def adicionar_arma(self, arma):
        self.armas.append(arma)

        # Remover percentual do tesouro carregado por conta da arma
        if self.perc_tesouro > 0:
            self.perc_tesouro -= arma.pontos_ataque

    # Método para remover Arma da lista
    def remover_arma(self, arma):
        if arma in self.armas:
            self.armas.remove(arma)
        else:
            print(f"{arma.tipo} não foi encontrada.\n")

    # MÉTODOS PARA A PORCENTAGEM DO TESOURO CARREGADA PELO EXPLORADOR

    # Método para adicionar a porcentagem do tesouro
    def adicionar_perc_tesouro(self):
        percentual = self.pontos_vida

        for arma in self.armas:
            # Calcular o percentual correto para o Explorador carregar o tesouro
            percentual -= arma.pontos_ataque

        self.perc_tesouro = percentual

    # Método para remover a porcentagem do tesouro
    def remover_perc_tesouro(self, valor):
        self.perc_tesouro -= valor

        # Se o percentual do tesouro chegou a menos que 0
        if self.perc_tesouro <= 0:
            self.perc_tesouro = 0
            print(f"Você perdeu todo o tesouro que tinha resgatado.\n")

    # MÉTODOS PARA MOVIMENTAÇÃO DO EXPLORADOR

    # Método para o ataque do Explorador contra a Criatura
    def atacar_criatura(self, criatura):
        dano = random.randint(1, self.pontos_ataque)
        criatura.pontos_vida -= dano
        print(f"Você atacou! Houve {dano} de dano.")
        print(f"{criatura.tipo} agora tem {criatura.pontos_vida} pontos de vida.\n")

    # Método para a luta entre o Explorador e a Criatura
    def lutar_criatura(self, criatura):
        resposta = True

        while resposta:
            resposta = input(f"Deseja lutar com {criatura.tipo} (S/N)? ")

            if resposta == "S" or resposta == "s":
                for _ in range(3):
                    if self.esta_vivo() and criatura.esta_viva():
                        self.atacar_criatura(criatura)
                    if criatura.esta_viva() and self.esta_vivo():
                        criatura.atacar_explorador(self)
                resposta = False

            elif resposta == "N" or resposta == "n":
                print(f"Você fugiu! ")
                resposta = False

            else:
                print(f"Opção inválida!")
