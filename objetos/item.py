from colorama import Fore, Style


# Declaração do objeto Arma
class Item:
    # Construtor de inicialização dos atributos da Arma
    def __init__(self, nome, tipo, pontos, qtd_uso, regiao):
        self.nome = nome        # Nome do Item
        self.tipo = tipo        # Tipo do Item
        self.pontos = pontos    # Pontos do Item
        self.qtd_uso = qtd_uso  # Quantidade de uso do Item
        self.regiao = regiao    # Região (vértice) do Item no mapa (grafo)

    # String representando as informações sobre a Arma
    def __str__(self):
        print(f"Nome: {self.nome}")
        print(f"Tipo: {self.tipo}")
        print(f"Pontos: {self.pontos}")
        print(f"Usos: {self.qtd_uso}")
        
    # MÉTODO PARA A QUANTIDADE DE USO DO ITEM

    # Método para remover a quantidade de uso do Item
    def remover_qtd_uso(self):
        self.qtd_uso -= 1
        
    # MÉTODOS PARA QUANDO OS ITENS FOREM ENCONTRADOS
    
    # Método para quando o Explorador encontrar um Perigo
    def encontrar_perigo(self, explorador):
        print(Fore.YELLOW + f"{self.nome} encontrado(a)! CUIDADO!")
        print(Style.RESET_ALL)  # Restaurar cores
        
        explorador.remover_pontos_vida(self.pontos)  # Remover pontos do Explorador
        
        print(Fore.RED + f"Você agora tem {explorador.pontos_vida} pontos de vida!")
        print(Style.RESET_ALL)  # Restaurar cores
    
    # Método para quando o Explorador encontrar uma Planta Medicinal
    def encontrar_planta_medicinal(self, explorador):
        print(Fore.YELLOW + f"{self.nome} encontrado(a)!")
        print(Style.RESET_ALL)  # Restaurar cores
        
        resposta = input(f"Deseja utilizar ou guardar (S/Outro)? ")
        print()

        # Verificar resposta do Explorador
        if resposta.upper() == "S":
            explorador.adicionar_item(self)                # Adicionar o elemento a lista
            explorador.regiao.remover_item(self)           # Remover o item da Região
            explorador.adicionar_pontos_vida(self.pontos)  # Adicionar pontos de ataque da Arma
            
            print(Fore.GREEN + f"Você guardou {self.nome} na mochila!")
            print(Style.RESET_ALL)  # Restaurar cores
            
    # Método para quando o Explorador encontrar uma Arma
    def encontrar_arma(self, explorador):
        print(Fore.YELLOW + f"{self.nome} encontrado(a)!")
        print(Style.RESET_ALL)  # Restaurar cores
        
        resposta = input(f"Deseja guardar (S/Outro)? ")
        print()

        # Verificar resposta do Explorador
        if resposta.upper() == "S":
            explorador.adicionar_item(self)                  # Adicionar o elemento a lista
            explorador.regiao.remover_item(self)             # Remover o item da Região
            explorador.adicionar_pontos_ataque(self.pontos)  # Adicionar pontos de ataque da Arma
            
            print(Fore.GREEN + f"Você guardou {self.nome} na mochila!")
            print(f"Você agora tem {explorador.pontos_ataque} pontos de ataque!")
            print(Style.RESET_ALL)  # Restaurar cores
    
