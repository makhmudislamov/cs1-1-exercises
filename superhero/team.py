from random import randint
from superheroes import *


class Team(object):

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
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                print(f'removed hero is {name}')
        return 0

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

        # while self.heroes or other_team.heroes:
        # print("inside while")
        # select random heroes from each team
        team1_hero = self.heroes[0]
        team2_hero = other_team.heroes[0]
        print(f"hero 1: {team1_hero.name}")
        
        # TODO: calling fight() from class Hero - Needs bugfix
        winner = team1_hero.fight(team2_hero)
        if winner == team1_hero.name:
            other_team.remove_hero(team2_hero.name)
        else:
            self.remove_hero(team1_hero.name)
        # print(f"Winner is {winner}")
        # print(f"team1 {self.heroes}")
        # print(f"team2 {other_team.heroes}")
            # print(f"team 1 hero: {team1_hero.name}, team 2 hero: {team2_hero.name}")


    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        # TODO: This method should reset all heroes health to their
        # original starting value.
        for hero in self.heroes:
            hero.current_health = health
        

    def stats(self):
        '''Print team statistics'''
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.
        pass


# if __name__ == "__main__":
#     pass
