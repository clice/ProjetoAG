import random
import networkx as nx
import matplotlib.pyplot as plt
from objetos.regiao import Regiao


# Declaração do objeto Ilha (Grafo)
class Ilha:
    # Construtor de inicialização dos atributos da Ilha
    def __init__(self):
        self.ilha = nx.Graph()                          # Inicializa um grafo vazio
        self.regioes = None                             #
        self.qtd_regioes = random.randint(5, 10)  # Número de Regiões na Ilha (vértices no grafo)
        self.qtd_arestas = 0                            #
        self.criaturas = []                             # Lista de Criaturas na Ilha
        self.armas = []                                 # Lista de Armas na Ilha
        self.perigos = []                               # Lista de Perigos na Ilha
        self.checkpoints = []                           # Lista de Regiões que são checkpoints

    # MÉTODOS PARA GERAR E MANIPULAR O GRAFO DA ILHA

    # Método para gerar uma Ilha com valores aleatórios de Regiões (vértices)
    def gerar_ilha(self):
        # Adiciona Regiões a Ilha (vértices ao grafo)
        for i in range(self.qtd_regioes):
            if i == 0:
                self.ilha.add_node("Praia")
            elif i == self.qtd_regioes - 1:
                self.ilha.add_node("Tesouro")
            else:
                self.ilha.add_node(i)

        # Garante que o grafo gerado é conectado adicionando arestas aleatórias entre os vértices
        for i in range(self.qtd_regioes - 1):
            if i == 0:
                self.ilha.add_edge("Praia", i + 1)
            elif i == self.qtd_regioes - 2:

                self.ilha.add_edge(i, "Tesouro")
            else:
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
                    if not self.ilha.has_edge(regiao, adjacente):
                        self.qtd_arestas += 1  # Contador para a quantidade de arestas entre os vértices

                        if adjacente == 0:
                            self.ilha.add_edge(regiao, "Praia")
                        elif adjacente == self.qtd_regioes - 1:
                            self.ilha.add_edge(regiao, "Tesouro")
                        else:
                            self.ilha.add_edge(regiao, adjacente)

    # Método para desenhar a Ilha
    def desenhar_ilha(self, regiao_atual):
        # Posição das Regiões (vértices) Position nodes using the spring layout algorithm
        pos = nx.spring_layout(self.ilha)

        # Desenhar o grafo com: Regiões padrão cor "sky blue", arestas em preto e fonte negrito
        nx.draw(self.ilha, pos, with_labels=True, node_color='skyblue', edge_color='black', font_weight='bold', node_size=3000)

        # Destacar a Região atual que o Explorador está com a cor "red"
        nx.draw_networkx_nodes(self.ilha, pos, nodelist=[regiao_atual], node_color='red', node_size=3000)

        # Destacar

        # Salvar imagem do mapa
        # plt.savefig('mapa.png')

        # Display the graph
        plt.show()

    # OUTROS MÉTODOS

    # Método para gerar a quantidade de elementos
    def sortear_qtd_elementos(self):
        return round(self.qtd_regioes * (random.randint(20, 30) / 100))

    # Método para adicionar os checkpoints
    def adicionar_checkpoints(self):
        self.checkpoints = random.sample(range(1, self.qtd_regioes), self.sortear_qtd_elementos())

    # Método para remover um checkpoint depois de usado
    def remover_checkpoint(self, checkpoint):
        self.checkpoints.remove(checkpoint)
