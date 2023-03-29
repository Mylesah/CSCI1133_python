
#==========================================
# Purpose: Adventurer objects are the base class for characters for the rpg game
# Instance variables: name: string, level: integer, strength: integer,
# speed: integer, power: integer, HP: integer derived from the integer of self.level, hidden: boolian
# each instance variable represents an attribute of the Adventurer class
# Methods: __repr__: overloads repr() with specail formating, attack: uses the instance variables
# to determine an attack between two Adventurer base class characters
#==========================================
class Adventurer:
    def __init__(self, name, level, strength, speed, power):
        self.name = name
        self.level = level
        self.strength = strength
        self.speed = speed
        self.power = power
        self.HP = self.level * 6
        self.hidden = False

    def __repr__(self):
        return '{} - HP: {}'.format(self.name, self.HP)
        
    def attack(self, target):
        if target.hidden == True:
            print('{} can\'t see {}'.format(self.name, target.name))
        else:
            damage = self.strength + 4
            target.HP -= damage
            print('{} attacks {} for {} damage'.format(self.name, target.name, damage))

#==========================================
# Purpose: Thief is a new class derived from Adventurer class
# Instance variables: same as base class
# Methods: same as base class but overrides the attack() function with specail thief sneak attack
#==========================================
class Thief(Adventurer):
    def __init__(self, name, level, strength, speed, power):
        super().__init__(name, level, strength, speed, power)
        self.HP = self.level * 8
        self.hidden = True

    def attack(self, target):
        if self.hidden == False:
            Adventurer.attack(self, target)
        else: #sneak attack
            damage = (self.speed + self.level)*5
            target.HP -= damage
            self.hidden = False
            target.hidden = False
            print('{} sneak attacks {} for {} damage'.format(self.name, target.name, damage))

#==========================================
# Purpose: Ninja is new class derived from the Theief class
# Instance variables: same as base class
# Methods: sames as Thief base class, but overrides the attack() function
#==========================================
class Ninja(Thief):
    def __init__(self, name, level, strength, speed, power):
        super().__init__(name, level, strength, speed, power)
        self.HP = self.level * 8
        self.hidden = True

    def attack(self, target):
        Thief.attack(self, target)
        self.hidden = True
        self.HP += self.level

#==========================================
# Purpose: Mage is a new class derived from Adventurer class
# Instance variables: same as base class and new instance variable fireballs_left: which is integer representing num of fireballs
# Methods: same as base class but overrides the attack() function with new fireball attack option
#==========================================
class Mage(Adventurer):
    def __init__(self, name, level, strength, speed, power):
        super().__init__(name, level, strength, speed, power)
        self.HP = self.level * 6
        self.hidden = False
        self.fireballs_left = self.power

    def attack(self, target):
        if self.fireballs_left == 0:
            Adventurer.attack(self, target)
        else:
            damage = self.level * 3
            self.fireballs_left -= 1
            target.HP -= damage
            target.hidden = False
            print('{} casts fireball on {} for {} damage'.format(self.name, target.name, damage))
            
#==========================================
# Purpose: Wizard is a new class derived from Mage class
# Instance variables: same as base class
# Methods: same as Mage base class 
#==========================================
class Wizard(Mage):
    def __init__(self, name, level, strength, speed, power):
        super().__init__(name, level, strength, speed, power)
        self.fireballs_left = self.power * 2
        self.HP = self.level * 4



#helper function for battle()
#prints the remaing Adventurer objects in player_list
def player_print(player_list): 
    print('Your team:')
    for i in range(len(player_list)):
        print(player_list[i])

#helper function for battle()
#prints the remaing Adventurer objects in player_list
def enemy_print(enemy_list):
    print('')
    for idx, enemy in enumerate(enemy_list, start = 1):
        print('Enemy',idx,':',enemy)

#helper function for battle()
#allows player to choose their attack target with user input 
def player_attack(player_list, enemy_list):
    print('\n----------Player Turn----------')
    player_print(player_list)
    for i in range(len(player_list)):
        enemy_print(enemy_list)
        player_up = player_list[i]
        enemy_idx = int(input('Choose a target for {}: '.format(player_up.name))) - 1
        enemy = enemy_list[enemy_idx]
        player_up.attack(enemy)
        if enemy.HP <= 0:
            print('{} was defeated!'.format(enemy.name))
            enemy_list.remove(enemy)
        if len(enemy_list) == 0:
            print('You win!')
            return True

#helper function for battle()
#enemy Adventurer objects attack player's objects based on lowest HP and lowest list index
def enemy_attack(player_list, enemy_list):
    print('\n----------Enemy Turn----------')
    for enemy_up in enemy_list:
        HP_list = []
        for i in player_list:
            HP_list.append(i.HP)
        weakest_idx = HP_list.index(min(HP_list))
        weakest = player_list[weakest_idx]
        enemy_up.attack(weakest)
        if weakest.HP <= 0:
            print('{} was defeated!'.format(weakest.name))
            player_list.remove(weakest)
        if len(player_list) == 0:
            print('You lose!')
            return True

#battle function calls the helper functions as long as there are Adventurer objects left in either player_list or enemy_list
def battle(player_list, enemy_list):
    while len(player_list) > 0 and len(enemy_list) > 0:
        if player_attack(player_list, enemy_list) == True:
           return player_list      
        if enemy_attack(player_list, enemy_list) == True:
            return enemy_list
            
