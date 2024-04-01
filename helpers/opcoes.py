import random
from colorama import Fore, Style


# Função para o remover os pontos de vida do atacado com base nos pontos de ataque do atacante
def atacar(atacante, atacado):
    dano = random.randint(1, atacante.pontos_ataque)
    atacado.pontos_vida -= dano
    return dano


# LUTA ENTRE O EXPLORADOR E UMA CRIATURA

# Função para a luta entre o Explorador e a Criatura
def lutar(explorador, criatura):
    while True:
        resposta = input(f"Deseja lutar com {criatura.nome} (S/Outro)? ")

        # Verificar resposta do Explorador
        if resposta.upper() != "S":
            # Gerar dano no Explorador
            dano = atacar(criatura, explorador)
            print(Fore.RED + f"Você sofreu {dano} de dano!")

            # Caso o Explorador morra com o ataque
            if not explorador.esta_vivo():
                explorador.reviver()
            else:
                print(f"Você agora tem {explorador.pontos_vida} pontos de vida.")

            break

        rodada = 1  # Rodada inicial

        # Se o Explorador optar por lutar contra a Criatura
        while rodada <= 3:
            print(f"\nROUND {rodada}")

            # Condições para os ataques
            # Primeiro o Explorador ataca a Criatura
            if explorador.esta_vivo() and criatura.esta_viva():
                dano = atacar(explorador, criatura)  # Calcular o dano gerado pelo Explorador
                item = explorador.tem_armas()                # Se o Esplorador tem armas para

                if item:
                    item.remover_qtd_uso()  # Diminuir a quantidade de uso do Item

                    # Caso a quantidade de uso seja menor que 1
                    if item.qtd_uso < 0:
                        explorador.remover_item(item)

                print(Fore.GREEN + f"Você atacou! Houve {dano} de dano.")

                # Teste para saber se a Criatura morreu com o ataque
                if not criatura.esta_viva():
                    print(Fore.YELLOW + f"\n{criatura.nome.upper()} MORREU!")
                    # criatura.reviver_criatura()
                    break
                else:
                    print(f"{criatura.nome} agora tem {criatura.pontos_vida} pontos de vida.")

            # Segundo a Criatura ataca o Explorador
            if criatura.esta_viva() and explorador.esta_vivo():
                dano = atacar(criatura, explorador)
                print(Fore.RED + f"{criatura.nome.upper()} ATACOU! Houve {dano} de dano.")

                # Teste para saber se o Explorador morreu com o ataque
                if not explorador.esta_vivo():
                    explorador.reviver()
                    break
                else:
                    print(f"Você agora tem {explorador.pontos_vida} pontos de vida.")

            print(Style.RESET_ALL)  # Restaurar cores

            # Se as três rodadas ainda não terminaram nem o Explorador ou Criatura morreram
            if rodada <= 2:
                # Perguntar novamente para continuar a luta
                resposta = input(f"Deseja continuar lutando com {criatura.nome}? (S/Outro)? ")

                # Verificar resposta do Explorador
                if resposta.upper() != "S":
                    break

            rodada += 1  # Acrescentar rodada concluida

        # Se os pontos de vida do Explorador chegarem a zero
        if not explorador.esta_vivo() or not criatura.esta_viva():
            print(Style.RESET_ALL)  # Restaurar cores
            break


# MÉTODOS PARA LUTA ENTRE ENTRE CRIATURAS


# Método para a luta entre as Criaturas
def lutar_criatura(self, criatura):
    # Se a Criatura é mais fraca que a outra
    if self.pontos_ataque < criatura.pontos_ataque:
        dano = self.atacar_criatura(criatura)
        print(Fore.GREEN + f"{self.tipo} atacou! Houve {dano} de dano.")
        print(Style.RESET_ALL)  # Restaurar cores
        print(f"{criatura.tipo} agora tem {criatura.pontos_vida} pontos de vida.")
        return criatura
    # Se a Criatura é mais forte que a outra
    elif self.pontos_ataque > criatura.pontos_ataque:
        dano = self.atacar_criatura(criatura)
        print(Fore.GREEN + f"{self.tipo} atacou! Houve {dano} de dano.")
        print(f"{criatura.tipo} agora tem {criatura.pontos_vida} pontos de vida.")
        print(Style.RESET_ALL)  # Restaurar cores
        return criatura
