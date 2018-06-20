import MyResources
import random
import MyEvents

class Ship:

    def __init__(self):
        self.Gold = 0
        self.ShipHpBeg = 0
        self.ShipHp = 0
        self.CrewHpBeg = 0
        self.CrewHp = 0
        self.Fame = 0
        self.Infamy = 0
        self.Happiness = 0
        self.Wealth = 0
        self.Crew = []
        self.Resources = MyResources.Resources()
        self.EventTyp = "N"
        self.mess = "N"

    def dodailyevent(self, a_mench):
        evech = 0
        evech = random.randint(1, 4)
        if self.EventTyp == "N" and evech == 1:
            typofsh = random.randint(1,3)
            if typofsh == 1:
                self.EventTyp = "shcomcar"
            if typofsh == 2:
                self.EventTyp = "shcompir"
        if self.EventTyp == "shcomcar":
            self.shcomcargo()
        if self.EventTyp == "attcargo":
            self.attshcargo(a_mench)

    def shcomcargo(self, a_ch):
        self.mess = "Look! It seems like a ship is approaching"
        self.mess += "It's a cargo ship! What should we do Captain?"
        if a_ch == "ATTCARGO":
            self.EventTyp ="attcargo"
            self.attshcargo()
        if a_ch == "IGNCARGO":
            self.EventTyp ="igncargo"
            self.attshcargo()

    def shcompir(self):
        self.mess = "Oh it's a pirate ship!"
        self.mess += "Other pirates on the sea are pretty tricky, how would you like to handle the encounter"
        if a_ch == "ATTPIR":
            self.EventTyp ="attpir"
            self.attshpir()
    def attshcargo(self, a_ch):
        redunum = random.randint(0, 2)
        self.CrewHp -= redunum
        self.mess = "The life of the Pirate is crowned by the menace generated on the innocents of the sea."
        self.mess += "You attacked the cargo ship!"
        self.mess += "Now that the ship is disabled what would you like to do?"
        if a_ch == "OB":
            self.shipeventob()
        if a_ch == "LT":
            self.shipeventltnonnavy()

    def attshpir(self):
        redunum = random.randint(0, 5)
    def shipeventob(self):
        messap1 = "No Mercy! You destroyed all in site, sparing no one and nothing."
        messap2 = "The breeze of the sea blows with the deafening silence after the cries of your victims!"
        messap3 = "Your name will ring around the globe for your destructive force"
        self.Fame += 50
        self.Infamy += 60

    def shipeventltnonnavy(self):
        mess = "You ravaged the goods of your enemy taking them for spoil"
        num = random.randint(1, 100)
        self.Wealth += num
        self.Fame += .80 * num
        self.Resources.Ammunition += .25 * num
        self.Resources.Medicine += .25 * num

    def shipeventltnavy(self):
        mess = "A pirate defeating the navy! Quite an unusual feat, and a juicy loot at that"
        num = random.randint(1, 100)
        self.Wealth += 2.5 * num
        self.Fame += 1.75 * num
        self.Resources.Ammunition += 1.25 * num
        self.Resources.Ammunition += .50 * num
        self.Resources.Medicine += .25 * num

    def shipeventafterlt(self, a_ch):
        mess += "The enemy is at your mercy, what would you have done to them?"
        if a_ch == "MRCY":
            mess = "You took their goods but spared their lives, some call it marcy others maybe not"
        if a_ch == "OB":
            self.shipeventob()
    def ignshcargo(self):
        self.mess = "You have ignored a ship perhaps tomorrow might be a better time for a good loot"

    def addcrewmem(self, a_mem):
        self.Crew.append(a_mem)

