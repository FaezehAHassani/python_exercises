# how to write a test

# first make a tree like below
#* Map
#    - next_scene
#    - opening_scene
#* Engine
#    - play
#* Scene
#   - enter
#   * Death
#   * Central Corridor
#   * Laser Weapon Armory
#   * The Bridge
#   * Escape Pod

# then add a litte test as the end

from sys import exit
from random import randint
from textwrap import dedent  # this is for using """

class Scene(object): # Scene is-a object
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter()")
        exit(1) # exit(1) means there was some issue / error / problem and that is why the program is exiting.

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

            # print the last scene
            current_scene.enter()

class Death(Scene):   # Death is-a Scene
    quips =[
       "You died. you kinda suck at this.",
       "Your Mom would be proud...if she were smarter.",
       "Such a luser.",
       "I have a small puppy that's better at this.",
       "You're worese than your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):
   def enter(self):
       pass

class LaserWeaponArmory(Scene):
   def enter(self):
       print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and destroyed entire crew. you are the last surviving member...
            """))
    action = input("> ")

    if action == "shoot!":
        print(dedent("""
        Quick on the draw you yank out your blaster and fire it at the Gothon...
        """))

class TheBridge(Scene):
   def enter(self):
       pass

class EscapePod(Scene):
   def enter(self):
       pass

class Map(object):
    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

# a little test
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
