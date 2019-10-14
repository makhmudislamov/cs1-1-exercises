import random


class Ability:
    def __init__(self, name, max_damage):
        '''
        Initialize the values passed into this
        method as instance variables.
        '''
        self.name = name
        self.max_damage = max_damage

    def __str__(self):
        return f'This is ability name {self.name}'

    def attack(self):
        '''
        Use random.randint(a, b) to select a random attack value.
        Return an attack value between 0 and the full attack.
        '''
        attack_value = random.randint(0, self.max_damage)
        return attack_value

class Armor():
    def __init__(self, name, max_block):
        '''
        Initialize the values passed into this
        method as instance variables.
        '''
        self.name = name
        self.max_block = max_block

    def block(self):
        ''' 
        Return a random value between 
        0 and the initialized max_block strength. 
        '''
        block_value = random.randint(0, self.max_block)
        return block_value

    

class Hero:
    def __init__(self, name, starting_health=100):
        '''
        Initialize these values as instance variables:
        (Some of these values are passed in above, others will need to be set at a starting value.)
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
        '''
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)

    def attack(self):
        '''
        Calculates damage from list of abilities.
        This method should call Ability.attack()
        on every ability in self.abilities and
        return the total.
        '''
        damage = 0
        for ability in self.abilities:
            damage += ability.attack()
        return damage

    def add_armor(self, armor):
        '''
        Add armor to self.armors
        Armor: Armor Object
        '''
        self.armors.append(armor)

    def defend(self, damage_amt):
        '''
        Runs `block` method on each armor.
        Returns sum of all blocks
        '''
        damage_amt = 0
        for armor in self.armors:
            damage_amt += armor.block()
        return damage_amt

    def take_damage(self, damage):
        '''
        This method should update self.current_health
        with the damage that is passed in.
        '''
        self.current_health -= damage
        return self.current_health

    def is_alive(self):  
        '''
        This function will
        return true if the hero is alive
        or false if they are not.
        '''
        if self.current_health > 0:
            return True
        else:
            return False

    def fight(self, opponent):
        ''' 
        Current Hero will take turns fighting the opponent hero passed in.
        '''
        print("{} vs {}. FIGHT!".format(self.name, opponent.name))

        # base case: both heroes have no abilities to fight  
        if (not self.abilities) and (not opponent.abilities):
            print("DRAW. The Heroes have no abilites to fight!")

        # self.take_damage(opponent.attack())
        # opponent.take_damage(self.attack())

        # TODO: double check your while loop

        while self.is_alive or opponent.is_alive:

            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())

            # print(self.name, self.take_damage(opponent.attack()))
            # print(opponent.name, opponent.take_damage(self.attack()))
            # print(self.current_health)
            

            # if opponent.take_damage(self.attack()) and self.take_damage(opponent.attack()):
            if self.current_health > 0 and opponent.current_health < 0:
                print("{} won!".format(self.name))
            else:
                print("{} won!".format(opponent.name))
            break 


class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        return random.randint(self.max_damage // 2, self.max_damage)
 



if __name__ == "__main__":

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 30)
    ability2 = Ability("Super Eyes", 10)
    ability3 = Ability("Wizard Wand", 8000)
    ability4 = Ability("Wizard Beard", 2000000)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)

    hero1.fight(hero2)
