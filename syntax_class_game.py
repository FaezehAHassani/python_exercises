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

class Scene(object): # Scene is-a object
    def enter(self):
        pass

class Engine(object):
    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Death(Scene): # Death is-a Scene
   def enter(self):
       pass

class CentralCorridor(Scene):
   def enter(self):
       pass

class LaserWeaponArmory(Scene):
   def enter(self):
       pass

class TheBridge(Scene):
   def enter(self):
       pass

class EscapePod(Scene): 
   def enter(self):
       pass
