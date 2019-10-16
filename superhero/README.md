# Superhero Dueller
![Project Poster](poster.jpeg)

## Description

Superhero Dueller is a mini simulator where users can duel their favorite superheroes to find out who is the most powerful of them. 


### How to use 'Superhero Dueller'

1. Download this repo
2. Go to main.py to build your superheroes
3. Add armors and abilites with their power units using the relative functions.

   Example:
   laser_sword = Ability("Laser Sword", 200)
   hero_name.add_ability(laser_sword) 
4. call fight method to find out who is the winner.

## Features
* [X] Users can create heroes 
`see Hero class`
* [X] Users can create superpowers and supershields 
`see class Ability and class Armor`
* [X] Users can duel the superheroes 
`see class Hero, def fight() `
* [X] Users can see which superheroes killed and died most
`see def add_kill() and def add_deaths()`

**Coming Soon**
* [ ] Build teams of supeheroes
`see class Team`
* [ ] Make the supeheroes fight in arena
`see class Arena

