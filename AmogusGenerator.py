import statistics
from os import remove
import random

class Amogus:
    def __init__(self, type, color, room, username, sus = False):
        self.type = type
        self.color = color
        self.location = room.cords
        self.sus = sus
        self.username = username
    def isitsus(self):
        if self.sus:
            return "hella sus"
        else:
            return "not sus"

class Room:
    def __init__(self, cords, name):
        self.cords = cords
        self.name = name
        self.crewmatesInside = 0
        self.deadBodies= 0
# Possible colors and locations
types = ["impostor", "crewmate", "dead"]
colors = ["cyan", "blue", "red", "green", "purple", "pink", "yellow",  "brown", "black", "white"]
locationNames = ["cafeteria", "admin", "navigation", "communication", "electrical", "engines", "medbay", "laser", "oxygen", "reactor"]
locations = [Room((0,0),locationNames[0]), Room((0,1),locationNames[1]), Room((0,2),locationNames[2]), Room((0,3),locationNames[3]), Room((0,4),locationNames[4]), Room((1,0),locationNames[5]), Room((1,1),locationNames[6]), Room((1,2),locationNames[7]), Room((1,3),locationNames[8]), Room((1,4),locationNames[9])]
words = ["funny", "cool", "crazy", "awesome", "random", "silly", "wacky", "zany", "amazing", "incredible"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

# Create 10 random Amogus objects
Amogus_list = []
# Generate 4 lists of 10 random numbers
lists = [[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]]
for i in range(4):
    numbers = [0,1,2,3,4,5,6,7,8,9]
    for a in range(10):
        r = random.randint(0,len(numbers)-1)
        lists[i][a] = numbers[r]
        numbers.remove(numbers[r])
for i in range(10):
        Amogus_list.append(Amogus(types[1], colors[lists[0][i]], locations[lists[1][i]], words[lists[2][i]] + str(random.randint(0,100)) + symbols[lists[3][i]]))
#make em sus

numbers = [0,1,2,3,4,5,6,7,8,9]
r1 = random.randint(0,len(numbers)-1)
numbers.remove(numbers[r1])
r2 = random.randint(0,len(numbers)-1)

Amogus_list[r1].type = types[0]
Amogus_list[r2].type = types[0]

for baka in Amogus_list:
    print(f"{baka.color}player: {baka.username} is in {baka.location} and he is {baka.isitsus()}!!!")

def updateMap():
    for location in locations:
        for amongus in Amogus_list:
            if amongus.location == location.cords:
                location.crewmatesInside += 1
def MoveAmogus():
    for i in range(len(Amogus_list)):
        r = random.randint(0,9)
        Amogus_list[i].location = locations[r].cords
        print(f"{Amogus_list[i].username} is in {locations[r].name}")

# if there is an impostor in the same room as a crewmate, the impostor will kill the crewmate
# if there is more than one crewmate in the same room, impostor cannot kill

def KillAmogus():
    for i in range(len(Amogus_list)):
        if Amogus_list[i].type == types[0]:
            for a in range(len(Amogus_list)):
                for location in locations:
                    if Amogus_list[a].location == location.cords:
                        if location.crewmatesInside > 1:
                            print(f"{Amogus_list[i].username} cannot kill because there are {location.crewmatesInside} crewmates in {location.name}")
                        elif location.crewmatesInside == 1:
                            print(f"{Amogus_list[i].username} killed {Amogus_list[a].username} in {location.name}")
                            Amogus_list[a].type = types[2]
                            location.crewmatesInside -= 1
                            location.deadBodies += 1
                            #imposter becomes sus
                            Amogus_list[i].sus = True

#if a crewmate enters a room with a dead body, they will report it
def ReportBody():
    for i in range(len(Amogus_list)):
        if Amogus_list[i].type == types[1]:
            for location in locations:
                if Amogus_list[i].location == location.cords:
                    if location.deadBodies == 1:
                        print(f"{Amogus_list[i].username} reported a dead body in {location.name}")
                        location.deadBodies -= 1
                        #imposter becomes sus
                        Amogus_list[i].sus = True

#crewmates can vote to eject a player, a sus player has a higher chance of getting votes
def Vote():
    votables = []
    choices = []
    for amogus in Amogus_list:
        if amogus.sus == True:
            votables.append(amogus)
            votables.append(amogus)
        votables.append(amogus)
    for amogus in Amogus_list:
        choices.append(random.randint(0,len(votables)-1))
        print(f"{amogus.username} voted for {votables[choices[Amogus_list.index(amogus)]].username}")
        #player with most votes gets ejected
    for amogus in Amogus_list:
        if  statistics.mode(choices) == choices[Amogus_list.index(amogus)]:
            print(f"{amogus.username} was ejected")
            Amogus_list.remove(amogus)

#the game loops until less than 3 players are left
def GameLoop():
    while len(Amogus_list) > 3:
        updateMap()
        MoveAmogus()
        KillAmogus()
        ReportBody()
        Vote()
        print("next turn")
    print("game over")
    if Amogus_list.count(types[0]) == 0:
        print("crewmates win")
    elif Amogus_list.count(types[1]) == 0:
        print("impostors win")
    else:
        print("draw")

#run the game
GameLoop()