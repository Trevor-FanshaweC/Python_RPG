from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

import random

# black magic spells!
fire = Spell("Fire", 10, 60, "black")
thunder = Spell("Thunder", 15, 80, "black")
blizzard = Spell("Blizzard", 20, 80, "black")
meteor = Spell("Meteor", 20, 100, "black")
quake = Spell("Quake", 25, 120, "black")

#white magic spells!
cure = Spell("Cure", 12, 100, "white")
cureall = Spell("CureAll", 10, 100, "white")

#create some items
potion = Item("Potion", "potion", "Heals 50 HP", 50, 50)
hipotion = Item("Power-potion", "potion", "Heals 100 HP", 100, 75)
superpotion = Item("Super Potion", "potion", "Heals 200 HP", 200, 100)
elixer = Item("Elixer", "elixer", "Restores HP/MP for one member", 5000, 200) #this should really be max_hp
hielixer = Item("Super Elixer", "elexir", "Restores everyones HP / MP", 5000, 500) #this should be max_hp

# weapon items
grenade = Item("Grenade", "weapon", "Deals 500 damage", 50, 50)
flamethrower = Item("FlameThrower", "weapon", "Deals 250 damage to all enemies", 150, 100)
crossbow = Item("Crossbow", "weapon", "Deals 400 damage", 100, 80)

player_magic = [fire, thunder, blizzard, meteor, cure, cureall]
player_items = [potion, hipotion, superpotion, elixer, hielixer, grenade, flamethrower, crossbow]

player1 = Person("Mario", 460, 65, 60, 34, player_magic, player_items, 1000)
player2 = Person("J    ", 500, 80, 60, 50, player_magic, player_items, 800)
player3 = Person("Longo", 450, 40, 60, 80, player_magic, player_items, 800)

players = [player1, player2, player3]

enemy = Person("boogerface", 1200, 65, 45, 25, [], [], 0)
enemy2 = Person("goober", 800, 60, 80, 20, [], [], 0)
enemy3 = Person("gooberface", 800, 60, 80, 20, [], [], 0)
print("Enemy hit points:", enemy.hp)

enemies = [enemy, enemy2, enemy3]
running = True

count = 0

while running:
    print("========================")
    print("\n")
    print("NAME               HP                                    MP")

    #loop thru stats
    for player in players:
         #print out stats
        player.get_stats()
        #print("\n")
    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        player.choose_action()
        choice = input("\nChoose Action:")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            player.generate_cash(5)

            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)            
            
            print("You attacked " + enemies[enemy].name + " for", dmg, "points of damage. Enemy HP:", enemies[enemy].get_hp())

            reward = random.randrange(5, 30)
            print("You got", reward, "coins for that attack!")

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name + "has been defeated, yo!")
                del enemies[enemy]

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose Spell:")) -1

            spell = player.magic[magic_choice]

            magic_dmg = spell.generate_spell_damage()        
            #cost = spell.cost

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue
            
            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(spell.dmg)
                print(bcolors.DKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "pts" + bcolors.ENDC)
            elif spell.type == "black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print(bcolors.DKBLUE + "\nYour", spell.name, "deals", magic_dmg, "damage to " + enemies[enemy].name + "!\n" + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + "has been defeated, yo!")
                    del enemies[enemy]

        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose Item:")) - 1

            item = player.items[item_choice]
            print("You chose", item.name, "which is a", item.type, "and has", item.prop, "power and costs", item.cost)
            #item_dmg = item.prop

            current_cash = player.get_cash()

            if current_cash < item.cost:
                print("You don't have enough cash to use that")
                continue 
            
            if item.type == "weapon":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                
                print(bcolors.DKBLUE + "\nYour", item.name, "deals", item.prop, "damage to " + enemies[enemy].name + "!\n" + bcolors.ENDC)
                print("You got 5 coins from that attack")

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + "has been defeated, yo!")
                    del enemies[enemy]

            elif item.type == "potion":
                player.heal(item.prop)
                print(bcolors.DKBLUE + "Healed player for" + str(item.prop) + "Player HP:"+ str(player.get_hp()) + bcolors.ENDC)
            elif item.type == "elexir":
                if item.name == "Super Elixer":
                    for player in players:
                        player.hp = player.max_hp
                        player.mp = player.max_mp
                        print("Everyone's good to go!")
                else:
                    player.hp = player.max_hp
                    player.mp = player.max_mp
                    print("/nTopped up, son! HP:", player.get_hp(), "MP:", player.get_mp())                

            player.use_item(item.cost)
            print("\nYou have", player.get_cash(), "cash left")

    for enemy in enemies:
        enemy_choice = 1

        target = random.randrange(0, 3)
        #active_enemy = random.randrange(0, 3)

        enemy_dmg = enemy.generate_damage()
        players[target].take_damage(enemy_dmg)

        print("Enemy attacks", players[target].name, "for",  enemy_dmg, "Player HP:", players[target].get_hp())
        print("========================")

    defeated_enemies = 0
    defeated_players = 0

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    if defeated_enemies == 2:
        print(bcolors.DKGREEN + "You Win!!" + bcolors.ENDC)
        running = False
    elif defeated_players == 2:
        print(bcolors.FAIL + "You were defeated, yo!" + bcolors.ENDC)
        running = False
  #running = False
