# from random import randint
from ability_and_armor import *

    

class Hero(object):
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
        self.deaths = 0
        self.kills = 0
        
    def add_kill(self, num_kills):
        ''' Update kills with num_kills'''
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        '''Update deaths with num_deaths'''
        self.deaths += num_deaths

    

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)
        

    def hero_attack(self):
        '''
        Calculates damage from list of abilities.
        This method should call Ability.attack()
        on every ability in self.abilities and
        return the total.
        '''
        damage = 0
        for ability in self.abilities:
            damage += ability.ability_attack()
        
        return damage

    def add_armor(self, armor):
        '''
        Add armor to self.armors
        Armor: Armor Object
        '''
        self.armors.append(armor)

    def defend(self):
        '''
        Runs `block` method on each armor.
        Returns sum of all blocks
        '''
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        '''
        This method should update self.current_health
        with the damage that is passed in.
        '''
        
        blocked = self.defend()
        damage -= blocked
        self.current_health -= damage

    def is_alive(self):  
        '''
        This function will
        return true if the hero is alive
        or false if they are not.
        '''
        if self.current_health > 0:
            return True
        
        return False

    def fight(self, opponent):
        ''' 
        Current Hero will take turns fighting the opponent hero passed in.
        '''
        # Note to self:
        # This method was the most fun to work on. 
        # It implements several other methods of this class
        # The method generated couple of bugs, caused interesting debates with my peers 
        # and needed special attention during pair programming.
        #
        # I might come back again to this method as it is called in my future classes (Team)
        print(f"{self.name} vs {opponent.name}. FIGHT!")

        # base case: both heroes have no abilities to fight  
        if (not self.abilities) and (not opponent.abilities):
            print("DRAW. The Heroes have no abilites to fight!")

        fighting = True
        while fighting:

            # first hero is attacking
            print(f"{opponent.name} is attacking...")
            self.take_damage(opponent.hero_attack())
            print(f"{self.name}\'s current health {self.current_health}")
            if not self.is_alive():
                winner = opponent.name
                break
            # second hero is attacking
            print(f"{self.name} is attacking...")
            opponent.take_damage(self.hero_attack())
            print(f"{opponent.name}\'s current health {opponent.current_health}")
  
            if not opponent.is_alive():
                winner = self.name
                break

        if winner == opponent.name:
            opponent.add_kill(1)
            self.add_deaths(1)
            print(f"{self.name} deaths = {self.deaths}")
            print(f"{opponent.name} kills = {opponent.kills}")
            
        else:
            self.add_kill(1)
            opponent.add_deaths(1)
            print(f"{self.name} kills = {self.kills}")
            print(f"{opponent.name} deaths = {opponent.deaths}")

        return winner



