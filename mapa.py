import random
import networkx as nx
import matplotlib.pyplot as plt


# Declaração do objeto Mapa (Grafo)
class Mapa:
    # Construtor de inicialização dos atributos do Mapa
    def __init__(self):
        self.grafo = nx.Graph()    # Inicializa um grafo vazio

    # MÉTOTOS PARA OS VÉRTICES DO MAPA

    # Método para adicionar um vértice ao Mapa
    def adicionar_vertice(self, vertice):
        self.grafo.add_node(vertice)

    # Método para adicionar os vértices
    def adicionar_vertices(self, vertices):
        self.grafo.add_nodes_from(vertices)

    # MÉTODOS PARA AS ARESTAS DOS VÉRTICES DO MAPA

    # Método para adicionar uma aresta entre os vértices
    def adicionar_aresta(self, vertice1, vertice2):
        self.grafo.add_edge(vertice1, vertice2)

    # Método para adicionar as arestas
    def adicionar_arestas(self, arestas):
        self.grafo.add_edges_from(arestas)

    # Método para desenhar o Mapa
    def desenhar_mapa(self):
        nx.draw(self.grafo, with_labels=True, node_size=300, node_color='skyblue', font_size=10)
        plt.show()

    # MÉTODOS PARA GERAÇÃO DO MAPA

    # Método para gerar um Mapa com valores aleatórios de vértices
    def gerar_mapa_aleatorio(self):
        num_vertices = random.randint(10, 20)  # Quantidade aleatória de vértices

        self.grafo.add_node(0)  # Adiciona o primeiro vértice (Praia)

        # Adiciona os vértices (localizações) no Mapa
        for i in range(num_vertices):
            self.grafo.add_node(i)  # Adiciona os outros vértices da ilha

        # Adiciona arestas aleatórias (caminhos) entre os vértices (localicações)
        for i in range(num_vertices):
            for j in range(i + 1, num_vertices):
                if random.random() < 0.3:  # Ajusta a probabilidade de ter uma conexão entre os vértices
                    self.grafo.add_edge(i, j)
                # # Conecta o novo vértice a vértices aleatórios já existentes
                # # Gerando um número aleatório com base na quantidade de vertices
                # # Variando de 0 (primeiro vértice) até o vértice atual menos 1
                # vertice_existente = random.randint(0, i - 1)
                # self.grafo.add_edge(vertice_existente, i)

        return self.grafo
