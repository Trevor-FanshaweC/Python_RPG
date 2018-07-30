import random

class bcolors:
    HEADER = '\033[95n'
    DKBLUE = '\033[94n'
    DKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, name, hp, mp, attack, defense, magic, items, money):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.attack_low = attack - 10
        self.attack_high = attack + 10
        self.defense = defense
        self.magic = magic
        self.actions = ["Attack", "Magic", "Items"]
        self.items = items
        self.money  = money

    def generate_damage(self):
        return random.randrange(self.attack_low, self.attack_high)

    def take_damage(self, dmg):
        self.hp -= dmg

        if self.hp < 0:
            self.hp = 0

        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp
    
    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def get_cash(self):
        return self.money

    def use_item(self, cost):
        self.money -= cost

        if self.money < 0:
            self.money = 0

        return self.money

    def heal(self, pts):
        self.hp += pts

        if self.hp > self.max_hp:
            self.hp = self.max_hp

        return self.hp
    
    def reduce_mp(self, cost):
        self.mp -= cost

    def generate_cash(self, amt):
        self.money += amt

    def choose_target(self, targets):
        i = 1
        print("TARGET:")
        
        for target in targets:
            print("    " + str(i) + "." + target.name)
            i += 1
        
        choice = int(input("Choose target:")) - 1
        return choice            
    
    def choose_action(self):
        i = 1
        print("\n" + bcolors.BOLD + self.name + bcolors.ENDC)
        print("Actions")
        for item in self.actions:
            print("  " + str(i) + ":", item)
            i += 1
    
    def choose_magic(self):
        i = 1
        print("\nMagic\n")
        for spell in self.magic:
            print("  " + str(i) + ":", spell.name, "(Cost: "+ str(spell.cost) + " SP)")
            i += 1

    def choose_item(self):
        i = 1
        print("\nItems\n")
        for item in self.items:
            print("  " + str(i) + ":", item.name, "(Cost: "+ str(item.cost) + " SP)")
            i += 1
    
    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.max_hp) * 100 / 2

        while bar_ticks > 0:
            hp_bar += "*"
            bar_ticks -= 1
        
        while len(hp_bar) < 50:
            hp_bar += " "

        print("\n" + bcolors.FAIL + self.name + ": " + str(self.hp) + "/" + str(self.max_hp) + "   |" + hp_bar + "|" + bcolors.ENDC)


    #generate stat bars
    def get_stats(self):
        hp_bar = ""
        mp_bar = ""
        # generate ticks
        bar_ticks = (self.hp / self.max_hp) * 100 / 4
        mp_ticks = (self.mp / self.max_mp) * 100 / 10

        while bar_ticks > 0:
            hp_bar += "*"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "*"
            mp_ticks -= 1
        
        while len(mp_bar) < 10:
            mp_bar += " "


        print("                  _________________________            __________")
        print(self.name + ": " + str(self.hp) + "/" + str(self.max_hp) + "   |" + hp_bar + "|    " + str(self.mp) + "/" + str(self.max_mp) + " |" + mp_bar + "|" )
