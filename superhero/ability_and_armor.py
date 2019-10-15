from random import randint
from team import Team

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
        self.max_damage -= attack_value
        return attack_value


class Weapon(Ability):
    def ability_attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        return randint(self.max_damage // 2, self.max_damage)


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
        self.max_block -= block_value
        return block_value


if __name__ == "__main__":
    pass
