import random
import MyMenuList
import pygame

pygame.font.init()
defF = pygame.font.get_default_font()
StrObj = pygame.font.Font(defF, 20)


class Activites:

    def __init__(self):
        self.m_pMenList = []
        self.m_textMenLi = ["N"]
        self.m_posD = []
        self.m_pxStartP = 0
        self.m_pyStartP = 0
        self.m_pSp = 30
        self.m_curMenC = "N"
        self.MenuOp = MyMenuList.MenuList()
        self.Rep = 0
        self.Heal = 0

    # Activity fishing Done
    @staticmethod
    def fishing(a_ship, a_screen):
        fishcau = random.randint(0, 10)
        if fishcau > 0:
            mess = "Your crew successfully caught " + str(fishcau) + " fish, you have more food to sustain"
            mess += " the crew for the journey ahead."
            if fishcau > 9:
                messobj = StrObj.render(mess[0:39], 1, (0, 0, 0))
            else:
                messobj = StrObj.render(mess[0:38], 1, (0, 0, 0))
            a_screen.blit(messobj, (610, 5))
            if fishcau > 9:
                messobj = StrObj.render(mess[39:72], 1, (0, 0, 0))
            else:
                messobj = StrObj.render(mess[38:71], 1, (0, 0, 0))
            a_screen.blit(messobj, (610, 25))
            if fishcau > 9:
                messobj = StrObj.render(mess[73:], 1, (0, 0, 0))
            else:
                messobj = StrObj.render(mess[72:], 1, (0, 0, 0))
            a_screen.blit(messobj, (610, 45))
            a_ship.Resources.Food += fishcau
        else:
            mess = "Fishing is a tedious task. Tough luck try another time."
            messobj = StrObj.render(mess[0:37], 1, (0, 0, 0))
            a_screen.blit(messobj, (610, 5))
            messobj = StrObj.render(mess[38:], 1, (0, 0, 0))
            a_screen.blit(messobj, (610, 25))

    # Activity heal crew Done
    def healcrew(self, a_screen):
        mess = "You have indicated that you would like to heal your crew."
        mess += " How much health do you want restored?"
        messobj = StrObj.render(mess[0:38], 1, (0, 0, 0))
        a_screen.blit(messobj, (610, 5))
        messobj = StrObj.render(mess[39:73], 1, (0, 0, 0))
        a_screen.blit(messobj, (610, 25))
        messobj = StrObj.render(mess[74:], 1, (0, 0, 0))
        a_screen.blit(messobj, (610, 45))
        self.MenuOp.initactivheal(100)
        self.MenuOp.drawmen(a_screen, 0)

    # Activity heal crew all Done
    @staticmethod
    def healcrewall(a_ship, a_screen):
        amountoheal = a_ship.CrewHpBeg - a_ship.CrewHp
        if amountoheal > a_ship.Resources.Medicine:
            mess = "You don't have that amount of medicine, try again with a different amount."
            messobj = StrObj.render(mess[0:30], 1, (0, 0, 0))
            a_screen.blit(messobj, (610, 5))
            messobj = StrObj.render(mess[30:66], 1, (0, 0, 0))
            a_screen.blit(messobj, (610, 25))
            messobj = StrObj.render(mess[67:], 1, (0, 0, 0))
            a_screen.blit(messobj, (610, 45))
        else:
            mess = "You have successfully healed your crew."
            messobj = StrObj.render(mess[0:33], 1, (0, 0, 0))
            a_screen.blit(messobj, (610, 5))
            messobj = StrObj.render(mess[34:], 1, (0, 0, 0))
            a_screen.blit(messobj, (610, 25))
            a_ship.Resources.Medicine -= amountoheal
            a_ship.CrewHp += amountoheal

    # Activity heal crew other Done
    @staticmethod
    def healcrewother(a_ship, a_screen, a_mount):
        if a_mount > a_ship.Resources.Medicine:
            mess = "You don't have that amount of medicine, try again with a different amount."
            messobj = StrObj.render(mess[0:30], 1, (0, 0, 0))
            a_screen.blit(messobj, (610, 5))
            messobj = StrObj.render(mess[30:66], 1, (0, 0, 0))
            a_screen.blit(messobj, (610, 25))
            messobj = StrObj.render(mess[67:], 1, (0, 0, 0))
            a_screen.blit(messobj, (610, 45))
        else:
            mess = "You have successfully healed your crew."
            messobj = StrObj.render(mess[0:33], 1, (0, 0, 0))
            a_screen.blit(messobj, (610, 5))
            messobj = StrObj.render(mess[34:], 1, (0, 0, 0))
            a_screen.blit(messobj, (610, 25))
            a_ship.Resources.Medicine -= a_mount
            a_ship.CrewHp += a_mount
            if a_ship.CrewHp > a_ship.CrewHpBeg:
                a_ship.CrewHp = a_ship.CrewHpBeg

    # Activity repair ship Done
    def repairship(self, a_screen):
        mess = "How much of the ship do you want repaired?"
        messobj = StrObj.render(mess[0:32], 1, (0, 0, 0))
        a_screen.blit(messobj, (610, 5))
        messobj = StrObj.render(mess[33:], 1, (0, 0, 0))
        a_screen.blit(messobj, (610, 25))
        self.MenuOp.initactivrepair(80)
        self.MenuOp.drawmen(a_screen, 0)

    # Activity repair ship all Done
    @staticmethod
    def repairshipall(a_ship, a_screen):
        amountorepair = a_ship.ShipHpBeg - a_ship.ShipHp
        if amountorepair > a_ship.Resources.Tools:
            mess = "You don't have enough tools to repair the entire ship. Try again later."
            messobj = StrObj.render(mess[0:37], 1, (0, 0, 0))
            a_screen.blit(messobj, (610, 5))
            messobj = StrObj.render(mess[38:], 1, (0, 0, 0))
            a_screen.blit(messobj, (610, 25))
        else:
            mess = "Your Ship is all fixed up and as good as new."
            messobj = StrObj.render(mess[0:32], 1, (0, 0, 0))
            a_screen.blit(messobj, (610, 5))
            messobj = StrObj.render(mess[33:], 1, (0, 0, 0))
            a_screen.blit(messobj, (610, 25))
            a_ship.Resources.Tools -= amountorepair
            a_ship.ShipHp += amountorepair

    # Activity repair ship some other question Done
    def repairshipother(self, a_ship, a_screen):
        mess = "How much tools can you spare for repairs?"
        messobj = StrObj.render(mess[0:32], 1, (0, 0, 0))
        a_screen.blit(messobj, (610, 5))
        messobj = StrObj.render(mess[33:], 1, (0, 0, 0))
        a_screen.blit(messobj, (610, 25))
        self.MenuOp.initactivrepairsome(80)
        self.MenuOp.drawmen(a_screen, 0)

    # Activity repair ship some other final result Done
    @staticmethod
    def repairshipotheram(a_ship, a_screen, a_amount):
        if a_amount > a_ship.Resources.Tools:
            mess = "You don't have enough tools to do any reasonable repairs. Hope your journey is not much longer."
            messobj = StrObj.render(mess[0:34], 1, (0, 0, 0))
            a_screen.blit(messobj, (610, 5))
            messobj = StrObj.render(mess[34:68], 1, (0, 0, 0))
            a_screen.blit(messobj, (610, 25))
            messobj = StrObj.render(mess[68:], 1, (0, 0, 0))
            a_screen.blit(messobj, (610, 45))
        else:
            mess = "You have successfully repaired some parts of your ship."
            messobj = StrObj.render(mess[0:35], 1, (0, 0, 0))
            a_screen.blit(messobj, (610, 5))
            messobj = StrObj.render(mess[36:], 1, (0, 0, 0))
            a_screen.blit(messobj, (610, 25))
            a_ship.Resources.Tools -= a_amount
            a_ship.ShipHp += a_amount
            if a_ship.ShipHp > a_ship.ShipHpBeg:
                a_ship.ShipHp = a_ship.ShipHpBeg
