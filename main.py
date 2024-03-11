# from ilha import Ilha
#
# # Gerar Ilha do jogo aleatoriamente
# ilha = Ilha()
# ilha.gerar_ilha_aleatoria()
# ilha.desenhar_ilha()

import random


# class Character:
#     def __init__(self, name, life_points, attack_points):
#         self.name = name
#         self.life_points = life_points
#         self.attack_points = attack_points
#
#     def __str__(self):
#         return f"{self.name}: Life Points={self.life_points}, Attack Points={self.attack_points}"
#
#     def attack(self, target):
#         damage = random.randint(1, self.attack_points)
#         target.life_points -= damage
#         print(f"{self.name} attacked {target.name} for {damage} damage!")
#         print(f"{target.name} now has {target.life_points} life points.")
#
#     def is_alive(self):
#         return self.life_points > 0
#
#     def fight(self, creature):
#         for _ in range(3):
#             if self.is_alive() and creature.is_alive():
#                 self.attack(creature)
#             if creature.is_alive() and self.is_alive():
#                 creature.attack(self)
#
# class Creature:
#     def __init__(self, name, life_points, attack_points):
#         self.name = name
#         self.life_points = life_points
#         self.attack_points = attack_points
#
#     def __str__(self):
#         return f"{self.name}: Life Points={self.life_points}, Attack Points={self.attack_points}"
#
#     def attack(self, target):
#         damage = random.randint(1, self.attack_points)
#         target.life_points -= damage
#         print(f"{self.name} attacked {target.name} for {damage} damage!")
#         print(f"{target.name} now has {target.life_points} life points.")
#
#     def is_alive(self):
#         return self.life_points > 0
#
#     def fight(self, character):
#         for _ in range(3):
#             if self.is_alive() and character.is_alive():
#                 self.attack(character)
#             if character.is_alive() and self.is_alive():
#                 character.attack(self)
#
#
# # Example usage
# hero = Character("Hero", 100, 20)
# monster = Creature("Monster", 80, 15)
#
# print(f"Hero has {hero.life_points} and Moster has {monster.life_points}.\n")
#
# hero.fight(monster)
from criatura import Criatura
from personagem import Personagem


# personagem = Personagem()
# personagem.__str__()

criatura = sortear_criatura()

print(f"Nome: {criatura['nome']}\n"
      f"Pontos de vida: {criatura['pontos_vida']}\n"
      f"Pontos de ataque: {criatura['pontos_ataque']}\n"
      f"Descrição: {criatura['descricao']}\n")
