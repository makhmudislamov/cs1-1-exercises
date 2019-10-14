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

        # TODO: double check your while loop

        while self.is_alive or opponent.is_alive:

            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
            
            if self.current_health > 0 and opponent.current_health < 0:
                self.add_kill(1)
                opponent.add_deaths(1)
                print("{} won!".format(self.name))
            else:
                opponent.add_kills(1)
                self.add_deaths(1)
                print("{} won!".format(opponent.name))
            break 


class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        return random.randint(self.max_damage // 2, self.max_damage)
 

class Team:
    
    def __init__(self, name):
        ''' 
        Initialize your team with its team name
        '''
        self.name = name
        self.heroes = list()

    def add_hero(self, hero):
        '''
        Adding heroes to a team
        '''
        self.heroes.append(hero)

    def remove_hero(self, name):
        '''
        Removing heroes from the team
        If Hero isn't found return 0.
        '''
        if name not in self.heroes:
            return 0
        else:
            self.heroes.remove(name)

    def view_all_heroes(self):
        '''
        Prints out all heroes to the console
        '''
        for hero in self.heroes:
            print(hero)
    
 
    def attack(self, other_team):
        ''' Battle each team against each other.'''
        # TODO: Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving heroes.
        # Hint: Use the fight method in the Hero class.
        pass

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        # TODO: This method should reset all heroes health to their
        # original starting value.
        pass

    def stats(self):
        '''Print team statistics'''
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.
        pass


if __name__ == "__main__":

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 3000)
    ability2 = Ability("Super Eyes", 1000)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)

    hero1.fight(hero2)
