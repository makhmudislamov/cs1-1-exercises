from random import randint
from ability_and_armor import *
from team import *
    

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
        else:
            return False

    def fight(self, opponent):
        ''' 
        Current Hero will take turns fighting the opponent hero passed in.
        '''
        print(f"{self.name} vs {opponent.name}. FIGHT!")
        # winner = ''
        # base case: both heroes have no abilities to fight  
        if (not self.abilities) and (not opponent.abilities):
            print("DRAW. The Heroes have no abilites to fight!")

        while self.is_alive() and opponent.is_alive():
            # first hero is attacking
            self.take_damage(opponent.hero_attack())
            print(f"self.current health {self.current_health}")
            # second hero is attacking
            opponent.take_damage(self.hero_attack())
            print(f"opponent.current health {opponent.current_health}")

        if not self.is_alive():
            opponent.add_kill(1)
            self.add_deaths(1)
            print(f" opp_kill = {opponent.kills}")
            print(f" self_death = {self.deaths}")
            
        elif not opponent.is_alive():
            self.add_kill(1)
            opponent.add_deaths(1)
            print(f"self kills {self.kills}")
            print(f"opp deth {opponent.deaths}")
        # determining the winner
        winner = self.name if self.is_alive() else opponent.name
        print(f"{winner} won!")

 


if __name__ == "__main__":

    # THIS IS TEST FOR TEAM
    # wond_woman = Hero("Wonder Woman")
    # dumbledore = Hero("Dumbledore")
    # alp = Hero("Alpomish")
    # superman = Hero("Superman")

    # ability1 = Ability("Super Speed", 30)
    # # ability2 = Ability("Super Eyes", 1000)
    # ability3 = Ability("Wizard Wand", 80)
    # # ability4 = Ability("Wizard Beard", 2000)
    # ability5 = Ability("Stregth", 70)
    # ability6 = Ability("Flying Speed", 20)
    
    # wond_woman.add_ability(ability1)
    # # wond_woman.add_ability(ability2)
    # dumbledore.add_ability(ability3)
    # # dumbledore.add_ability(ability4)
    # alp.add_ability(ability5)
    # superman.add_ability(ability6)

    # team1 = Team("Cupcake")
    # team2 = Team("Coffee")
    # team1.add_hero(wond_woman)
    # team2.add_hero(dumbledore)
    # team1.add_hero(alp)
    # team2.add_hero(superman)

    # team1.team_attack(team2)


    # TEST FOR HERO ATTACK
    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 300)
    # ability2 = Ability("Super Eyes", 130)
    # ability3 = Ability("Wizard Wand", 80)
    # ability4 = Ability("Wizard Beard", 20)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # team = Team("Super")
    # team.add_hero(hero1)
    # team.add_hero(hero2)
    # team.view_all_heroes()
    # team.remove_hero("Wonder Woman")
    # team.view_all_heroes()
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 800)
    ability4 = Ability("Wizard Beard", 200)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
    # hero1.fight(hero2)
