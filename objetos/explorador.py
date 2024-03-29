import random

from colorama import Fore, Style


# Declaração do objeto Explorador
class Explorador:
    # Construtor de inicialização dos atributos do Explorador
    def __init__(self):
        self.pontos_vida = 100      # Pontos de vida do Explorador
        self.pontos_ataque = 20     # Pontos de ataque do Explorador
        self.perc_tesouro = 0       # Porcentagem do tesouro carregado pelo Explorador
        self.indice = 0             # Índice do local que o Explorador está no mapa (grafo)
        self.tipo_regiao = 'Praia'  # Nome do tipo de Região que o Explorador está no mapa (grafo)
        self.armas = None           # Lista de Armas carregadas pelo Explorador
        self.backup = {}            # Backup do Explorador quando encontrar um checkpoint

    # String representando as informações sobre o Explorador
    def __str__(self):
        print(f"Pontos de vida: {self.pontos_vida}")
        print(f"Pontos de ataque: {self.pontos_ataque}")
        print(f"Porcentagem do tesouro: {self.perc_tesouro}")
        print(f"Índice: {self.indice}")
        print(f"Região atual: {self.tipo_regiao}")

        if self.armas is None:
            print(f"Armas: Nenhuma arma coletada\n")
        else:
            print(f"Armas: {self.armas}\n")

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
        self. pontos_ataque -= pontos

        # Se os pontos de ataque do Explorador forem reduzidos a menor valor que o mínimo
        if self.pontos_ataque < 20:
            self.pontos_ataque = 20

    # MÉTODOS PARA A PORCENTAGEM DO TESOURO CARREGADA PELO EXPLORADOR

    # Método para adicionar a porcentagem do tesouro
    def adicionar_perc_tesouro(self):
        percentual = self.pontos_vida

        for arma in self.armas:
            # Calcular o percentual correto para o Explorador carregar o tesouro
            percentual -= arma.pontos_ataque

        self.perc_tesouro = percentual

    # Método para remover a porcentagem do tesouro
    def remover_perc_tesouro(self, valor):
        self.perc_tesouro -= valor

        # Se o percentual do tesouro chegou a menos que 0
        if self.perc_tesouro <= 0:
            self.perc_tesouro = 0
            print(f"Você perdeu todo o tesouro que tinha resgatado.\n")

    # MÉTODOS PARA MOVIMENTAÇÃO DO EXPLORADOR

    # Método para atualizar a Região que o Explorador está
    def atualizar_regiao(self, indice, tipo_regiao):
        self.indice = indice
        self.tipo_regiao = tipo_regiao

    # Método para realizar a movimentação do Explorador de uma Região a outra
    def movimentacao(self, ilha):
        print(f"Localização atual: {self.tipo_regiao}.")

        while True:
            resposta = input("Deseja avançar para um lugar aleatorio? (S/Outro)? ")

            # Verificar resposta do Explorador
            if resposta.upper() != "S":
                break

            # Buscar regiões adjacentes a região atual
            regioes_adjacentes = list(ilha.encontrar_regioes_adjacantes(self.tipo_regiao))

            # Escolher aleatoriamente uma Região para o Explorador ir
            tipo_regiao = random.choice(regioes_adjacentes)

            # Encontrar as informações da Região escolhida
            nova_regiao = ilha.encontrar_regiao(tipo_regiao)

            self.atualizar_regiao(nova_regiao.indice, nova_regiao.tipo)

            print(f"Localização atual: {self.tipo_regiao}.")

            nova_regiao.checar_regiao()

    # MÉTODOS PARA OS ITENS CARREGADOS PELO EXPLORADOR

    # Método para adicionar Arma a lista
    def adicionar_arma(self, arma):
        self.armas.append(arma)

        # Remover percentual do tesouro carregado por conta da arma
        if self.perc_tesouro > 0:
            self.perc_tesouro -= arma.pontos_ataque

    # Método para remover Arma da lista
    def remover_arma(self, arma):
        if arma in self.armas:
            self.armas.remove(arma)
        else:
            print(f"{arma.tipo} não foi encontrada.\n")

    # MÉTODOS PARA CONFERÊNCIA DO BACKUP

    # Método para fazer o backup das informações do Explorador quando encontrar um checkpoint
    def realizar_backup(self):
        self.backup = {
            'pontos_vida': self.pontos_vida,
            'pontos_ataque': self.pontos_ataque,
            'perc_tesouro': self.perc_tesouro,
            'regiao': self.regiao,
            'armas': self.armas
        }

    # Método para atualizar os dados do Explorador com os dados do backup
    def atualizar_dados(self):
        self.pontos_vida = self.backup['pontos_vida']
        self.pontos_ataque = self.backup['pontos_ataque']
        self.perc_tesouro = self.backup['perc_tesouro']
        self.regiao = self.backup['regiao']
        self.armas = self.backup['armas']
                
    # MÉTODOS PARA LUTA ENTRE O EXPLORADOR E UMA CRIATURA

    # Método para o ataque do Explorador contra a Criatura
    def atacar_criatura(self, criatura):
        dano = random.randint(1, self.pontos_ataque)
        criatura.pontos_vida -= dano
        return dano

    # Método para a luta entre o Explorador e a Criatura
    def lutar_criatura(self, criatura):
        while True:
            resposta = input(f"Deseja lutar com {criatura.tipo} (S/Outro)? ")

            # Verificar resposta do Explorador
            if resposta.upper() != "S":
                break

            rodada = 1  # Rodada inicial

            while rodada <= 3:
                print(f"\nROUND {rodada}")

                # Condições para os ataques
                # Primeiro o Explorador ataca a Criatura
                if self.esta_vivo() and criatura.esta_viva():
                    dano = self.atacar_criatura(criatura)
                    print(Fore.GREEN + f"Você atacou! Houve {dano} de dano.")
                    print(f"{criatura.tipo} agora tem {criatura.pontos_vida} pontos de vida.")

                # Teste para saber se a Criatura morreu com o ataque
                if not criatura.esta_viva():
                    print(Fore.YELLOW + f"\n{criatura.tipo} morreu!")
                    break

                # Segundo a Criatura ataca o Explorador
                if criatura.esta_viva() and self.esta_vivo():
                    dano = criatura.atacar_explorador(self)
                    print(Fore.RED + f"{criatura.tipo} atacou! Houve {dano} de dano.")
                    print(f"Você agora tem {self.pontos_vida} pontos de vida.")

                # Teste para saber se o Explorador morreu com o ataque
                if not self.esta_vivo():
                    print(Fore.YELLOW + f"Você morreu!")
                    break

                # Restaurar cores
                print(Style.RESET_ALL)

                # Se os pontos de vida do Explorador chegarem a zero
                if not self.esta_vivo() or not criatura.esta_viva():
                    resposta = False
                    break
                # Se as três rodadas ainda não terminaram nem o Explorador ou Criatura morreram
                elif rodada <= 2:
                    # Perguntar novamente para continuar a luta
                    resposta = input(f"Deseja continuar lutando com {criatura.tipo}? (S/Outro)? ")

                    # Verificar resposta do Explorador
                    if resposta.upper() != "S":
                        break

                # Acrescentar rodada concluida
                rodada += 1

            # Se os pontos de vida do Explorador chegarem a zero
            if not self.esta_vivo() or not criatura.esta_viva():
                # Restaurar cores
                print(Style.RESET_ALL)
                break
