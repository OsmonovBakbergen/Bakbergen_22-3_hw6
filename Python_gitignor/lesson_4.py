import random



class SuperAbiliti():
    CRITICAL_DAMAGE = 1
    HEAL = 2
    BOOST = 3
    SAVE_DAMAGE_AND_REVERT = 4


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
        return self.__health = 0
    else:
    
    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        return self.__damage

class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super(Boss, self).__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

class Hero(GameEntity):
    def __init__(self, name, health, damage, super_abiliti):
        super(Hero, self).__init__(name, health, damage)
        self.__super_abiliti = super_abiliti

    def hit(self, boss):
        boss.health -= self.damage

class Warrior(Hero):
    def __init__(self, name, health, damage):
        super(Warrior, self).__init__(name, health, damage, SuperAbiliti.CRITICAL_DAMAGE)

class Mag(Hero):
    def __init__(self, name, health, damage):
        super(Mag, self).__init__(name, health, damage, SuperAbiliti.BOOST)

class Medic(Hero):
    def __init__(self, name, health, damage):
        super(Medic, self).__init__(name, health, damage, SuperAbiliti.HEAL)

class Berserk(Hero):
    def __init__(self, name, health, damage):
        super(Berserk, self).__init__(name, health, damage, SuperAbiliti.SAVE_DAMAGE_AND_REVERT)

def print_statistics(boss, heroes):
    print()


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.hit(heroes)
    for hero in heroes:
        if hero.health > 0 and hero.super.abiliti != boss.defence:
            hero.hit(boss)
            hero.apply_super.power(boss, heroes)
    print_statistics(boss,heroes)

def start_game():
    boss = Boss("Aid", 1000, 50)

    warrior = Warrior("Ahiles", 270, 10)

    heroes = [Warrior, ]