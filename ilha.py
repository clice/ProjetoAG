import random
import networkx as nx
import matplotlib.pyplot as plt
from regiao import Regiao


# Declaração do objeto Ilha (Grafo)
class Ilha:
    # Construtor de inicialização dos atributos da Ilha
    def __init__(self):
        self.regioes = None                             #
        self.qtd_regioes = random.randint(5, 10)  # Número de Regiões na Ilha (vértices no grafo)
        self.qtd_arestas = 0                            #
        self.ilha = nx.Graph()                          # Inicializa um grafo vazio

    # Método para gerar uma Ilha com valores aleatórios de Regiões (vértices)
    def gerar_ilha(self):
        # Adiciona Regiões a Ilha (vértices ao grafo)
        for i in range(self.qtd_regioes):
            self.ilha.add_node(i)

        # Garante que o grafo gerado é conectado adicionando arestas aleatórias entre os vértices
        for i in range(self.qtd_regioes - 1):
            self.ilha.add_edge(i, i + 1)
            self.qtd_arestas += 1  # Contador para a quantidade de arestas entre os vértices

        # Adiciona mais arestas aleatórias para tornar o grafo mais conectado
        for regiao in range(self.qtd_regioes):
            # Limite de metade da quantidade de Regiões (arendondando)
            qtd_arestas = random.randint(0, self.qtd_regioes // 2)

            # Laço percorrendo a quantidade de arestas geradas aleatoriamente
            for _ in range(qtd_arestas):
                adjacente = random.randint(0, self.qtd_regioes - 1)

                # Se a Região adjacente for diferente da Região atual, adicionar como Região adjacente a atual
                if adjacente != regiao:
                    self.ilha.add_edge(regiao, adjacente)

    # Método para desenhar a Ilha
    def desenhar_ilha(self):
        nx.draw(self.ilha, with_labels=True)
        plt.show()
