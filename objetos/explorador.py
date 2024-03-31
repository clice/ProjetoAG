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
                print(item)

    # MÉTODOS PARA OS PONTOS DE VIDA DO EXPLORADOR

    # Método para adicionar pontos de vida
    def adicionar_pontos_vida(self, pontos):
        if self.pontos_vida == 100:
            print(f"Você já tem o máximo de pontos de vida.\n")
        else:
            self.pontos_vida += pontos

            if self.pontos_vida > 100:
                self.pontos_vida = 100

            print(f"Você tem {self.pontos_vida} pontos de vida.\n")

    # Método para remover pontos de vida
    def remover_pontos_vida(self, pontos):
        self.pontos_vida -= pontos

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
            tesouro -= item.pontos_ataque

        self.tesouro = tesouro

    # Método para remover tesouro
    def remover_tesouro(self, tesouro):
        self.tesouro -= tesouro

        # Se o percentual do tesouro chegou a menos que 0
        if self.tesouro <= 0:
            self.tesouro = 0
            print(f"Você perdeu todo o tesouro que tinha resgatado.\n")

    # MÉTODOS PARA A REGIÃO DO EXPLORADOR

    # Método para atualizar a Região que o Explorador está
    def atualizar_regiao(self, ilha):
        print(Fore.MAGENTA + f"Localização atual: {self.regiao.tipo}.")
        print(Style.RESET_ALL)  # Restaurar cores

        while True:
            resposta = input("Deseja avançar para um lugar aleatório (S/Outro)? ")
            print()

            # Verificar resposta do Explorador
            if resposta.upper() != "S":
                break

            adjacentes = list(ilha.mapa.neighbors(self.regiao.tipo))  # Regiões adjacentes da Região atual
            self.regiao = ilha.encontrar_regiao(random.choice(adjacentes))  # Atualizar a região

            print(Fore.MAGENTA + f"Localização atual: {self.regiao.tipo}.")
            print(Style.RESET_ALL)  # Restaurar cores
            break

    # MÉTODOS PARA OS ITENS CARREGADOS PELO EXPLORADOR

    # Método para adicionar Item a lista
    def adicionar_item(self, item):
        self.itens.append(item)

        # Remover percentual do tesouro carregado por conta da arma
        if self.tesouro > 0:
            self.tesouro -= item.pontos_ataque

    # Método para remover Item da lista
    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)
        else:
            print(f"{item.tipo} não foi encontrado(a).\n")
            
    # MÉTODOS PARA A QUANTIDADE DE MOVIMENTOS DO EXPLORADOR
    
    # Método para remover a quantidade de movimentos do Explorador
    def remover_qtd_movimentos(self):
        self.qtd_movimentos -= 1

    # MÉTODOS PARA CONFERÊNCIA DO BACKUP

    # Método para adicionar o backup das informações do Explorador quando encontrar um checkpoint
    def adicionar_backup(self):
        self.backup = {
            'pontos_vida': self.pontos_vida,
            'pontos_ataque': self.pontos_ataque,
            'tesouro': self.tesouro,
            'regiao': self.regiao,
            'itens': self.itens
        }

    # Método para atualizar os dados do Explorador com os dados do backup
    def atualizar_dados(self):
        self.pontos_vida = self.backup['pontos_vida']
        self.pontos_ataque = self.backup['pontos_ataque']
        self.tesouro = self.backup['tesouro']
        self.regiao = self.backup['regiao']
        self.itens = self.backup['itens']
                
    # MÉTODOS PARA LUTA ENTRE O EXPLORADOR E UMA CRIATURA

    # Método para o ataque do Explorador contra a Criatura
    def atacar_criatura(self, criatura):
        dano = random.randint(1, self.pontos_ataque)
        criatura.pontos_vida -= dano
        return dano

    # Método para a luta entre o Explorador e a Criatura
    def lutar_criatura(self, criatura):
        while True:
            resposta = input(f"Deseja lutar com {criatura.nome} (S/Outro)? ")

            # Verificar resposta do Explorador
            if resposta.upper() != "S":
                dano = criatura.atacar_explorador(self)
                print(Fore.RED + f"Você sofreu {dano} de dano!")
                print(f"Você agora tem {self.pontos_vida} pontos de vida.")

                # Teste para saber se o Explorador morreu com o ataque
                if not self.esta_vivo():
                    print(Fore.YELLOW + f"Você morreu!")

                break

            rodada = 1  # Rodada inicial

            while rodada <= 3:
                print(f"\nROUND {rodada}")

                # Condições para os ataques
                # Primeiro o Explorador ataca a Criatura
                if self.esta_vivo() and criatura.esta_viva():
                    dano = self.atacar_criatura(criatura)
                    print(Fore.GREEN + f"Você atacou! Houve {dano} de dano.")
                    print(f"{criatura.nome} agora tem {criatura.pontos_vida} pontos de vida.")

                # Teste para saber se a Criatura morreu com o ataque
                if not criatura.esta_viva():
                    print(Fore.YELLOW + f"\n{criatura.nome} morreu!")
                    break

                # Segundo a Criatura ataca o Explorador
                if criatura.esta_viva() and self.esta_vivo():
                    dano = criatura.atacar_explorador(self)
                    print(Fore.RED + f"{criatura.nome} atacou! Houve {dano} de dano.")
                    print(f"Você agora tem {self.pontos_vida} pontos de vida.")

                # Teste para saber se o Explorador morreu com o ataque
                if not self.esta_vivo():
                    print(Fore.YELLOW + f"Você morreu!")
                    break

                print(Style.RESET_ALL)  # Restaurar cores

                # Se os pontos de vida do Explorador chegarem a zero
                if not self.esta_vivo() or not criatura.esta_viva():
                    resposta = False
                    break
                # Se as três rodadas ainda não terminaram nem o Explorador ou Criatura morreram
                elif rodada <= 2:
                    # Perguntar novamente para continuar a luta
                    resposta = input(f"Deseja continuar lutando com {criatura.nome}? (S/Outro)? ")

                    # Verificar resposta do Explorador
                    if resposta.upper() != "S":
                        break

                # Acrescentar rodada concluida
                rodada += 1

            # Se os pontos de vida do Explorador chegarem a zero
            if not self.esta_vivo() or not criatura.esta_viva():
                print(Style.RESET_ALL)  # Restaurar cores
                break
