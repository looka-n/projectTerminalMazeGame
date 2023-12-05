# 2D Maze Game
A Python programming assignment done at CSULB
## Description
The user plays a game on the terminal to traverse a maze of rooms, with its contents being unknown. Each room may contain lurking danger, useful items, or maybe nothing at all. The goal is to get to the finish, whose location is also unknown.
## How to play
Use number inputs to take action based on the player's available choices presented through the terminal. For every turn, each action results in a consequential event within the game.
### Name your character
The player is given the ability to enter a name of their own choosing for their character. This will persist throughout the run.
### Choose your difficulty
The player is also given the choice to face monsters of "beginner" and "expert" difficulty. Depending on which you choose, the monsters will possess varying amounts of health and damage.
### Enter the maze
Once the game starts, the player is placed at the start of the maze, unaware of what lies in their surrounding area. In order to complete the game, the player must explore rooms to find the finish, discovering what lies within along the way.
* Potions: Upon entering a room with a potion in it, the player takes it, refilling their health back to its maximum value.
* Monsters: There also lies the possibility of encountering goblins, ogres, and trolls. You may either choose to face off against them, or run away to an adjacent room. Successfully fighting the monster kills it, allowing the player to enter the room freely. Running away, however, leaves the monster alive and keeps it a remaining threat if the player decides to come back.
### Find the finish
Navigate the rooms to find the location of the finish. Upon doing so, the player enters yet another level, repeating the previous steps. The finish is in a new location and there are three levels in total.
