import random


# Declaração do objeto Criatura
class Criatura(object):
    # Construtor de inicialização dos atributos da Criatura
    def __init__(self, tipo, pontos_vida, pontos_ataque, descricao, regiao):
        self.tipo = tipo                    # Nome do tipo da Criatura
        self.pontos_vida = pontos_vida      # Pontos de vida da Criatura
        self.pontos_ataque = pontos_ataque  # Pontos de ataque da Criatura
        self.descricao = descricao          # Descrição da Criatura
        self.regiao = regiao                # Região da Criatura no mapa (grafo)

    # String representado as informações sobre a Criatura
    def __str__(self):
        print(f"Criatura")
        print(f"Pontos de vida: {self.pontos_vida}")
        print(f"Pontos de ataque: {self.pontos_ataque}")
        print(f"Descrição: {self.descricao}\n")

    # MÉTODOS PARA OS PONTOS DE VIDA DA CRIATURA

    # Método para remover pontos de vida
    def remover_pontos_vida(self, pontos):
        self.pontos_vida -= pontos

        # Se os pontos de vida da Criatura chegarem a zero
        if self.pontos_vida <= 0:
            print(f"{self.tipo} morreu!\n")

    # Método para retornar se a Criatura está viva (pontos_vida > 0)
    def esta_viva(self):
        return self.pontos_vida > 0

    # MÉTODOS PARA MOVIMENTAÇÃO DA CRIATURA

    # Método para o ataque da Criatura contra o Personagem
    def atacar_personagem(self, personagem):
        dano = random.randint(1, self.pontos_ataque)
        personagem.pontos_vida -= dano
        print(f"{self.tipo} atacou! Houve {dano} de dano.")
        print(f"Você agora tem {personagem.pontos_vida} pontos de vida.\n")

    # Método para a luta entre a Criatura e o Personagem
    def lutar_personagem(self, personagem):
        for _ in range(3):
            if self.esta_viva() and personagem.esta_vivo():
                self.atacar_personagem(personagem)
            if personagem.esta_vivo() and self.esta_viva():
                personagem.atacar_criatura(self)


# OUTROS MÉTODOS

# Método para sortear o tipo da Criatura
def sortear_criatura():
    # Dicionário das Criaturas da Ilha
    criaturas = (
        {
            "nome": "Crocodilo Gigante",
            "pontos_vida": 50,
            "pontos_ataque": 10,
            "descricao": "Crocodilo gigante de 8 metros de comprimento, possuindo "
                         "pele dura, além de bastante força e mordida poderosa"
        },
        {
            "nome": "Formiga Quimera",
            "pontos_vida": 50,
            "pontos_ataque": 10,
            "descricao": "Formigas quimera, que podem desossar um boi em poucos minutos, "
                         "apesar de frágeis individualmente"
        },
        {
            "nome": "Onça Pintada",
            "pontos_vida": 50,
            "pontos_ataque": 10,
            "descricao": "Orça pintada mítica, que consegue se camuflar quase que "
                         "perfeitamente, e possui o tamanho de um touro, com garras "
                         "e dentes poderosos"
        }
    )

    return random.choice(criaturas)
