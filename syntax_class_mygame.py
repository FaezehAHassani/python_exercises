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

class Hall(object):
    def enter(self):
        print("Welcome to my Gold Coins game.")
        print("A fantastic entrance hall, isn't it?")
        action = input("There is two doors, which door you choose DoorA or DoorB? > ")

        if action == "DoorA":
            print("Here you face the evil, what do you do?")
            fight = print("Please choose, I fight Barehand or InfiniteCry >")

            if fight == "Barehand":
                print("You hit the evil back and force until it dies!")
                return 'gold_coins'

            elif fight == "InfiniteCry":
                print("You cry infinitely and the evil sinks in your tears.")
                return 'gold_coins'

        elif action == "DoorB":
            print("You should select your weapon, do you choose Sword or Gun")

            if fight == "Sword":
                print("You are well equipeed now, you have a strong sword!")
                return 'evil_room'

            elif fight == "Gun":
                print("You are smart, you have a nice gun now!")
                return 'evil_room'

class GoldCoins(Scene):
    print("You did a good job, this bag of 100 gold coins bbelongs to you!")

class EvilRoom(Scene):
    print("Here you face the evil, what do you do?")
    fightsmart = print("Please choose, I fight with Sword or Gun >")

    if fightsmart == "Sword":
        print("You kill the evil with your strong sword!")
        return 'evil_room'

    elif fightsmart == "Gun":
        print("You shot the evil, well done!")
        return 'evil_room'

class Map(object):
    scenes = {
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
a_map = Map('evil_room')
a_game = Hall(a_map)
a_game.play()
