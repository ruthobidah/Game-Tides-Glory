import random
import MyMenuList
import pygame
import math
pygame.font.init()
defF = pygame.font.get_default_font()
StrObj = pygame.font.Font(defF, 20)


class Events:

    def __init__(self):
        self.EventTyp = "N"
        self.EventTypChS = False
        self.mess = "N"
        self.xpos = 610
        self.MenuOp = MyMenuList.MenuList()
        self.pladam = 0

    def genrevent(self, a_screen, a_ship=None):
        evech = random.randint(1, 5)
        if evech == 1:
            self.mess = "Look! It seems like a ship is approaching"
            typofsh = random.randint(1, 3)
            if typofsh == 1:
                self.shcomcargo(a_screen, a_ship)
            if typofsh == 2:
                self.shcompir(a_screen, a_ship)
            if typofsh == 3:
                self.shcomnav(a_screen, a_ship)
        if evech == 2:
            self.sharkevent(a_screen, a_ship)
        if evech == 3:
            self.plagueevent(a_screen, a_ship)
        if evech == 4:
            self.clearDay(a_screen)
        if evech == 5:
            self.barrelevent(a_screen)

    def clearDay(self, a_screen):
        self.mess = "A peaceful day at sea."
        messobj = StrObj.render(self.mess, 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 5))

    # event cargo ship Done
    def shcomcargo(self, a_screen, a_ship):
        self.mess += "It's a cargo ship! What should we do Captain?"
        tradshImg = pygame.image.load("trade.png")
        tradshImg = pygame.transform.scale(tradshImg, (int(tradshImg.get_width() * .15), int(tradshImg.get_height() * .15)))
        a_screen.blit(tradshImg, (490, 20))
        messobj = StrObj.render(self.mess[0:30], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 5))
        messobj = StrObj.render(self.mess[30:41], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 25))
        messobj = StrObj.render(self.mess[41:75], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 50))
        messobj = StrObj.render(self.mess[75:], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 70))
        self.MenuOp.initshipcargoop(a_ship)
        self.MenuOp.drawmen(a_screen, 0)

    # event pirate ship Done
    def shcompir(self, a_screen, a_ship):
        self.mess += "Oh it's a pirate ship!"
        self.mess += "Other pirates on the sea are pretty tricky, how would you like to handle the encounter?"
        pirshImg = pygame.image.load("Pirate.png")
        pirshImg = pygame.transform.scale(pirshImg, (int(pirshImg.get_width() * .15), int(pirshImg.get_height() * .15)))
        a_screen.blit(pirshImg, (490, 20))
        messobj = StrObj.render(self.mess[0:30], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 5))
        messobj = StrObj.render(self.mess[30:41], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 25))
        messobj = StrObj.render(self.mess[41:63], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 50))
        messobj = StrObj.render(self.mess[63:98], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 70))
        messobj = StrObj.render(self.mess[99:136], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 90))
        messobj = StrObj.render(self.mess[136:], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 110))
        self.MenuOp.initshippirop(a_ship)
        self.MenuOp.drawmen(a_screen, 0)

    # event navy ship Done
    def shcomnav(self, a_screen, a_ship):
        self.mess = "Look! It seems like a ship is approaching"
        messobj = StrObj.render(self.mess[0:30], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 5))
        messobj = StrObj.render(self.mess[30:41], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 25))
        self.mess = "Oh no! A pirate's nightmare, the navy is upon us. How would you want to handle this Captain?"
        NavImg = pygame.image.load("Navy.png")
        NavImg = pygame.transform.scale(NavImg, (int(NavImg.get_width() * .15), int(NavImg.get_height() * .15)))
        a_screen.blit(NavImg, (490, 20))
        messobj = StrObj.render(self.mess[0:37], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 45))
        messobj = StrObj.render(self.mess[38:71], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 65))
        messobj = StrObj.render(self.mess[72:], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 85))
        self.MenuOp.initshipnavop(70, a_ship)
        self.MenuOp.drawmen(a_screen, 0)

    # ship event attack cargo ship Done
    def shipeventattcargo(self, a_ship, a_screen):
        self.mess = "The life of the Pirate is crowned by the menace generated on the innocents of the sea."
        self.mess += "You attacked the cargo ship!"
        self.mess += "Now that the ship is disabled what would you like to do?"
        messobj = StrObj.render(self.mess[0:36], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 5))
        messobj = StrObj.render(self.mess[37:64], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 25))
        messobj = StrObj.render(self.mess[65:86], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 45))
        messobj = StrObj.render(self.mess[86: 114], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 70))
        messobj = StrObj.render(self.mess[114: 148], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 95))
        messobj = StrObj.render(self.mess[149: 170], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 115))
        redunum = random.randint(0, 5)
        a_ship.CrewHp -= redunum
        a_ship.Resources.Ammunition -= 2
        self.MenuOp.initafterattnonnav(150)
        self.MenuOp.drawmen(a_screen, 0)

    # ship event ignore cargo ship Done
    def shipeventigncargo(self, a_ship, a_screen):
        self.mess = "You have ignored a ship perhaps tomorrow might be a better time for a good loot"
        messobj = StrObj.render(self.mess[0:31], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 5))
        messobj = StrObj.render(self.mess[32:63], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 25))
        messobj = StrObj.render(self.mess[64:80], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 45))

    # ship event attack pirate ship Done
    def shipeventattpir(self, a_ship, a_screen):
        ranloss = random.randint(0, 5)
        a_ship.ShipHp -= ranloss
        a_ship.CrewHp -= int(math.ceil(.75 * ranloss))
        self.mess = "You attacked the other pirate, Violence is the language of the sea."
        self.mess += "Unfortunately, there is often a price to pay to speak it"
        self.mess += "You've overpowered the other pirate, showing your dominance, what would you do "
        self.mess += "with whats left of his crew?"
        messobj = StrObj.render(self.mess[0:39], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 5))
        messobj = StrObj.render(self.mess[40:67], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 25))
        messobj = StrObj.render(self.mess[67:104], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 45))
        messobj = StrObj.render(self.mess[105:123], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 65))
        messobj = StrObj.render(self.mess[123:151], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 85))
        messobj = StrObj.render(self.mess[152:183], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 105))
        messobj = StrObj.render(self.mess[184:212], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 125))
        messobj = StrObj.render(self.mess[213:235], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 145))
        redunum = random.randint(0, 5)
        a_ship.CrewHp -= redunum
        a_ship.Resources.Ammunition -= 2
        self.MenuOp.initafterattnonnav(200)
        self.MenuOp.drawmen(a_screen, 0)

    # ship event ignore pirate ship Done
    def shipeventignpir(self, a_ship, a_screen):
        randnum = random.randint(1, 2)
        if randnum == 1:
            self.mess = "Whew! You expertly avoided an interaction with another pirate at sea"
            messobj = StrObj.render(self.mess[0:30], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 5))
            messobj = StrObj.render(self.mess[30:64], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 25))
            messobj = StrObj.render(self.mess[65:], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 45))
            self.EventTyp = "0"
        if randnum == 2:
            self.mess = "You tried to avoid another pirate at sea but you weren't quick enough and got sighted."
            self.mess += "You know the law of the seas, the other pirate attacked you"
            self.mess += "The pirates attacked your ship, what would you like to do?"
            messobj = StrObj.render(self.mess[0:40], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 5))
            messobj = StrObj.render(self.mess[41:74], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 25))
            messobj = StrObj.render(self.mess[74:110], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 45))
            messobj = StrObj.render(self.mess[110:145], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 65))
            messobj = StrObj.render(self.mess[145:181], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 85))
            messobj = StrObj.render(self.mess[182:], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 105))
            a_ship.ShipHp -= 1
            a_ship.CrewHp -= 1
            self.MenuOp.initafterignpir(160)
            self.MenuOp.drawmen(a_screen, 0)
            self.EventTyp = "1"

    # ship event bribe pirate ship Done
    def shipeventbribpir(self, a_ship, a_screen):
        randnum = random.randint(1, 2)
        self.mess = "It's not in you to engage in battle now, sometimes violence is not the best choice"
        messobj = StrObj.render(self.mess[0:40], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 5))
        messobj = StrObj.render(self.mess[41:75], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 25))
        messobj = StrObj.render(self.mess[76:110], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 45))
        a_ship.Resources.Beer -= 2
        if randnum == 1:
            self.mess = "You tried to bribe the Captain of the pirate  ship, but the captain proves more"
            self.mess += " cunning than you expected. At least you avoided a bloody battle."
            messobj = StrObj.render(self.mess[0:37], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 65))
            messobj = StrObj.render(self.mess[38:74], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 85))
            messobj = StrObj.render(self.mess[75:109], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 105))
            messobj = StrObj.render(self.mess[110:], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 125))
        else:
            self.mess = "You successfully bribed the Ship Captain. "
            self.mess += "Sometimes a good trade is as good as a bloody conquest."
            messobj = StrObj.render(self.mess[0:33], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 65))
            messobj = StrObj.render(self.mess[33:67], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 85))
            messobj = StrObj.render(self.mess[68:], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 105))
            a_ship.Wealth += 1

    # ship event flee pirate ship Done
    def shipeventfleepir(self, a_ship, a_screen):
        self.mess = "Today is not the day for battle, retreat!"
        messobj = StrObj.render(self.mess[0:41], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 5))
        randnum = random.randint(0, 5)
        a_ship.ShipHp -= randnum
        a_ship.CrewHp -= int(math.ceil(randnum * .75))
        a_ship.Happiness -= randnum * .70

    # ship event flee navy ship Done
    def shipeventfleenav(self, a_ship, a_screen):
        self.mess = "Today is not the day for battle, retreat!"
        messobj = StrObj.render(self.mess[0:41], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 5))
        randnum = random.randint(3, 10)
        a_ship.ShipHp -= randnum
        a_ship.CrewHp -= int(math.ceil(randnum * .75))
        a_ship.Happiness -= randnum * .70

    # ship event attack navy ship Done
    def shipeventattnav(self, a_ship, a_screen):
        self.mess = "Like a cornered hunter, you pounce back! It's better to go down with the blood of thy "
        self.mess += "enemies than of only thine own. "
        self.mess += "You defeated the navy, a most prized feat, what would you have done with what's left of them."
        messobj = StrObj.render(self.mess[0:35], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 5))
        messobj = StrObj.render(self.mess[35:72], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 25))
        messobj = StrObj.render(self.mess[73:106], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 45))
        messobj = StrObj.render(self.mess[107:140], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 65))
        messobj = StrObj.render(self.mess[141:171], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 85))
        messobj = StrObj.render(self.mess[172:202], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 105))
        messobj = StrObj.render(self.mess[203:], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 125))
        randnum = random.randint(0, 6)
        a_ship.ShipHp -= randnum
        a_ship.CrewHp -= int(math.ceil(.75 * randnum))
        a_ship.Resources.Ammunition -= 2
        self.MenuOp.initafterattnav(200)
        self.MenuOp.drawmen(a_screen, 0)

    # ship event ignore navy ship Done
    def shipeventignnav(self, a_ship, a_screen):
        randnum = random.randint(1, 10)
        if randnum < 10:
            self.mess = "It is a near impossible thing for a pirate to escape being caught by the navy. "
            self.mess += "The navy ship sighted you as you tried to escape and opened fire at your ship."
            messobj = StrObj.render(self.mess[0:35], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 5))
            messobj = StrObj.render(self.mess[36:68], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 25))
            messobj = StrObj.render(self.mess[69:104], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 45))
            messobj = StrObj.render(self.mess[105:138], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 65))
            messobj = StrObj.render(self.mess[139:], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 85))
            randnum = random.randint(0, 10)
            a_ship.ShipHp -= randnum
            if randnum > 1:
                a_ship.CrewHp -= randnum - 2
            self.MenuOp.initafterignnav(200)
            self.MenuOp.drawmen(a_screen, 0)
            self.EventTyp = "1"
        else:
            self.mess = "You did the impossible! You escaped the navy without being caught. Be Merry"
            messobj = StrObj.render(self.mess[0:36], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 5))
            messobj = StrObj.render(self.mess[36:66], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 25))
            messobj = StrObj.render(self.mess[67:], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 45))
            a_ship.Happiness += 10
            self.EventTyp = "0"

    # ship event bribe navy ship Done
    def shipeventbribnav(self, a_ship, a_screen):
        randnum = random.randint(1, 20)
        if randnum < 20:
            self.mess = "You dare dream to bribe the navy? That's unheard of. The commander ordered an attack on "
            self.mess += "your ship, what would you like to do?"
            messobj = StrObj.render(self.mess[0:33], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 5))
            messobj = StrObj.render(self.mess[34:66], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 25))
            messobj = StrObj.render(self.mess[67:92], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 45))
            messobj = StrObj.render(self.mess[93:], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 65))
            a_ship.ShipHp -= 1
            a_ship.Resources.Beer -= 3
            self.EventTyp = "1"
            self.MenuOp.initafterignnav(200)
            self.MenuOp.drawmen(a_screen, 0)
            self.EventTyp = "1"
        else:
            self.mess = "Wow You did the impossible! You successfully bribed the Commander. The news "
            self.mess += "of the swiftness of your tongue and the sweetness of your beer shall travel ashore"
            messobj = StrObj.render(self.mess[0:32], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 5))
            messobj = StrObj.render(self.mess[32:66], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 25))
            messobj = StrObj.render(self.mess[67:100], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 45))
            messobj = StrObj.render(self.mess[101:138], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 65))
            messobj = StrObj.render(self.mess[139:], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 85))
            a_ship.Wealth += 1
            a_ship.Fame += 1
            a_ship.Resources.Beer -= 2
            a_ship.Resources.Ammunition += 1
            a_ship.Resources.Medicine += 1
            self.EventTyp = "0"

    def shipeventafterattopnav(self, a_ch):
        if self.MenuOp.m_curMenC == "OB":
            self.MenuOp.m_curMenC = "N"
            self.shipeventob()
        if self.MenuOp.m_curMenC == "LT":
            self.MenuOp.m_curMenC = "N"
            self.shipeventltnavy()

    def shipeventafterltop(self, a_ch):
        if self.MenuOp.m_curMenC == "MRCY":
            mess = "You took their goods but spared their lives, some call it marcy others maybe not"
            self.MenuOp.m_curMenC = "N"
        if self.MenuOp.m_curMenC == "OB":
            self.MenuOp.m_curMenC = "N"
            self.shipeventob()

    # ship event destroy the ship Done
    def shipeventob(self,a_ship, a_screen):
        self.mess = "No Mercy! You destroyed all in site, sparing no one and nothing."
        self.mess += "The breeze of the sea blows with the deafening silence after the cries of your victims!"
        self.mess += "Your name will ring around the globe for your destructive force"
        messobj = StrObj.render(self.mess[0:36], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 5))
        messobj = StrObj.render(self.mess[37:64], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 25))
        messobj = StrObj.render(self.mess[64:100], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 45))
        messobj = StrObj.render(self.mess[101:137], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 65))
        messobj = StrObj.render(self.mess[138:151], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 85))
        messobj = StrObj.render(self.mess[151:181], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 105))
        messobj = StrObj.render(self.mess[182:], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 125))
        a_ship.Fame += 50
        a_ship.Infamy += 60

    # ship event loot from cargo or pirate ship Done
    def shipeventltnonnavy(self, a_ship, a_screen):
        self.mess = "You ravaged the goods of your enemy taking them for spoil."
        messobj = StrObj.render(self.mess[0:36], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 5))
        messobj = StrObj.render(self.mess[36:], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 25))
        num = random.randint(1, 50)
        a_ship.Wealth += num
        a_ship.Fame += .80 * num
        a_ship.Resources.Ammunition += int(math.ceil(.25 * num))
        a_ship.Resources.Medicine += int(math.ceil(.25 * num))
        self.shipeventafterlt()

    # ship event loot from navy ship Done
    def shipeventltnavy(self, a_ship, a_screen):
        self.mess = "A pirate defeating the navy! Quite an unusual feat, and a juicy loot at that."
        messobj = StrObj.render(self.mess[0:37], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 5))
        messobj = StrObj.render(self.mess[38:], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 25))
        num = random.randint(1, 70)
        a_ship.Wealth += int(math.ceil(2.5 * num))
        a_ship.Fame += int(math.ceil(1.75 * num))
        a_ship.Resources.Ammunition += int(math.ceil(1.25 * num))
        a_ship.Resources.Ammunition += int(math.ceil(.50 * num))
        a_ship.Resources.Medicine += int(math.ceil(.25 * num))
        self.shipeventafterlt()
    
    def shipeventafterlt(self):
        mess = "The enemy is at your mercy, what would you have done to them?"

    # event shark Done
    def sharkevent(self, a_screen, a_ship):
        self.mess = "Captain! There is something that looks like an unusually large fin in the distance"
        sharim = pygame.image.load("shark.png")
        sharim = pygame.transform.scale(sharim, (int(sharim.get_width() * .15), int(sharim.get_height() * .15)))
        a_screen.blit(sharim, (450, 250))
        messobj = StrObj.render(self.mess[0:32], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 5))
        messobj = StrObj.render(self.mess[33:70], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 25))
        messobj = StrObj.render(self.mess[70:], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 45))
        randnum = random.randint(1, 5)
        if randnum < 3:
            self.MenuOp.initshkinop(100, a_ship)
            self.MenuOp.drawmen(a_screen, 0)
        else:
            self.MenuOp.initshregop(100, a_ship)
            self.MenuOp.drawmen(a_screen, 0)

    # event attack regular shark Done
    def sharkeventregshatt(self, a_ship, a_screen):
        self.mess = "The Sea brings to life some of our scariest dreams, today it shows a little mercy, "
        self.mess += "it's but a shark, if we fight, we can live for another day"
        messobj = StrObj.render(self.mess[0:34], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 5))
        messobj = StrObj.render(self.mess[35:69], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 25))
        messobj = StrObj.render(self.mess[69:103], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 45))
        messobj = StrObj.render(self.mess[104:], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 65))
        randnum = random.randint(0, 3)
        a_ship.ShipHp -= randnum
        a_ship.Resources.Ammunition -=2

    # event navigate away regular shark Done
    def sharkeventregshnavaw(self, a_ship, a_screen):
        self.mess = "We just caught a stroke of luck! We escaped the shark!"
        messobj = StrObj.render(self.mess[0:35], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 5))
        messobj = StrObj.render(self.mess[36:], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 25))

    # event attack king shark Done
    def sharkeventkinshatt(self, a_ship, a_screen):
        self.mess = "Woe to us! We've encountered the demon of the sea. May we live to breath another day."
        messobj = StrObj.render(self.mess[0:33], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 5))
        messobj = StrObj.render(self.mess[33:66], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 25))
        messobj = StrObj.render(self.mess[66:], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 45))
        randnum = random.randint(0, 9)
        a_ship.ShipHp -= randnum
        a_ship.CrewHp -= int(math.ceil(.65 * randnum))
        a_ship.Resources.Ammunition -= 3

    # event navigate away king shark Done
    def sharkeventkinshnavaw(self, a_ship, a_screen):
        randnum = random.randint(1, 10)
        if randnum < 10:
            self.mess = "What were you thinking? The king shark sees all in the seas, nothing escapes it's sight"
            self.mess += "What would you order your crew to do? The shark is still attacking."
            messobj = StrObj.render(self.mess[0:33], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 5))
            messobj = StrObj.render(self.mess[33:68], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 25))
            messobj = StrObj.render(self.mess[69:87], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 45))
            messobj = StrObj.render(self.mess[87:113], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 65))
            messobj = StrObj.render(self.mess[113:143], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 85))
            messobj = StrObj.render(self.mess[144:], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 105))
            randnum = random.randint(0, 9)
            a_ship.ShipHp -= int(math.ceil(randnum * .55))
            a_ship.CrewHp -= int(math.ceil(randnum * .45))
            self.MenuOp.initshkinafternavawf(170)
            self.MenuOp.drawmen(a_screen, 0)
        else:
            self.mess = "Impossible! The king shark did not see us! The fates must be asleep."
            messobj = StrObj.render(self.mess[0:35], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 5))
            messobj = StrObj.render(self.mess[35:], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 25))

    # event navigate away king shark Done
    def sharkeventkinshflee(self, a_ship, a_screen):
        self.mess = "When the danger is great, sometimes we must flee to face another day."
        messobj = StrObj.render(self.mess[0:35], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 5))
        messobj = StrObj.render(self.mess[36:], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 25))
        a_ship.ShipHp -= 1
        a_ship.CrewHp -= 1

    # barrel event Done
    def barrelevent(self, a_screen):
        self.mess = "Look! It's a barrel, shall we bring it on board?"
        barImg = pygame.image.load("barrel.png")
        barImg = pygame.transform.scale(barImg, (int(barImg.get_width() * .15), int(barImg.get_height() * .15)))
        a_screen.blit(barImg, (450, 350))
        messobj = StrObj.render(self.mess[0:35], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 5))
        messobj = StrObj.render(self.mess[36:], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 25))
        self.MenuOp.initbarrelop(70)
        self.MenuOp.drawmen(a_screen, 0)

    # barrel event bring aboard Done
    def barreleventbrinab(self, a_ship, a_screen):
        randomnum = random.randint(1, 3)
        if randomnum == 1:
            self.mess = "Oh well it could have been worse, there's nothing in the barrel."
            messobj = StrObj.render(self.mess[0:33], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 5))
            messobj = StrObj.render(self.mess[34:], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 25))
        if randomnum == 2:
            self.mess = "The winds of the sea brings good luck! We've found treasure."
            messobj = StrObj.render(self.mess[0:33], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 5))
            messobj = StrObj.render(self.mess[33:], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 25))
            a_ship.Wealth += 100
        if randomnum == 3:
            self.mess = "It's an explosive! Toss it quickly!"
            messobj = StrObj.render(self.mess, 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 5))
            a_ship.ShipHp -= 3

    # barrel event ignore Done
    def barreleventign(self, a_ship, a_screen):
        self.mess = "Sometimes we need to be cautious, the sea is full of surprises."
        messobj = StrObj.render(self.mess[0:33], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 5))
        messobj = StrObj.render(self.mess[34:], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 25))

    # Event plague Done
    def plagueevent(self, a_screen, a_ship):
        n = random.randint(1, 2)
        d = random.randint(1, 5)
        ypos = 0
        PlagueImage = pygame.image.load("plague.png")
        PlagueImage = pygame.transform.scale(PlagueImage, (int(PlagueImage.get_width() * .15), int(PlagueImage.get_height() * .15)))
        a_screen.blit(PlagueImage, (490, 20))
        a_ship.CrewHp -= d
        self.pladam = d
        if n == 1:
            self.mess = "A long journey without the amenities ashore. Your crew must have eaten"
            self.mess += " some spoiled food and have gotten sick"
            messobj = StrObj.render(self.mess[0:36], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 5))
            messobj = StrObj.render(self.mess[37:65], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 25))
            messobj = StrObj.render(self.mess[65:97], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 45))
            messobj = StrObj.render(self.mess[98:], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 65))
            ypos = 85
        if n == 2:
            self.mess = "A hard and long journey, the wicked scurvy plague is upon us"
            messobj = StrObj.render(self.mess[0:36], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 5))
            messobj = StrObj.render(self.mess[36:], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 25))
            ypos = 45
        self.mess = "You would need " + str(d) + " medicine to heal your crew"
        messobj = StrObj.render(self.mess[0:33], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, ypos))
        messobj = StrObj.render(self.mess[34:], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, ypos + 20))
        self.MenuOp.initplagueop(145)
        self.MenuOp.drawmen(a_screen, 0)

    # Event heal crew from plague Done
    def plagueeventhl(self, a_ship, a_screen):
        if self.pladam <= a_ship.Resources.Medicine:
            a_ship.Resources.Medicine -= self.pladam
            a_ship.CrewHp += self.pladam
            self.mess = "It's always good to store up on some medicine, you healed your crew"
            messobj = StrObj.render(self.mess[0:36], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 5))
            messobj = StrObj.render(self.mess[37:], 1, (0, 0, 0))
            a_screen.blit(messobj, (self.xpos, 25))
        else:
            if a_ship.Resources.Medicine > 0:
                a_ship.Resources.Medicine -= a_ship.Resources.Medicine
                a_ship.CrewHp += a_ship.Resources.Medicine
                self.mess = "You were able to partial heal some of your crew"
                messobj = StrObj.render(self.mess[0:34], 1, (0, 0, 0))
                a_screen.blit(messobj, (self.xpos, 5))
                messobj = StrObj.render(self.mess[35:], 1, (0, 0, 0))
                a_screen.blit(messobj, (self.xpos, 25))
            else:
                d = random.randint(10, 15)
                a_ship.CrewHp -= d
                self.mess = "You don't have enough medicine to heal your crew"
                messobj = StrObj.render(self.mess[0:34], 1, (0, 0, 0))
                a_screen.blit(messobj, (self.xpos, 5))
                messobj = StrObj.render(self.mess[34:], 1, (0, 0, 0))
                a_screen.blit(messobj, (self.xpos, 25))

    # Event wait out from plague Done
    def plagueeventwaout(self, a_ship, a_screen):
        d = random.randint(10, 15)
        a_ship.CrewHp -= d
        self.mess = "You didn't heal the members of your crew, disease spread and took it's toll"
        messobj = StrObj.render(self.mess[0:35], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 5))
        messobj = StrObj.render(self.mess[36:70], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 25))
        messobj = StrObj.render(self.mess[71:], 1, (0, 0, 0))
        a_screen.blit(messobj, (self.xpos, 45))



