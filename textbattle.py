# encoding: utf-8
from random import randint
import time


class Player:
    def __init__(self, args):
        self.name = args[0]
        self.energy = int(args[1])
        self.power = int(args[2])


def main():
    while True:
        try:
            hero = Player(raw_input('Entre a primeira personagem: ').split(' '))
            enemy = Player(raw_input('Entre a segunda personagem: ').split(' '))
            fight(hero, enemy)
            break
        except:
            print('ERRO na criação da personagem. Utilize o formato "nome energia poder"')
            time.sleep(1)
            continue


def fight(hero, enemy):
    print('O jogo começou')
    time.sleep(1)
    print('Batalha entre %s e %s' % (hero.name, enemy.name))
    time.sleep(1.5)

    players = [hero, enemy]
    while hero.energy > 0 and enemy.energy > 0:
        turn(players[0], players[1])
        players.reverse()

    announcewinner(players)


def turn(attacker, defender):
    print('%s atacou %s' % (attacker.name, defender.name))
    luck = randint(0, 100)
    time.sleep(0.5)

    if luck <= 15:
        print('Errou - 0 HP')
    else:
        damage = attacker.power / 3
        if luck <= 70:
            print('Normal - %d HP' % damage)
        elif luck <= 96:
            damage += damage * 0.2
            print('Sorte! - %d HP' % damage)
        elif luck > 96:
            damage += damage
            print('Crítico!!! - %d HP' % damage)
        defender.energy -= damage
    time.sleep(1)


def announcewinner(players):
    time.sleep(1)
    for player in players:
        if player.energy > 0:
            print('Jogo acabou, o vencedor foi %s com HP restante de %d' % (player.name, player.energy))

main()
