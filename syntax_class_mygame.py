# my first made up game

# Looking for Gold Coins
#* Hall
#   - enter
#   * Evil room
#      Infinite cry
#      Fight barehand
#   * Gun room
#      Sword
#      Gun
#   * Gold coins

from sys import exit

class Scene(object):
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter()")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('gold_coins')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Hall(Scene):
    def enter(self):
        print("Welcome to my Gold Coins game.")
        print("A fantastic entrance hall, isn't it?")
        action = input("There is two doors, which door you choose DoorA or DoorB? > ")

        if action == "DoorA":
            print("Here you face the evil, what do you do?")
            fight = input("Please choose, I fight Barehand or Infinitecry >")

            if fight == "Barehand":
                print("You hit the evil back and force until it dies!")
                return 'gold_coins'

            elif fight == "Infinitecry":
                print("You cry infinitely and the evil sinks in your tears.")
                return 'gold_coins'

        elif action == "DoorB":
            equipment = input("You should select your weapon, do you choose Sword or Gun? >")

            if equipment == "Sword":
                print("You are well equipped now, you have a strong sword!")
                return 'evil_room'

            elif equipment == "Gun":
                print("You are smart, you have a nice gun now!")
                return 'evil_room'

class GoldCoins(Scene):
    def enter(self):
        print("You did a good job, this bag of 100 gold coins belongs to you!")

class EvilRoom(Scene):
    def enter(self):
        equipment = input("Oh I forgot, tell me again, you chose Sword or Gun? >")
        print(f"So, you use your {equipment} to figth the evil.")

        if equipment == "Sword":
            print("You kill the evil with your strong sword!")
            return 'gold_coins'

        elif equipment == "Gun":
            print("You shot the evil, well done!")
            return 'gold_coins'

class Map(object):
    scenes = {
       'hall': Hall(),
       'gold_coins': GoldCoins(),
       'evil_room': EvilRoom()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

# a little test
a_map = Map('hall')
a_game = Engine(a_map)
a_game.play()
