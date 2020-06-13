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

class Death(Scene): # Death is-a Scene
    quips = [
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
        print(dedent("""
                The Gothons of Planet Percal #25 have invaded your ship and destroyed entire crew. you are the last surviving member...
                """))

        action = input("Please choose shoot! or dodge! or tell a joke!> ")

        if action == "shoot!":
            print(dedent("""
                    Quick on the draw you yank out your blaster and fire
                    it at the Gothon. His clown costume is flowing and
                    moving around his body, which throws off your aim.
                    Your laser hits his costume but misses him entirely.
                    This completely ruins his brand new costume his mother
                    bought him, which makes him fly into an insane rage
                    and blast you repeatedly in the face until you are
                    dead. Then he eats you.
                    """))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
                    Like a world class
                    boxer you dodge, weave, slip and slide right
                    as the Gothon's blaster cranks a laser past your head...
                    """))
            return 'death'


        elif action == "tell a joke!":
            print(dedent("""
                    Lucky for you they made you learn
                    Gothon insults in the academy...
                    """))
            return 'laser_weapon_army'

        else:
            print("DOES NOT CMPUTE!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    def enter(self):
         print(dedent("""
                 You do a dive roll into the Weapon Armory,
                 crouch and scan the room for
                 more Gothons that might be hiding....
                 """))
         code = f"{randint(1, 9)}{randint(1,9)}{randint(1,9)}"  # randint(a, b) => Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
         guess = input("[keypad]> ")
         guesses = 0

         while guess != code and guesses < 10:
             print("BZZZZEDDDD!")
             guesses += 1
             guess = input("[keypad]> ")

         if guess == code:
             print(dedent("""
                   The container clickes open and the seal breaks,
                   letting gas out. You grab the nuetron bomb and run as fast as
                   you can to bridge where you must place it in thenright spot.
                   """))
             return 'the_bridge'

         else:
           print(dedent("""
                   The lock buzzes one last time and then
                   you hear a sickening melting sound as the mechanism is
                   fused together....
                   """))
           return 'death'

class TheBridge(Scene):
   def enter(self):
       print(dedent("""
               You burst onto the bridge with thr nuetron
               destruct bomb under your arm around
               surprise 5 Gothons who are trying
               to take control of the ship...
               """))
       action = input("Please choose throw the bomb or throw the bomb> ")

       if action == "throw the bomb":
           print(dedent("""
                   In a panic you throw the bomp at
                   the group of Gothons and
                   make a leap for the door....
                   """))
           return 'death'

       elif action == 'throw the bomb':
           print(dedent("""
                   You point your blaster at the bomb under
                   your arm and the Gothons put their hands up and
                   start to sweat....
                   """))
           return 'escape_pod'

       else:
           print("DOES NOT COMPUTE!")
           return 'the_bridge'

class EscapePod(Scene):
    def enter(self):
        print(dedent("""
                You rush through the ship desperately
                trying to make it to the escape pod before
                the whole ship explodes...
                """))
        good_pod = randint(1,5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
                   You jump into pod {guess} and hit
                   the eject button...
                   """))
            return 'death'

        else:
           print(dedent("""
                    You jump into pod {guess} and hits
                    the eject button....
                    """))
           return 'finished'

class Finished(Scene):
    def enter(self):
        print("You won! Good job.")
        return 'finished'

class Map(object):
    scenes = {
       'central_corridor': CentralCorridor(),
       'laser_weapon_army': LaserWeaponArmory(),
       'the_bridge': TheBridge(),
       'escape_pod': EscapePod(),
       'death': Death(),
       'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

# a little test
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
