from random import randint
from ability_and_armor import Ability, Armor, Weapon
from team import Team
    

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
        return self.kills

    def add_deaths(self, num_deaths):
        ''' Update deaths with num_deaths'''
        self.deaths += num_deaths
        return self.deaths

    

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

        # TODO: double check your while loop

        while self.is_alive() and opponent.is_alive():

            self.take_damage(opponent.hero_attack())
            print(f"self.current healt {self.current_health}")
            opponent.take_damage(self.hero_attack())
            print(f"opponent.current healt {opponent.current_health}")
            
            if self.current_health > 0 and opponent.current_health <= 0:
                # self.add_kill(1)
                # opponent.add_deaths(1)
                # print("{} won!".format(self.name))
                winner = self.name
            elif self.current_health <= 0 and opponent.current_health > 0:
                # opponent.add_kills(1)
                # self.add_deaths(1)
                winner = opponent.name
                # print("{} won!".format(opponent.name))
            # break 
        print(f"Winner is {winner}")
 



if __name__ == "__main__":
    wond_woman = Hero("Wonder Woman")
    dumbledore = Hero("Dumbledore")
    alp = Hero("Alpomish")
    superman = Hero("Superman")

    ability1 = Ability("Super Speed", 30)
    # ability2 = Ability("Super Eyes", 1000)
    ability3 = Ability("Wizard Wand", 80)
    # ability4 = Ability("Wizard Beard", 2000)
    ability5 = Ability("Stregth", 70)
    ability6 = Ability("Flying Speed", 20)
    
    wond_woman.add_ability(ability1)
    # wond_woman.add_ability(ability2)
    dumbledore.add_ability(ability3)
    # dumbledore.add_ability(ability4)
    alp.add_ability(ability5)
    superman.add_ability(ability6)

    team1 = Team("Cupcake")
    team2 = Team("Coffee")
    team1.add_hero(wond_woman)
    team2.add_hero(dumbledore)
    team1.add_hero(alp)
    team2.add_hero(superman)

    team1.team_attack(team2)


    # hero1.fight(hero2)
