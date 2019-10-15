from random import randint
import superheroes
import ability_and_armor

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
            team1_hero = self.heroes[randint(0, len(self.heroes)-1)]
            team2_hero = other_team.heroes[randint(
                0, len(other_team.heroes)-1)]
            #   select random heroes from each team
            #   and make them fight
            #
            # remove the dead hero from the team
            if not team1_hero.is_alive():
                self.heroes.remove(team1_hero.name)
            elif not team2_hero.is_alive():
                other_team.heroes.remove(team2_hero.name)

            print(
                f"team 1 hero: {team1_hero.name}, team 2 hero: {team2_hero.name}")

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
