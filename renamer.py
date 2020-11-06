import random
import os

base = "Jerma"
number = 0
INPUT_DIR = input("Input Directory: ")
adjectives = ["Innocent", "Corrupted", "Cowardly", "Evil", "Punished", "Charged", "Normal", "Weird",
              "Defender", "Psycho", "Banished", "Long", "Short", "Spinning", "Wealthy", "Poor",
              "Lonely", "Happy", "Broke", "Firey", "Spindly", "Lanky", "Pointy", "Late", "Early", "Enraged",
              "Powerful", "Weak", "Stupid", "Idiot", "Sensual", "Determined", "Washed Up", "Fucked Up", "Unhinged",
              "Destructive", "Creative", "Completely Normal", "Factory New", "Damaged", "Twitchy", "Icey", "Boomer",
              "Zoomer", "Enourmous", "Giant", "Chaotic", "Chaotic Neutral", "Neutral", "Lawful", "Lawful Neutral",
              "Chaotic Evil", "Lawful Good", "Lawful Evil", "Chaotic Good", "Disiplined Emotional", "Chaotic Neutral",
              "Old", "Bald", "Young", "Proto", "Ignorant", "Blissful", "Ooey Gooey", "Master of Comedy"]

nouns = ["Minecraft", "Light", "Darkness", "Dankness", "Life", "Justice", "Cheetos", "Monkeys", "Apes", "Goblins",
         "Gnomes", "Vegas", "Vegans", "Star_", "ster", "Spore", "The Capture Point", "Chat", "Garfield", "Chaos",
         "Peace", "Bones", "Cheezits", "Coffee", "Cheetos", "Chickens", "Minecraft Steve", "Arms", "Feet", "Hands",
         "Toes", "Ankles", "Billy Hatcher and The Giant Egg for The Nintendo Gamecube", "Jermas", "Money", "Bits",
         "CBT", "WEED", "CBD", "Mr. Green", "Bat Boy", "Glueman", "The Pencil", "Gamer Juice", "Gabe Newell", "The Spy",
         "Gamer Grease", "Byeahs", "Gamer Gunk", "Gamer Goop", "Grandpa", "Burgah Boy", "Sonic", "Pac Man",
         "Gamer Grime",
         "Obama", "Gamer Crust", "Benjamin Franklin", "The Monopoly Guy", "Mario", "Milkmen", "Gordon Freeman",
         "The Easter Bunny", "Santa Claus", "Ma3la", "Cap'n Crunch", "Frank Pizza", "Turtimos", "Dick Richard",
         "Zeraxos",
         "Mr. Sneak Man", "Rats", "Jay Buffet", "Carl Grinnensteed", "Fruit", "The Christmas Tree", "Beanbag Sonic",
         "Otto", "Etalyx", "Greg From Nvidia", "Jex", "GrillMasterXBBQ", "Odd Micheal", "BugleBerry", "Dean Dingus",
         "Anthony Banthony"]

titles = ["Bringer", "Fuckface", "Lost Soul", "Corrupter", "Gamer", "Fighter", "Goblin", "Gnome", "Bastard", "Gamer",
          "TFTuber", "Idiot", "Supreme Being", "Defender", "Psycho", "Killer", "Demon", "Horror", 'Terrorizer',
          "Hunter", "Cooker", "Griller", "Baker", "Obliterator", "Reaper", "Sower", "Evicerator", "Slicer", "Maniac",
          "Slurper", "Licker", "Kisser", "Sucker", "Consumer", "ConsOOMER", "Tyrant", "Lover", "Memer", "Player", "Ape",
          "Money", "Enjoyer", "Collector", "Excreter", "Rulemaker", "Milker"]

already_done = []  # List of names we already made

count = 0
for file in os.listdir(INPUT_DIR):
    original_name = False
    prefix = ""  # 1 - 4 adjectives
    suffix = ""  # Title + "of" + noun

    while not original_name:
        original_name = True
        cur_adjectives = []
        adj = adjectives[random.randint(0, len(adjectives)) - 1] + " "
        for j in range(random.randint(1, 3)):
            while adj in cur_adjectives:  # Prevent duplicate adjectives
                adj = adjectives[random.randint(0, len(adjectives)) - 1] + " "
            cur_adjectives.append(adj)
            prefix += adj
        suffix = titles[random.randint(0, len(titles)) - 1] + " of " + nouns[random.randint(0, len(nouns)) - 1]
        number = count
        numberless_name = prefix + base + " " + " The " + suffix
        if numberless_name in already_done:
            original_name = False
        else:
            already_done.append(numberless_name)
            full_name = prefix + base + str(number) + " The " + suffix
            os.rename(INPUT_DIR + "/" + file, INPUT_DIR + "/" + full_name + ".jpg")
    count += 1
