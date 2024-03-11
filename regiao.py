import random


# Declaração do objeto Região (Partes da Ilha = Vértices)
class Regiao(object):
    regioes = ('Praia', 'Montanha', 'Lago', 'Paredão de Rocha', 'Riacho', 'Floresta')

    # Construtor de inicialização dos atributos da Região
    def __init__(self, tipo):
        self.indice = 0          # Determina o índice da Região (vértice)
        self.num_adjacentes = 0  # Inicializa a região sem vértices adjacantes
        self.tipo = tipo         # Determina o tipo de Região
        self.criaturas = None    # Lista de criaturas na Região
        self.perigos = None      # Lista de perigos na Região
        self.armas = None        # Lista de armas na Região
        self.itens = None        # Lista de itens de cura na Região

    # OUTROS MÉTODOS

    # Método para sortear os perigos na Região
    def sortear_perigos(self):
        # Lista dos Perigos da Ilha
        perigos = (
            'Passagens escorregadias à beira do abismo',
            'Animais selvagens perigosos ou venenosos',
            'Poço de areia movediça e de piche',
            'Plantas venenosas com frutos chamativos e aparentemente suculentos'
        )

        nome_criatura = random.choice(list(criaturas.keys()))
        stats = criaturas[nome_criatura]
        return nome_criatura, stats
