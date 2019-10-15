from random import randint


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

    def ability_attack(self):
        '''
        Use randint(a, b) to select a random attack value.
        Return an attack value between 0 and the full attack.
        '''
        attack_value = randint(0, self.max_damage)
        print(f"attack value in ability: {attack_value}")
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
        block_value = randint(0, self.max_block)
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

class Weapon(Ability):
    def ability_attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        return randint(self.max_damage // 2, self.max_damage)
 

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
            print(hero.name)
    
 
    def team_attack(self, other_team):
        ''' Battle each team against each other.'''
        # TODO: Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving heroes.
        # Hint: Use the fight method in the Hero class.
        
        if not self.heroes and not other_team.heroes:
            print("No alive heroes left on both teams")
        # else:

        while self.heroes or other_team.heroes:
            print("inside while")
            team1_hero = self.heroes[randint(0,len(self.heroes)-1)]
            team2_hero = other_team.heroes[randint(0, len(other_team.heroes)-1)]
            #   select random heroes from each team
            #   and make them fight
            # 
            # remove the dead hero from the team
            if not team1_hero.is_alive():
                self.heroes.remove(team1_hero.name)
            elif not team2_hero.is_alive():
                other_team.heroes.remove(team2_hero.name)
                

            print(f"team 1 hero: {team1_hero.name}, team 2 hero: {team2_hero.name}")
            
            # team1_hero.fight(team2_hero)
            team1_hero.fight(team2_hero)

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
