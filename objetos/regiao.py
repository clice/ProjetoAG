from colorama import Fore, Style


# Declaração do objeto Região (Partes da Ilha = Vértices)
class Regiao:
    # Construtor de inicialização dos atributos da Região
    def __init__(self, indice, tipo):
        self.indice = indice     # Determina o índice da Região (vértice)
        self.tipo = tipo         # Determina o tipo de Região
        self.perc_tesouro = 0    # Determina o percentual do Tesouro que há na Região
        self.elementos = []      # Lista de elementos (Criaturas ou Itens) na Região
        self.qtd_criaturas = 0   # Quantidade de Criaturas na Região

    # String representando as informações sobre a Região
    def __str__(self):
        print(f"Índice: {self.indice}")
        print(f"Tipo: {self.tipo}")

    # MÉTODOS PARA AS INFORMAÇÕES DA REGIÃO

    # Método para checar qual a Região atual
    def checar_regiao(self, explorador):
        if self.tipo == 'Tesouro':
            print(Fore.CYAN + f"Você chegou ao Tesouro!")
            print(Style.RESET_ALL)  # Restaurar cores
        else:
            if self.elementos:
                for elemento in self.elementos:
                    if elemento.tipo == 'criatura':
                        print(f"{elemento.nome} encontrado(a)! CUIDADO!")
                        explorador.lutar_criatura(elemento)

                    if elemento.tipo == 'perigo':
                        print(f"{elemento.nome} encontrado(a)! CUIDADO!")
                        explorador.remover_pontos_vida(elemento.pontos)  # Remover pontos do Explorador
                        print(f"Você agora tem {explorador.pontos_vida} pontos de vida!")

                    if elemento.tipo == 'planta_medicinal':
                        print(f"{elemento.nome} encontrado(a)!.")

                        while True:
                            resposta = input(f"Deseja utilizar guardar (S/Outro)? ")
                            print()

                            # Verificar resposta do Explorador
                            if resposta.upper() == "S":
                                break

                        explorador.adicionar_item(elemento)  # Adicionar o elemento a lista
                        print(Fore.GREEN + f"Você guardou {elemento.nome} na mochila!")
                        print(Style.RESET_ALL)  # Restaurar cores

                    if elemento.tipo == 'arma':
                        print(f"{elemento.nome} encontrado(a)!.")

                        while True:
                            resposta = input(f"Deseja utilizar guardar (S/Outro)? ")
                            print()

                            # Verificar resposta do Explorador
                            if resposta.upper() == "S":
                                break

                        explorador.adicionar_item(elemento)  # Adicionar o elemento a lista
                        print(Fore.GREEN + f"Você guardou {elemento.nome} na mochila!")
                        print(Style.RESET_ALL)  # Restaurar cores

            print("Continue procurando...\n")

    # MÉTODOS PARA ELEMENTOS NA REGIÃO

    # Método para adicionar elementos na Região
    def adicionar_elementos(self, elemento):
        self.elementos.append(elemento)

        # Se o elemento adicionado for `criatura` soma mais um na quantidade
        if elemento.tipo == 'criatura':
            self.qtd_criaturas += 1

    # Método para retornar se há mais de uma Criatura na Região
    def ha_criaturas(self):
        return self.qtd_criaturas > 1
