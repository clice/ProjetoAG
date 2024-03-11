# Declaração do objeto Arma
class Arma(object):
    # Construtor de inicialização dos atributos da Arma
    def __init__(self, tipo, pontos_ataque):
        self.tipo = tipo                    # Nome do tipo da Arma
        self.pontos_ataque = pontos_ataque  # Pontos de ataque da Arma
        self.uso = 3                        # Quantidade de uso restante da Arma

    # Método para remover a quantidade de uso da Arma
    def remover_uso(self):
        self.uso -= 1
