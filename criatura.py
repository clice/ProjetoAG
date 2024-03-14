import random


# Declaração do objeto Criatura
class Criatura:
    # Construtor de inicialização dos atributos da Criatura
    def __init__(self, tipo, pontos_vida, pontos_ataque, descricao, regiao):
        self.tipo = tipo                    # Nome do tipo da Criatura
        self.pontos_vida = pontos_vida      # Pontos de vida da Criatura
        self.pontos_ataque = pontos_ataque  # Pontos de ataque da Criatura
        self.descricao = descricao          # Descrição da Criatura
        self.regiao = regiao                # Região (vértice) da Criatura no mapa (grafo)

    # String representado as informações sobre a Criatura
    def __str__(self):
        print(f"Criatura: {self.tipo}")
        print(f"Pontos de vida: {self.pontos_vida}")
        print(f"Pontos de ataque: {self.pontos_ataque}")
        print(f"Descrição: {self.descricao}")
        print(f"Região: {self.regiao}\n")

    # MÉTODOS PARA OS PONTOS DE VIDA DA CRIATURA

    # Método para remover pontos de vida
    def remover_pontos_vida(self, pontos):
        self.pontos_vida -= pontos

        # Se os pontos de vida da Criatura chegarem a zero
        if self.pontos_vida <= 0:
            print(f"{self.tipo} morreu!\n")

    # Método para retornar se a Criatura está viva (pontos_vida > 0)
    def esta_viva(self):
        return self.pontos_vida > 0

    # MÉTODOS PARA MOVIMENTAÇÃO DA CRIATURA

    # Método para o ataque da Criatura contra o Explorador
    def atacar_explorador(self, explorador):
        dano = random.randint(1, self.pontos_ataque)
        explorador.pontos_vida -= dano
        print(f"{self.tipo} atacou! Houve {dano} de dano.")
        print(f"Você agora tem {explorador.pontos_vida} pontos de vida.\n")

    # Método para a luta entre a Criatura e o Explorador
    def lutar_explorador(self, explorador):
        for _ in range(3):
            if self.esta_viva() and explorador.esta_vivo():
                self.atacar_explorador(explorador)
            if explorador.esta_vivo() and self.esta_viva():
                explorador.atacar_criatura(self)

    # # Método para a luta entre as Criaturas
    # def lutar_criatura(self, criatura2):
    #     for _ in range(3):
    #         if self.esta_viva() and criatura2.esta_viva():
    #             self.ata
