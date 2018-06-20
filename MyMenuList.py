import pygame
pygame.font.init()
defF = pygame.font.get_default_font()
StrObj = pygame.font.Font(defF, 20)


# Helps organize options player can click on
class MenuList:

    # Default constructor (called when object is intialized (ex. object = Menulist())
    def __init__(self):
        self.m_pMenList = ["N"]
        self.m_textMenLi = ["N"]
        self.m_posD = []
        self.m_pxStartP = 0
        self.m_pyStartP = 0
        self.m_pSp = 30
        self.m_curMenC = "N"
        self.m_pXwid = []
    # Function to intialize where first menue item starts
    # self similar to this in c++
    def topps(self, a_xstartpos, a_ystartpos):
        self.m_pxStartP = a_xstartpos
        self.m_pyStartP = a_ystartpos

    def initstartmen(self):
        del self.m_textMenLi[:]
        del self.m_pMenList[:]
        del self.m_posD[:]
        xpos = self.m_pxStartP - 50
        ypos = self.m_pyStartP - 100
        self.m_pMenList.append(StrObj.render("Tides and Glory", 1, (0, 0, 0)))
        self.m_textMenLi.append("N")
        self.m_posD.append([xpos, ypos])
        ypos += 60
        xpos += 40
        self.m_pMenList.append(StrObj.render("Start", 1, (0, 0, 0)))
        self.m_textMenLi.append("ST")
        self.m_posD.append([xpos, ypos])


    def initlevelchmen(self):
        del self.m_textMenLi[:]
        del self.m_pMenList[:]
        del self.m_posD[:]

        xpos = 40
        ypos = self.m_pyStartP
        self.m_pMenList.append(StrObj.render("Easy", 1, (0, 0, 0)))
        self.m_textMenLi.append("EA")
        self.m_posD.append([xpos, ypos])
        ypos += self.m_pSp
        self.m_pMenList.append(StrObj.render("10 days", 1, (0, 0, 0)))
        self.m_textMenLi.append("")
        self.m_posD.append([xpos, ypos])
        xpos = self.m_pxStartP - 30
        ypos = self.m_pyStartP
        self.m_pMenList.append(StrObj.render("Medium", 1, (0, 0, 0)))
        self.m_textMenLi.append("ME")
        self.m_posD.append([xpos, ypos])
        xpos = self.m_pxStartP  + 250
        ypos = self.m_pyStartP
        self.m_pMenList.append(StrObj.render("Hard", 1, (0, 0, 0)))
        self.m_textMenLi.append("HA")
        self.m_posD.append([xpos, ypos])

    def initconsolemen(self, a_wid, a_hei):
        del self.m_textMenLi[:]
        del self.m_pMenList[:]
        del self.m_posD[:]
        xpos = a_wid - 140
        ypos = a_hei - 80
        self.m_pMenList.append(StrObj.render("Next Day", 1, (0, 0, 0)))
        self.m_textMenLi.append("NXTDAY")
        self.m_posD.append([xpos, ypos])
        xpos = xpos - 150
        self.m_pMenList.append(StrObj.render("Fish", 1, (0, 0, 0)))
        self.m_textMenLi.append("FIS")
        self.m_posD.append([xpos, ypos])
        ypos += 30
        self.m_pMenList.append(StrObj.render("Heal Crew", 1, (0, 0, 0)))
        self.m_textMenLi.append("HEAL")
        self.m_posD.append([xpos, ypos])
        xpos = a_wid - 140
        self.m_pMenList.append(StrObj.render("Repair Ship", 1, (0, 0, 0)))
        self.m_textMenLi.append("REP")
        self.m_posD.append([xpos, ypos])

    def initshipcargoop(self, a_ship):
        del self.m_textMenLi[:]
        del self.m_pMenList[:]
        del self.m_posD[:]
        xpos = 610
        ypos = 120
        if a_ship.Resources.Ammunition >= 2:
            self.m_pMenList.append(StrObj.render("Attack", 1, (0, 0, 0)))
            self.m_textMenLi.append("ATTC")
            self.m_posD.append([xpos, ypos])
        xpos = 800
        self.m_pMenList.append(StrObj.render("Ignore", 1, (0, 0, 0)))
        self.m_textMenLi.append("IGNC")
        self.m_posD.append([xpos, ypos])

    def initshippirop(self, a_ship):
        del self.m_textMenLi[:]
        del self.m_pMenList[:]
        del self.m_posD[:]
        xpos = 610
        ypos = 200
        if a_ship.Resources.Ammunition >= 2:
            self.m_pMenList.append(StrObj.render("Attack", 1, (0, 0, 0)))
            self.m_textMenLi.append("ATTP")
            self.m_posD.append([xpos, ypos])
        xpos = 750
        self.m_pMenList.append(StrObj.render("Ignore", 1, (0, 0, 0)))
        self.m_textMenLi.append("IGNP")
        self.m_posD.append([xpos, ypos])
        xpos = 900
        if a_ship.Resources.Beer >= 2:
            self.m_pMenList.append(StrObj.render("Bribe", 1, (0, 0, 0)))
            self.m_textMenLi.append("BRP")
            self.m_posD.append([xpos, ypos])

    def initshipnavop(self, a_ypos, a_ship):
        del self.m_textMenLi[:]
        del self.m_pMenList[:]
        del self.m_posD[:]
        xpos = 610
        ypos = 200
        if a_ship.Resources.Ammunition >= 2:
            self.m_pMenList.append(StrObj.render("Attack", 1, (0, 0, 0)))
            self.m_textMenLi.append("ATTN")
            self.m_posD.append([xpos, ypos])
        xpos = 750
        self.m_pMenList.append(StrObj.render("Ignore", 1, (0, 0, 0)))
        self.m_textMenLi.append("IGNN")
        self.m_posD.append([xpos, ypos])
        xpos = 900
        if a_ship.Resources.Beer >= 3:
            self.m_pMenList.append(StrObj.render("Bribe", 1, (0, 0, 0)))
            self.m_textMenLi.append("BRN")
            self.m_posD.append([xpos, ypos])

    def initafterattnonnav(self, a_ypos):
        del self.m_textMenLi[:]
        del self.m_pMenList[:]
        del self.m_posD[:]
        xpos = 610
        self.m_pMenList.append(StrObj.render("Destroy", 1, (0, 0, 0)))
        self.m_textMenLi.append("OBIL")
        self.m_posD.append([xpos, a_ypos])
        xpos += 200
        self.m_pMenList.append(StrObj.render("Loot", 1, (0, 0, 0)))
        self.m_textMenLi.append("LTNON")
        self.m_posD.append([xpos, a_ypos])

    def initafterattnav(self, a_ypos):
        del self.m_textMenLi[:]
        del self.m_pMenList[:]
        del self.m_posD[:]
        xpos = 610
        self.m_pMenList.append(StrObj.render("Destroy", 1, (0, 0, 0)))
        self.m_textMenLi.append("OBIL")
        self.m_posD.append([xpos, a_ypos])
        xpos += 200
        self.m_pMenList.append(StrObj.render("Loot", 1, (0, 0, 0)))
        self.m_textMenLi.append("LTNAV")
        self.m_posD.append([xpos, a_ypos])

    def initafterignpir(self, a_ypos):
        del self.m_textMenLi[:]
        del self.m_pMenList[:]
        del self.m_posD[:]
        xpos = 610
        self.m_pMenList.append(StrObj.render("Attack", 1, (0, 0, 0)))
        self.m_textMenLi.append("ATTP")
        self.m_posD.append([xpos, a_ypos])
        xpos = 750
        self.m_pMenList.append(StrObj.render("Flee", 1, (0, 0, 0)))
        self.m_textMenLi.append("FLP")
        self.m_posD.append([xpos, a_ypos])

    def initafterignnav(self, a_ypos):
        del self.m_textMenLi[:]
        del self.m_pMenList[:]
        del self.m_posD[:]
        xpos = 610
        self.m_pMenList.append(StrObj.render("Attack", 1, (0, 0, 0)))
        self.m_textMenLi.append("ATTN")
        self.m_posD.append([xpos, a_ypos])
        xpos = 750
        self.m_pMenList.append(StrObj.render("Flee", 1, (0, 0, 0)))
        self.m_textMenLi.append("FLN")
        self.m_posD.append([xpos, a_ypos])

    def initafterlt(self, a_ypos):
        self.m_pMenList.append(StrObj.render("Mercy", 1, (0, 0, 0)))
        self.m_textMenLi.append("MRCy")
        self.m_posD.append([xpos, a_ypos])
        xpos = 610
        self.m_pMenList.append(StrObj.render("Destroy", 1, (0, 0, 0)))
        self.m_textMenLi.append("FLN")
        self.m_posD.append([xpos, a_ypos])

    def initshregop(self, a_ypos, a_ship):
        del self.m_textMenLi[:]
        del self.m_pMenList[:]
        del self.m_posD[:]
        xpos = 610
        if a_ship.Resources.Ammunition >= 2:
            self.m_pMenList.append(StrObj.render("Attack", 1, (0, 0, 0)))
            self.m_textMenLi.append("ATTREGSH")
            self.m_posD.append([xpos, a_ypos])
        xpos = 750
        self.m_pMenList.append(StrObj.render("Navigate Away", 1, (0, 0, 0)))
        self.m_textMenLi.append("NAVAREGSH")
        self.m_posD.append([xpos, a_ypos])

    def initshkinop(self, a_ypos, a_ship):
        del self.m_textMenLi[:]
        del self.m_pMenList[:]
        del self.m_posD[:]
        xpos = 610
        if a_ship.Resources.Ammunition >= 2:
            self.m_pMenList.append(StrObj.render("Attack", 1, (0, 0, 0)))
            self.m_textMenLi.append("ATTKINSH")
            self.m_posD.append([xpos, a_ypos])
        xpos = 750
        self.m_pMenList.append(StrObj.render("Navigate Away", 1, (0, 0, 0)))
        self.m_textMenLi.append("NAVAKINSH")
        self.m_posD.append([xpos, a_ypos])

    def initshkinafternavaw(self, a_ypos):
        del self.m_textMenLi[:]
        del self.m_pMenList[:]
        del self.m_posD[:]
        xpos = 610
        self.m_pMenList.append(StrObj.render("Attack", 1, (0, 0, 0)))
        self.m_textMenLi.append("ATTKINSH")
        self.m_posD.append([xpos, a_ypos])
        xpos = 750
        self.m_pMenList.append(StrObj.render("Navigate Away", 1, (0, 0, 0)))
        self.m_textMenLi.append("FLSHKIN")
        self.m_posD.append([xpos, a_ypos])

    def initshkinafternavawf(self, a_ypos):
        del self.m_textMenLi[:]
        del self.m_pMenList[:]
        del self.m_posD[:]
        xpos = 610
        self.m_pMenList.append(StrObj.render("Attack", 1, (0, 0, 0)))
        self.m_textMenLi.append("ATTKINSH")
        self.m_posD.append([xpos, a_ypos])
        xpos = 750
        self.m_pMenList.append(StrObj.render("Flee", 1, (0, 0, 0)))
        self.m_textMenLi.append("FLSHKIN")
        self.m_posD.append([xpos, a_ypos])

    def initbarrelop(self, a_ypos):
        del self.m_textMenLi[:]
        del self.m_pMenList[:]
        del self.m_posD[:]
        xpos = 610
        self.m_pMenList.append(StrObj.render("Bring", 1, (0, 0, 0)))
        self.m_textMenLi.append("BRIBARAB")
        self.m_posD.append([xpos, a_ypos])
        xpos = 750
        self.m_pMenList.append(StrObj.render("Ignore", 1, (0, 0, 0)))
        self.m_textMenLi.append("IGNBAR")
        self.m_posD.append([xpos, a_ypos])

    def initplagueop(self, a_ypos):
        del self.m_textMenLi[:]
        del self.m_pMenList[:]
        del self.m_posD[:]
        xpos = 610
        self.m_pMenList.append(StrObj.render("Heal", 1, (0, 0, 0)))
        self.m_textMenLi.append("HEPLA")
        self.m_posD.append([xpos, a_ypos])
        xpos = 750
        self.m_pMenList.append(StrObj.render("Wait Out", 1, (0, 0, 0)))
        self.m_textMenLi.append("WAOUPLA")
        self.m_posD.append([xpos, a_ypos])

    def initactivheal(self, a_ypos):
        del self.m_textMenLi[:]
        del self.m_pMenList[:]
        del self.m_posD[:]
        if len(self.m_pXwid) > 0:
            del self.m_pXwid[:]
        xpos = 610
        self.m_pXwid.append(20)
        self.m_pMenList.append(StrObj.render("All", 1, (0, 0, 0)))
        self.m_textMenLi.append("ALL")
        self.m_posD.append([xpos, a_ypos])
        self.m_pXwid.append(10)
        xpos += 70
        self.m_pMenList.append(StrObj.render("10", 1, (0, 0, 0)))
        self.m_textMenLi.append("10H")
        self.m_posD.append([xpos, a_ypos])
        xpos += 70
        self.m_pMenList.append(StrObj.render("20", 1, (0, 0, 0)))
        self.m_textMenLi.append("20H")
        self.m_posD.append([xpos, a_ypos])
        xpos += 70
        self.m_pMenList.append(StrObj.render("30", 1, (0, 0, 0)))
        self.m_textMenLi.append("30H")
        self.m_posD.append([xpos, a_ypos])
        xpos += 70
        self.m_pMenList.append(StrObj.render("40", 1, (0, 0, 0)))
        self.m_textMenLi.append("40H")
        self.m_posD.append([xpos, a_ypos])

    def initactivrepair(self, a_ypos):
        del self.m_textMenLi[:]
        del self.m_pMenList[:]
        del self.m_posD[:]
        if len(self.m_pXwid) > 0:
            del self.m_pXwid[:]
        xpos = 610
        self.m_pXwid.append(100)
        self.m_pMenList.append(StrObj.render("All", 1, (0, 0, 0)))
        self.m_textMenLi.append("ALLREP")
        self.m_posD.append([xpos, a_ypos])
        xpos = 710
        self.m_pMenList.append(StrObj.render("Some", 1, (0, 0, 0)))
        self.m_textMenLi.append("SOMREP")
        self.m_posD.append([xpos, a_ypos])

    def initactivrepairsome(self, a_ypos):
        del self.m_textMenLi[:]
        del self.m_pMenList[:]
        del self.m_posD[:]
        if len(self.m_pXwid) > 0:
            del self.m_pXwid[:]
        xpos = 610
        self.m_pXwid.append(20)
        self.m_pMenList.append(StrObj.render("10", 1, (0, 0, 0)))
        self.m_textMenLi.append("10RP")
        self.m_posD.append([xpos, a_ypos])
        xpos += 70
        self.m_pMenList.append(StrObj.render("20", 1, (0, 0, 0)))
        self.m_textMenLi.append("20RP")
        self.m_posD.append([xpos, a_ypos])
        xpos += 70
        self.m_pMenList.append(StrObj.render("30", 1, (0, 0, 0)))
        self.m_textMenLi.append("30RP")
        self.m_posD.append([xpos, a_ypos])
        xpos += 70
        self.m_pMenList.append(StrObj.render("40", 1, (0, 0, 0)))
        self.m_textMenLi.append("40RP")
        self.m_posD.append([xpos, a_ypos])

    def drawmen(self, a_screen, a_red=1):
        i = 0
        background = pygame.Surface(a_screen.get_size())
        background.fill((250, 250, 50))
        background = background.convert()
        if a_red == 1:
            a_screen.blit(background, (0, 0))
        for m in self.m_pMenList:
            a_screen.blit(m, (self.m_posD[i]))
            i += 1

    def drawresources(self, a_ship):
        sgoldam = "Gold: " + a_ship.gold
        sfoodamt = "Food: " + a_ship.food
        swateramt = "Water: " + a_ship.water

    def chcl(self, a_xpos, a_ypos):
        xvalid = False
        yvalid = False
        i = 0
        retmess = "NU"
        addsep = 0
        addx = 100
        for pos in self.m_posD:
            if len(self.m_pXwid) > 0:
                addx = self.m_pXwid[addsep]
            if pos[0] <= a_xpos <= pos[0] + self.m_pMenList[i].get_width():
                xvalid = True
            else:
                xvalid = False
            if pos[1] <= a_ypos <= pos[1] + self.m_pMenList[i].get_height():#self.m_pSp:
                yvalid = True
            else:
                yvalid = False
            if xvalid is True and yvalid is True:
                retmess = self.m_textMenLi[i]
                self.m_curMenC = self.m_textMenLi[i]
                break
            if i < len(self.m_pXwid) - 1:
                addsep += 1
            i += 1
        return retmess
