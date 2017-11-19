#python githubbable 11:35 11/19/2017
print ("Hi")
print ("YO")
swords={
        "Rapier":
        {"Attack":87, "Description":"A Rapie sword"},
        "Katana":
        {"Attack":122,"Description":"Ana's Kat"},
        }
monsters={
        "Slime":
        {"HP":200,"Attack":40,"Gold":10},
        "Bat":
        {"HP":250,"Attack":40,"Gold":15}
        }

class Player(object):
    def __init__(self, hp, strength, weapon, gold):
        self.hp=hp
        self.strength=strength
        self.weapon=weapon
        self.gold=gold

    def giveGold(self, coins):
        self.gold+=coins

def summon (monster,bob):
    print ("A %s appears!"%(monster))
    slimeA=monsters[monster]["HP"]
    while slimeA>0:
        input("Attack?")
        print ("You attack the %s for "%(monster) + str(power) + " damage!")
        slimeA=slimeA-power
        if (slimeA<=0):
            print ("%s defeated!\n"%(monster) + "You gained " + str(monsters[monster]["Gold"]) + " gold.")
            bob.giveGold(monsters[monster]["Gold"])
            break
        print ("Slime health now at " + str(slimeA))
        bob.hp=bob.hp-monsters["Slime"]["Attack"]
        print ("Your health: " +str(bob.hp))
    
bob=Player(100,10, "Rapier",0)

print (swords)
print (monsters)

for key in swords:
    print (key + "\n"+"Attack:"+str(swords[key]["Attack"])+"\n"+swords[key]["Description"])

option=""
print ("test")

power=swords[bob.weapon]["Attack"]+bob.strength
while (option !="q"):
    option=input("Do something:")
    if option=="summon":
        print ("A slime appears!")
        slimeA=monsters["Slime"]["HP"]
        while slimeA>0:
            input("Attack?")
            print ("You attack the slime for " + str(power) + " damage!")
            slimeA=slimeA-power
            if (slimeA<=0):
                print ("Slime defeated!\n" + "You gained " + str(monsters["Slime"]["Gold"]) + " gold.")
                bob.giveGold(monsters["Slime"]["Gold"])
                break
            print ("Slime health now at " + str(slimeA))
            bob.hp=bob.hp-monsters["Slime"]["Attack"]
            print ("Your health: " +str(bob.hp))
    if option=="i":
        print ("You have: \n " +str(bob.gold) + " gold")
    if option=="sb":
        summon("Bat",bob)
