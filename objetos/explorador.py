import random

from colorama import Fore, Style


# Declaração do objeto Explorador
class Explorador:
    # Construtor de inicialização dos atributos do Explorador
    def __init__(self, regiao, qtd_movimentos):
        self.pontos_vida = 100                # Pontos de vida do Explorador
        self.pontos_ataque = 20               # Pontos de ataque do Explorador
        self.tesouro = 0                      # Porcentagem do tesouro carregado pelo Explorador
        self.regiao = regiao                  # Região que o Explorador se encontra atualmente
        self.itens = []                       # Lista de Itens carregadas pelo Explorador
        self.qtd_movimentos = qtd_movimentos  # Quantidade de movimentos restantes do Explorador
        self.backup = {}                      # Backup do Explorador quando encontrar um checkpoint

    # String representando as informações sobre o Explorador
    def __str__(self):
        print(f"Pontos de vida: {self.pontos_vida}")
        print(f"Pontos de ataque: {self.pontos_ataque}")
        print(f"Porcentagem do tesouro: {self.tesouro}")
        print(f"Movimentos restantes: {self.qtd_movimentos}")

        if not self.itens:
            print(f"Itens: Nenhum item coletado\n")
        else:
            print(f"Itens:")
            for item in self.itens:
                print("{")
                item.__str__()
                print("}\n")

    # MÉTODOS PARA OS PONTOS DE VIDA DO EXPLORADOR

    # Método para adicionar pontos de vida
    def adicionar_pontos_vida(self, pontos):
        if self.pontos_vida == 100:
            print(f"Você já tem o máximo de pontos de vida.\n")
        else:
            self.pontos_vida += pontos

            # Pontos de vida não podem passar de 100
            if self.pontos_vida > 100:
                self.pontos_vida = 100

            print(f"Você tem {self.pontos_vida} pontos de vida.\n")

    # Método para remover pontos de vida
    def remover_pontos_vida(self, pontos):
        self.pontos_vida -= pontos
        
        # Caso chegue a pontos de vida negativos
        if self.pontos_vida < 0:
            self.reviver_explorador()

    # Método para retornar se o Explorador está vivo (pontos_vida > 0)
    def esta_vivo(self):
        return self.pontos_vida > 0

    # MÉTODOS PARA OS PONTOS DE ATAQUE DO EXPLORADOR

    # Método para adicionar pontos de ataque
    def adicionar_pontos_ataque(self, pontos):
        self.pontos_ataque += pontos

    # Método para remover pontos de ataque
    def remover_pontos_ataque(self, pontos):
        self.pontos_ataque -= pontos

        # Se os pontos de ataque do Explorador forem reduzidos a menor valor que o mínimo
        if self.pontos_ataque < 20:
            self.pontos_ataque = 20

    # MÉTODOS PARA O TESOURO CARREGADA PELO EXPLORADOR

    # Método para adicionar tesouro
    def adicionar_tesouro(self):
        tesouro = self.pontos_vida

        # Calcular o percentual correto para o Explorador carregar o tesouro
        for item in self.itens:
            tesouro -= item.pontos

        self.tesouro = tesouro

    # Método para remover tesouro
    def remover_tesouro(self, tesouro):
        self.tesouro -= tesouro

        # Se o percentual do tesouro chegou a menos que 0
        if self.tesouro <= 0:
            self.tesouro = 0
            print(f"Você perdeu todo o tesouro que tinha resgatado.\n")

    # MÉTODOS PARA A REGIÃO DO EXPLORADOR
    
    # Função para mover Explorador de Região
    def mover(self, ilha):
        while input("Deseja avançar para uma região aleatória (S/Outro)? ").upper() == "S":
            print()
            adjacentes = list(ilha.mapa.neighbors(self.regiao.tipo))        # Regiões adjacentes da Região atual
            self.regiao = ilha.encontrar_regiao(random.choice(adjacentes))  # Atualizar a região
            self.mostrar_regiao()                                           # Mostrar localização atual
            break

    # Método para mostrar a localização atual
    def mostrar_regiao(self):
        print(Fore.MAGENTA + f"Localização atual: {self.regiao.tipo}.")
        print(Style.RESET_ALL)  # Restaurar cores

    # MÉTODOS PARA OS ITENS CARREGADOS PELO EXPLORADOR

    # Método para adicionar Item a lista
    def adicionar_item(self, item):
        self.itens.append(item)

        # Remover percentual do tesouro carregado por conta da arma
        if self.tesouro > 0:
            self.tesouro -= item.pontos

    # Método para remover Item da lista
    def remover_item(self, item):
        if item in self.itens:
            self.remover_pontos_ataque(item.pontos)  # Remover os pontos de ataque do Explorador pelo Item
            self.itens.remove(item)
        else:
            print(f"{item.tipo} não foi encontrado(a).\n")

    # Método para quando o Explorador possui Arma
    def ha_armas(self):
        if self.itens:
            for item in self.itens:
                # Caso o Item seja do tipo Arma
                if item.tipo == 'arma':
                    item.remover_qtd_uso()  # Diminuir a quantidade de uso do Item

                    # Caso a quantidade de uso seja menor que 1
                    if item.qtd_uso < 0:
                        self.remover_item(item)

    # Método para quando o Explorador encontrar um Perigo
    def encontrar_perigo(self, perigo):
        print(Fore.YELLOW + f"{perigo.nome} encontrado(a)! CUIDADO!")
        print(Style.RESET_ALL)  # Restaurar cores

        self.remover_pontos_vida(perigo.pontos)  # Remover pontos do Explorador

        print(Fore.RED + f"Você agora tem {self.pontos_vida} pontos de vida!")
        print(Style.RESET_ALL)  # Restaurar cores

    # Método para quando o Explorador encontrar uma Planta Medicinal
    def encontrar_planta_medicinal(self, planta_medicinal):
        print(Fore.YELLOW + f"{planta_medicinal.nome} encontrado(a)!")
        print(Style.RESET_ALL)  # Restaurar cores

        resposta = input(f"Deseja utilizar (S/Outro)? ")
        print()

        # Verificar resposta do Explorador
        if resposta.upper() == "S":
            self.regiao.remover_item(planta_medicinal)  # Remover o item da Região
            self.adicionar_pontos_vida(planta_medicinal.pontos)  # Adicionar pontos de ataque da Arma

    # Método para quando o Explorador encontrar uma Arma
    def encontrar_arma(self, arma):
        print(Fore.YELLOW + f"{arma.nome} encontrado(a)!")
        print(Style.RESET_ALL)  # Restaurar cores

        resposta = input(f"Deseja guardar (S/Outro)? ")
        print()

        # Verificar resposta do Explorador
        if resposta.upper() == "S":
            self.adicionar_item(arma)  # Adicionar o elemento a lista
            self.regiao.remover_item(arma)  # Remover o item da Região
            self.adicionar_pontos_ataque(arma.pontos)  # Adicionar pontos de ataque da Arma

            print(Fore.GREEN + f"Você guardou {arma.nome} na mochila!")
            print(f"Você agora tem {self.pontos_ataque} pontos de ataque!")
            print(Style.RESET_ALL)  # Restaurar cores

    # MÉTODOS PARA A QUANTIDADE DE MOVIMENTOS DO EXPLORADOR
    
    # Método para remover a quantidade de movimentos do Explorador
    def remover_qtd_movimentos(self):
        self.qtd_movimentos -= 1
        
    # Método para reviver o Explorador caso ainda haja movimentos disponíveis
    def reviver_explorador(self):
        print(Fore.YELLOW + f"VOCÊ MORREU!")
        
        self.atualizar_explorador()
            
        print(Fore.YELLOW + f"Agora será revivido, voltando para {self.regiao.tipo}.")
        print(Style.RESET_ALL)  # Restaurar cores 

    # MÉTODOS PARA CONFERÊNCIA DO BACKUP

    # Método para adicionar o backup das informações do Explorador quando encontrar um checkpoint
    def adicionar_backup(self):
        self.backup = {
            'pontos_vida': 100,
            'pontos_ataque': self.pontos_ataque,
            'tesouro': self.tesouro,
            'regiao': self.regiao,
            'itens': [],
            'qtd_movimentos': self.qtd_movimentos,
            'backup': self.backup
        }

    # Método para atualizar os dados do Explorador com os dados do backup
    def atualizar_explorador(self):
        self.pontos_vida = self.backup['pontos_vida']
        self.pontos_ataque = self.backup['pontos_ataque']
        self.tesouro = self.backup['tesouro']
        self.regiao = self.backup['regiao']
        self.itens = self.backup['itens'],
        self.qtd_movimentos = self.backup['qtd_movimentos'],
        self.backup = self.backup['backup']
