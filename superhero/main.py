from superheroes import *
from team import *

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
    # team1.view_all_heroes()
    # team2.view_all_heroes()

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
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    winner = hero1.fight(hero2)
    print(f"Winner is {winner}")
