from colorama import Fore, Style


# Declaração do objeto Região (Partes da Ilha = Vértices)
class Regiao:
    # Construtor de inicialização dos atributos da Região
    def __init__(self, indice, tipo, tesouro):
        self.indice = indice    # Determina o índice da Região (vértice)
        self.tipo = tipo        # Determina o tipo de Região
        self.tesouro = tesouro  # Determina o percentual do Tesouro que há na Região
        self.criaturas = []     # Lista de Criaturas na Região
        self.itens = []         # Lista de Itens na Região

    # String representando as informações sobre a Região
    def __str__(self):
        print(f"Índice: {self.indice}")
        print(f"Tipo: {self.tipo}")

    # MÉTODOS PARA A QUANTIDADE PERCENTUAL DO TESOURO NA REGIÃO

    # Método para remover o percentual do tesouro da Região
    def remover_tesouro(self, tesouro):
        self.tesouro -= tesouro

    # MÉTODOS PARA AS CRIATURAS NA REGIÃO

    # Métoro para adicionar Criatura na Região
    def adicionar_criatura(self, criatura):
        self.criaturas.append(criatura)

    # Método para retornar se há Criaturas na Região
    def ha_criaturas(self):
        return bool(self.criaturas)

    # MÉTODOS PARA OS ITENS NA REGIÃO

    # Método para adicionar Item na Região
    def adicionar_item(self, item):
        self.itens.append(item)

    # Método para remover Item da Região
    def remover_item(self, item):
        self.itens.remove(item)

    # MÉTODOS PARA AS INFORMAÇÕES DA REGIÃO

    # Método para checar qual a Região atual
    def checar_regiao(self, explorador):
        if self.tipo == 'Tesouro':
            print(Fore.CYAN + f"Você chegou ao Tesouro!")
            print(Style.RESET_ALL)  # Restaurar cores
        else:
            if self.itens:
                for item in self.itens:
                    if item.tipo == 'criatura':
                        print(f"{item.nome} encontrado(a)! CUIDADO!")
                        explorador.lutar_criatura(item)

                    if item.tipo == 'perigo':
                        print(f"{item.nome} encontrado(a)! CUIDADO!")
                        explorador.remover_pontos_vida(item.pontos)  # Remover pontos do Explorador
                        print(f"Você agora tem {explorador.pontos_vida} pontos de vida!")

                    if item.tipo == 'planta_medicinal':
                        print(f"{item.nome} encontrado(a)!.")

                        while True:
                            resposta = input(f"Deseja utilizar guardar (S/Outro)? ")
                            print()

                            # Verificar resposta do Explorador
                            if resposta.upper() == "S":
                                break

                        explorador.adicionar_item(item)  # Adicionar o elemento a lista
                        print(Fore.GREEN + f"Você guardou {item.nome} na mochila!")
                        print(Style.RESET_ALL)  # Restaurar cores

                    if item.tipo == 'arma':
                        print(f"{item.nome} encontrado(a)!.")

                        while True:
                            resposta = input(f"Deseja utilizar guardar (S/Outro)? ")
                            print()

                            # Verificar resposta do Explorador
                            if resposta.upper() == "S":
                                break

                        explorador.adicionar_item(item)  # Adicionar o elemento a lista
                        print(Fore.GREEN + f"Você guardou {item.nome} na mochila!")
                        print(Style.RESET_ALL)  # Restaurar cores

            print("Continue procurando...\n")
