import pygame
import sys
import MyShip
import MyEvents
import MyActivites
import MyCrew
import MyMenuList

#fig = reg
# Holds list of images to draw
GameSprites = pygame.sprite.Group()

pygame.font.init()
defF = pygame.font.get_default_font()
StrObj = pygame.font.Font(defF, 20)
StrObjT = pygame.font.Font(defF, 40)

# Used to create a image object
# Mysprite is a subclass of pygame.sprite.Sprite
class MySprite(pygame.sprite.Sprite):

    # Default Constructor
    def __init__(self, a_imgnam, a_intx, a_inty):
        # Super class constructor
        pygame.sprite.Sprite.__init__(self)
        # Loads the image into object based on a_imgnam( file name of image)
        try:
            self.image = pygame.image.load(a_imgnam)
        except pygame.error:
            print("Can't load image with name " + a_imgnam)
            raise SystemExit
        # a_intx = x coordinate of image, a_inty = y coordinate of image
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * .40), int(self.image.get_height() * .30)))
        self.rect = pygame.Rect(a_intx, a_inty, 400, 400)

        # Converts image to pygame format (May or may not need)
        self.image = self.image.convert()

    def rotimg(self, a_ang):
        self.image = pygame.transform.rotate(self.image, a_ang)

    def scaimg(self, a_xsc, a_ysc):
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * a_xsc), int(self.image.get_height() * a_ysc)))

class textObj:

    def __init__(self):
        self.Mess = []

def chClick(a_obj, a_startx, a_starty, a_msPosX, a_msPosY):
    xValid = False
    yValid = False
    pReturn = False
    startx = a_obj.get_width()
    if a_startx + a_obj.get_width() > a_msPosX >= a_startx:
          xValid = True
    if a_starty + a_obj.get_height() > a_msPosY >= a_starty:
          yValid = True
    if xValid is True and yValid is True:
        return True
    else:
        return False

def chClickO(a_startx, a_starty, a_msPosX, a_msPosY, a_xspace, a_yspace):

    xValid = False
    yValid = False

    if a_startx + a_xspace > a_msPosX >= a_startx:
        xValid = True
    if a_starty + a_yspace > a_msPosY >= a_starty:
        yValid = True
    if xValid is True and yValid is True:
        return True
    else:
        return False


def detSel(a_ch, a_list):
    i = 0
    toPop = 0
    prev = False
    for ch in a_list:
        if ch == a_ch:
            prev = True
            toPop = i
            break
        i += 1
    if prev is True:
        a_list.pop(toPop)
    else:
        a_list.append(a_ch)


def displaySel(a_list, a_screen, a_wid, a_hei):
    for ch in a_list:
        if ch == 1:
            pygame.draw.rect(a_screen, (255, 0, 0), (10, 10, a_wid, a_hei), 2)
        if ch == 2:
            pygame.draw.rect(a_screen, (255, 0, 0), (261, 10, a_wid, a_hei), 2)
        if ch == 3:
            pygame.draw.rect(a_screen, (255, 0, 0), (551, 10, a_wid, a_hei), 2)
        if ch == 4:
            pygame.draw.rect(a_screen, (255, 0, 0), (10, 286, a_wid, a_hei), 2)
        if ch == 5:
            pygame.draw.rect(a_screen, (255, 0, 0), (261, 286, a_wid, a_hei), 2)
        if ch == 6:
            pygame.draw.rect(a_screen, (255, 0, 0), (551, 286, a_wid, a_hei), 2)
        if ch == 7:
            pygame.draw.rect(a_screen, (255, 0, 0), (10, 562, a_wid, a_hei), 2)
        if ch == 8:
            pygame.draw.rect(a_screen, (255, 0, 0), (261, 562, a_wid, a_hei), 2)


def writeshipinfo(a_ship, a_screen):
    #a_screen.blit(backgroundPB, (0, 500) )
    Fobj = StrObj.render("Food: " + str(a_ship.Resources.Food), 1, (0, 0, 0))
    a_screen.blit(Fobj, (20, 600))
    Fobj = StrObj.render("Beer: " + str(a_ship.Resources.Beer), 1, (0, 0, 0))
    a_screen.blit(Fobj, (20, 640))
    Fobj = StrObj.render("Tool: " + str(a_ship.Resources.Tools), 1, (0, 0, 0))
    a_screen.blit(Fobj, (20, 680))
    Fobj = StrObj.render("Medicene: " + str(a_ship.Resources.Medicine), 1, (0, 0, 0))
    a_screen.blit(Fobj, (20, 720))
    Fobj = StrObj.render("Ammo: " + str(a_ship.Resources.Ammunition), 1, (0, 0, 0))
    a_screen.blit(Fobj, (20, 760))
    Fobj = StrObj.render("Hp: " + str(a_ship.CrewHp), 1, (0, 0, 0))
    a_screen.blit(Fobj, (20, 560))
    Fobj = StrObj.render("Ship Hp: " + str(a_ship.ShipHp), 1, (0, 0, 0))
    a_screen.blit(Fobj, (20, 520))

pygame.init()
FirstTh = True
PlayerShip = MyShip.Ship()
PlayerEvents = MyEvents.Events()
PlayerActi = MyActivites.Activites()
PlayerMenu = MyMenuList.MenuList()
CrewSeleList = []
CrewCh = 0
textObjResF = textObj()
StrFood = ""
StrFoodC = 0
FoodAdd = False
textObjResT = textObj()
StrTool = "0"
StrToolC = 0
ToolAdd = False
increF = 1
textObjResM = textObj()
StrMed = "0"
StrMedC = 0
MedAdd = False
textObjResB = textObj()
StrBeer = "0"
StrBeerC = 0
BeerAdd = False
textObjResA = textObj()
StrAmmo = "0"
StrAmmoC = 0
AmmoAdd = False
TotDays = 0

FoodMinus = False
ToolMinus = False
MedMinus = False
BeerMinus = False
AmmoMinus = False

PlayerCh = "NU"
GameStart = False
levSel = False
GameMaiSc = True
GameTutScr = False
isClTut = False
isClStart = False
isClExit = False
isEasyIs = False
isMedIs = False
isHardIs = False
CrewSelection = False
ResSel = False
NextD = False
isMedCl = False
PlayerRep = False
CurGold = 0
FoodResclic = False
FoodDed = 0
ToolDed = 0
MedDed = 0
BeerDed = 0
AmmoDed = 0
ToolCl = False
MedCl = False
BeerCl = False
AmmoCl = False
DidCl = False
PlayerFis = False
curSp = 0
curFoodC = ""
offsetx = 200
offxsym = 0
offsetytop = 0
offsetytop1 = 0
offsetytop2 = 0
offsetytop3 = 0
offsetytop4 = 0
screenwidth = 800
screenheight = 800
screen = pygame.display.set_mode([1000, 800])
MySpriteNot = MySprite("notpadpaper.png", 600, 0)
JourIm = pygame.image.load("notpadpaper.png")
JourIm = pygame.transform.scale(JourIm, (int(JourIm.get_width() * .40), int(JourIm.get_height() * .30)))
sprobj = GameSprites.add(MySpriteNot)
BackGrouGamImage = pygame.image.load("Background1.png")
BackGrouGamImage = pygame.transform.scale(BackGrouGamImage, (int(BackGrouGamImage.get_width() * 1), int(BackGrouGamImage.get_height() * .80)))
BackGrouImage = pygame.image.load("BackgrCol.jpg")
BackGrouImage = pygame.transform.scale(BackGrouImage, (int(BackGrouImage.get_width() * 2), int(BackGrouImage.get_height() * 2)))

CoverImage = pygame.image.load("Tides and Glory Cover.png")
StartIcon = pygame.image.load("icon-start.png")
StartIcon = pygame.transform.scale(StartIcon, (int(StartIcon.get_width() * .15), int(StartIcon.get_height() * .15)))
TutrIcon = pygame.image.load("icon-tuiturial.png")
TutrIcon = pygame.transform.scale(TutrIcon, (int(TutrIcon.get_width() * .15), int(TutrIcon.get_height() * .15)))
TutImage = pygame.image.load("Tides and Glory Tutorial.png")
HomIcon = pygame.image.load("home button tides and glory.png")
ExitIcon = pygame.image.load("icon-exit.png")
ExitIcon = pygame.transform.scale(ExitIcon, (int(ExitIcon.get_width() * .15), int(ExitIcon.get_height() * .15)))
MapImage = pygame.image.load("resize tide and glory map.png")

CoinIcon = pygame.image.load("tides and glory coin.png")
CoinIcon = pygame.transform.scale(CoinIcon, (int(CoinIcon.get_width() * .20), int(CoinIcon.get_height() * .20)))
FoodIc = pygame.image.load("icon-food.png")
FoodIc = pygame.transform.scale(FoodIc, (int(FoodIc.get_width() * .15), int(FoodIc.get_height() * .15)))
ToolIc = pygame.image.load("icon-tool.png")
ToolIc = pygame.transform.scale(ToolIc, (int(ToolIc.get_width() * .15), int(ToolIc.get_height() * .15)))
MedIc = pygame.image.load("icon-medicine.png")
MedIc = pygame.transform.scale(MedIc, (int(MedIc.get_width() * .15), int(MedIc.get_height() * .15)))
AmIc = pygame.image.load("icon-ammo.png")
AmIc = pygame.transform.scale(AmIc, (int(AmIc.get_width() * .15), int(AmIc.get_height() * .15)))
BeerIc = pygame.image.load("icon-beer.png")
BeerIc = pygame.transform.scale(BeerIc, (int(BeerIc.get_width() * .15), int(BeerIc.get_height() * .15)))


CookImage = pygame.image.load("Job8.png")
CookImage = pygame.transform.scale(CookImage, (int(CookImage.get_width() * .15), int(CookImage.get_height() * .15)))
TechImage = pygame.image.load("Job2.png")
TechImage = pygame.transform.scale(TechImage, (int(TechImage.get_width() * .15), int(TechImage.get_height() * .15)))
PhyImage = pygame.image.load("Job7.png")
PhyImage = pygame.transform.scale(PhyImage, (int(PhyImage.get_width() * .15), int(PhyImage.get_height() * .15)))
FigImage = pygame.image.load("Job1.png")
FigImage = pygame.transform.scale(FigImage, (int(FigImage.get_width() * .15), int(FigImage.get_height() * .15)))
FigImageT = pygame.image.load("Job4.png")
FigImageT = pygame.transform.scale(FigImageT, (int(FigImageT.get_width() * .15), int(FigImageT.get_height() * .15)))
FigImageH = pygame.image.load("Job6.png")
FigImageH = pygame.transform.scale(FigImageH, (int(FigImageH.get_width() * .15), int(FigImageH.get_height() * .15)))
RegImage = pygame.image.load("Job3.png")
RegImage = pygame.transform.scale(RegImage, (int(RegImage.get_width() * .15), int(RegImage.get_height() * .15)))
ThieImage = pygame.image.load("Job5.png")
ThieImage = pygame.transform.scale(ThieImage, (int(ThieImage.get_width() * .15), int(ThieImage.get_height() * .15)))

SelcImg = pygame.image.load("Selctr1.png")
PlusMark = StrObjT.render("+", 1, (0, 0, 0))
MinusMark = StrObjT.render("-", 1, (0, 0, 0))

WaveOneImg = pygame.image.load("wave1.png")
WaveTwoImg = pygame.image.load("wave2.png")
WaveThrImg = pygame.image.load("wave3.png")
ShipImg = pygame.image.load("mainShip.png")
ShipImg = pygame.transform.scale(ShipImg, (int(ShipImg.get_width() * .15), int(ShipImg.get_height() * .15)))
FisImg = pygame.image.load("fish.png")
FisImg = pygame.transform.scale(FisImg, (int(FisImg.get_width() * .15), int(FisImg.get_height() * .15)))
NextDayIc = pygame.image.load("icon-nextday.png")
NextDayIc = pygame.transform.scale(NextDayIc, (int(NextDayIc.get_width() * .15), int(NextDayIc.get_height() * .15)))
MedicineImage = pygame.image.load("medicine.png")
MedicineImage = pygame.transform.scale(MedicineImage, (int(MedicineImage.get_width() * .15), int(MedicineImage.get_height() * .15)))
ToolImage = pygame.image.load("tool.png")
ToolImage = pygame.transform.scale(ToolImage, (int(ToolImage.get_width() * .15), int(ToolImage.get_height() * .15)))
PlaEv = True

backgroundP = pygame.Surface(screen.get_size())
backgroundP.fill((139, 115, 85))
#backgroundP = backgroundP.convert()
screen.blit(backgroundP, (0, 0))
backgroundPB = pygame.Surface((600, 800))
backgroundPB.fill((139, 115, 85))
backgroundPT = pygame.Surface((20, 20))
backgroundPT.fill((250, 250, 250))
#screen.blit(BackGroundImage, (0, 0))
backgroundTypArea = pygame.Surface((100, 40))
backgroundTypArea.fill((250, 250, 250))
selc = "None"

IntMenuList = MyMenuList.MenuList()

StrO = StrObj.render("1", 1, (0, 0, 0))
StrT = StrObj.render("2", 1, (0, 0, 0))
StrTh = StrObj.render("3", 1, (0, 0, 0))
StrFo= StrObj.render("4", 1, (0, 0, 0))
StrFi = StrObj.render("5", 1, (0, 0, 0))
StrSix = StrObj.render("6", 1, (0, 0, 0))
StrSev = StrObj.render("7", 1, (0, 0, 0))
StrEi = StrObj.render("8", 1, (0, 0, 0))
StrNin = StrObj.render("9", 1, (0, 0, 0))
StrZer = StrObj.render("0", 1, (0, 0, 0))

CTFifL = StrObj.render("50", 1, (0, 0, 0))
CHun = StrObj.render("100", 1, (0, 0, 0))
CThHun = StrObj.render("300", 1, (0, 0, 0))
CFifT = StrObj.render("15", 1, (0, 0, 0))
CFiHun = StrObj.render("500", 1, (0, 0, 0))

rectw = CookImage.get_width()
recth = CookImage.get_height()

CurClList = []
for i in range(0, 8):
    CurClList.append(False)
#StrObjTitle = StrObj.render("Tides and Glory", 1, (0, 0, 0,))
#screen.blit(StrObjTitle, (380, 300))
screen.blit(CoverImage, (0, 0))
screen.blit(StartIcon, (600, 260))
screen.blit(TutrIcon, (600, 265 + StartIcon.get_height()))
screen.blit(ExitIcon, (600, 270 + (StartIcon.get_height() * 2)))
notCl = False
BuyImage = StrObj.render("Buy", 1, (0, 0, 0))

GameOver = False
CrewFC = 0
isClHome = False
TotFish = 1
cont = 1
while cont == 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouspos = pygame.mouse.get_pos()
            menitch = IntMenuList.chcl(mouspos[0], mouspos[1])
            PlayerCh = PlayerEvents.MenuOp.chcl(mouspos[0], mouspos[1])
            PlayerChAct = PlayerActi.MenuOp.chcl(mouspos[0], mouspos[1])
            isClHome = chClick(HomIcon, 800, 600, mouspos[0], mouspos[1])
            isEasyIs = chClickO(122, 160, mouspos[0], mouspos[1], 200, 221)
            isMedIs = chClickO(471, 53, mouspos[0], mouspos[1], 307, 276)
            isHardIs = chClickO(854, 193, mouspos[0], mouspos[1], 77, 92)
            if GameMaiSc is True:
                isClStart = chClick(StartIcon, 600, 260, mouspos[0], mouspos[1])
                isClTut = chClick(TutrIcon, 600, 265 + StartIcon.get_height(), mouspos[0], mouspos[1])
                isClExit = chClick(ExitIcon, 600, 270 + (StartIcon.get_height() * 2), mouspos[0], mouspos[1])
            if isClStart is True:
                screen.blit(MapImage, (0, 0))
                levSel = True
                FirstTh = True
                GameMaiSc = False
                isClStart = False
            if isClExit is True:
                sys.exit()
            if isEasyIs is True and levSel is True:
                if FirstTh is False:
                    TotDays = 10
                    screen.blit(backgroundP, (0, 0))
                    IntMenuList.initconsolemen(screenwidth, screenheight)
                    IntMenuList.drawmen(screen, 1)
                    PlayerShip.Gold += 5000
                    PlayerShip.ShipHpBeg = 60
                    PlayerShip.ShipHp = 60
                    levSel = False
                    CrewSelection = True
                    FirstTh = True
                    GameOver = False
            if isMedIs is True and levSel is True:
                if FirstTh is False:
                    TotDays = 20
                    screen.blit(backgroundP, (0, 0))
                    IntMenuList.initconsolemen(screenwidth, screenheight)
                    IntMenuList.drawmen(screen, 1)
                    PlayerShip.Gold += 4000
                    PlayerShip.ShipHpBeg = 60
                    PlayerShip.ShipHp = 60
                    levSel = False
                    CrewSelection = True
                    FirstTh = True
                    GameOver = False
            if isHardIs is True and levSel is True:
                if FirstTh is False:
                    TotDays = 30
                    screen.blit(backgroundP, (0, 0))
                    IntMenuList.initconsolemen(screenwidth, screenheight)
                    IntMenuList.drawmen(screen, 1)
                    PlayerShip.Gold += 3000
                    PlayerShip.ShipHpBeg = 60
                    PlayerShip.ShipHp = 60
                    levSel = False
                    CrewSelection = True
                    FirstTh = True
                    GameOver = False
            if ResSel is True:
                FoodAdd = chClick(PlusMark, offxsym, offsetytop, mouspos[0], mouspos[1])
                ToolAdd = chClick(PlusMark, offxsym, offsetytop1, mouspos[0], mouspos[1])
                MedAdd = chClick(PlusMark, offxsym, offsetytop2, mouspos[0], mouspos[1])
                BeerAdd = chClick(PlusMark, offxsym, offsetytop3, mouspos[0], mouspos[1])
                AmmoAdd = chClick(PlusMark, offxsym, offsetytop4, mouspos[0], mouspos[1])
                FoodMinus = chClick(MinusMark, offxsym + 40, offsetytop, mouspos[0], mouspos[1])
                ToolMinus = chClick(MinusMark, offxsym + 40, offsetytop1, mouspos[0], mouspos[1])
                MedMinus = chClick(MinusMark, offxsym + 40, offsetytop2, mouspos[0], mouspos[1])
                BeerMinus = chClick(MinusMark, offxsym + 40, offsetytop3, mouspos[0], mouspos[1])
                AmmoMinus = chClick(MinusMark, offxsym + 40, offsetytop4, mouspos[0], mouspos[1])
            if GameStart is True:
                PlayerFis = chClick(FisImg, 900, 600, mouspos[0], mouspos[1])
                PlayerRep = chClick(ToolImage, 900, 700, mouspos[0], mouspos[1])
                isMedCl = chClick(MedicineImage, 600, 700, mouspos[0], mouspos[1])
                NextD = chClick(NextDayIc, 600, 600, mouspos[0], mouspos[1])
            if isClTut is True:
                screen.blit(TutImage, (0, 0))
                screen.blit(HomIcon, (800, 600))
                GameMaiSc = False
                GameTutScr = True
            if isClHome is True and GameTutScr is True:
                screen.blit(CoverImage, (0, 0))
                screen.blit(StartIcon, (600, 260))
                screen.blit(TutrIcon, (600, 265 + StartIcon.get_height()))
                screen.blit(ExitIcon, (600, 270 + (StartIcon.get_height() * 2)))
                GameMaiSc = True
            if CrewSelection is True:
                screen.blit(BackGrouImage, (0, 0))
                CrewCh = 0
                offsetxls = 10
                offsetyls = 10
                offsetytop = 10
                offsetymid = offsetytop + CookImage.get_height() + 150
                offsetybot = offsetymid + CookImage.get_height() + 150
                offsetym = [0, 0, 0, 0, 0]
                offset1yl = offsetytop + FoodIc.get_width() + 5
                offset2yl = offsetymid + FoodIc.get_height() + 5
                offsetxm = (screenwidth / 2) - (TechImage.get_width() / 2) - 90
                offset1xm = offsetxm + CookImage.get_width() + 5
                offset2xm = offsetxm + FoodIc.get_width() + 5
                offset1xl = offsetxls + CookImage.get_width() + 5
                offset2xl = offset1xl + FoodIc.get_width() + 5
                offsetxr = screenwidth - TechImage.get_width() - 150
                offsetcostp = 70
                offsethp = 30
                for i in range(0, 5):
                    offsetym[i] = offsetymid + (i * FoodIc.get_height()) + (i * 5)
                #screen.blit(backgroundP, (0, 0))
                screen.blit(CookImage, (10, 10))
                offsetxl = CookImage.get_width() + 15
                CFooL = StrObj.render("Food", 1, (0, 0, 0))
                CCostL = StrObj.render("Cost", 1,(0, 0, 0))
                CHpL = StrObj.render("Hp", 1, (0, 0, 0))
                CTwen = StrObj.render("20", 1, (0, 0, 0))
                CTenL = StrObj.render("10", 1, (0, 0, 0))
                CTWenL = StrObj.render("20", 1, (0, 0, 0))
                CZeroL = StrObj.render("0", 1, (0, 0, 0))
                CFiveL = StrObj.render("5", 1, (0, 0, 0))
                CFortL = StrObj.render("40", 1, (0, 0, 0))
                CTHun = StrObj.render("200", 1, (0, 0, 0))
                CThFif = StrObj.render("350", 1, (0, 0, 0))
                CSevHun = StrObj.render("700", 1, (0, 0, 0))
                screen.blit(FoodIc, (CookImage.get_width() + 15, 10))
                offset1 = offsetxl + FoodIc.get_width()
                screen.blit(CTwen, (offset1 + 5, 10))
                screen.blit(CoinIcon, (offsetxls, offsetytop + CookImage.get_height() + 10))
                screen.blit(CTHun, (offsetxls + offsetcostp, offsetytop + CookImage.get_height() + 10))
                screen.blit(CHpL, (offsetxls, offsetytop + CookImage.get_height() + CoinIcon.get_height() + 20))
                screen.blit(CFifT, (offsetxls + offsetcostp, offsetytop + CookImage.get_height() + CoinIcon.get_height() + 20))


                CTools = StrObj.render("20", 1, (0, 0, 0))
                #100
                offsetxm = (screenwidth / 2) - (TechImage.get_width() / 2) - 90

                offsetxm1 = offsetxm + FoodIc.get_width() + 15
                offset1 = offsetxm + TechImage.get_width() + 10
                offset1x = offset1 + ToolIc.get_width() + 5
                offset2y = offsetytop + FoodIc.get_height() + 5

                screen.blit(TechImage, (offsetxm, 10))
                screen.blit(ToolIc, (offset1, offsetytop))
                screen.blit(CTools, (offset1x, offsetytop))
                screen.blit(CoinIcon, (offsetxm, offsetytop + CookImage.get_height() + 10))
                screen.blit(CThFif, (offsetxm + offsetcostp, offsetytop + CookImage.get_height() + 10))
                screen.blit(CHpL, (offsetxm, offsetytop + CookImage.get_height() + CoinIcon.get_height() + 20))
                screen.blit(CFiveL, (offsetxm + offsetcostp, offsetytop + CookImage.get_height() + CoinIcon.get_height() + 20))

                screen.blit(PhyImage, (offsetxr, 10))
                CMedC = StrObj.render("35", 1, (0, 0, 0))
                offset1 = offsetxr + TechImage.get_width() + 10
                offset1x = offset1 + FoodIc.get_width() + 5
                offset3y = offsetytop + (FoodIc.get_height() * 2) + 15
                screen.blit(MedIc, (offset1, offsetytop))
                screen.blit(CMedC, (offset1x, offsetytop))
                screen.blit(CoinIcon, (offsetxr, offsetytop + CookImage.get_height() + 10))
                screen.blit(CSevHun, (offsetxr + offsetcostp, offsetytop + CookImage.get_height() + 10))
                screen.blit(CHpL, (offsetxr, offsetytop + CookImage.get_height() + CoinIcon.get_height() + 20))
                screen.blit(CTwen, (offsetxr + offsetcostp, offsetytop + CookImage.get_height() + CoinIcon.get_height() + 20))

                offsety1l = offsetymid + CookImage.get_width() + 5
                offset1xm = offsetxm + CookImage.get_width() + 5
                offset2xm = offset1xm + FoodIc.get_width() + 5
                offset1ym = offsetymid + (FoodIc.get_height() * 1) + 15
                offset4ym = offsetymid + (FoodIc.get_height() * 4) + 15
                offset1xr = offsetxr + CookImage.get_width() + 5
                offset4yr = offsetymid + (FoodIc.get_height() * 4) + 15
                offset2xr = offset1xr + FoodIc.get_width() + 5
                offset4mr = offsetymid + (FoodIc.get_height() * 4) + 15

                screen.blit(FigImage, (10, offsetymid))
                screen.blit(FoodIc, (offset1xl + 40, offsetymid))
                screen.blit(CFiveL, (offset2xl + 40, offsetymid))
                screen.blit(ToolIc, (offset1xl + 40, offset2yl))
                screen.blit(CFiveL, (offset2xl + 40, offset2yl))
                screen.blit(AmIc, (offset1xl + 40, offsetym[4]))
                screen.blit(CFiveL, (offset2xl + 40, offsetym[4]))
                screen.blit(MedIc, (offset1xl + 40, offsetym[2]))
                screen.blit(CFiveL, (offset2xl + 40, offsetym[2]))
                screen.blit(BeerIc, (offset1xl + 40, offsetym[3]))
                screen.blit(CFiveL, (offset2xl + 40, offsetym[3]))
                screen.blit(CoinIcon, (offsetxls, offsetymid + CookImage.get_height() + 10))
                screen.blit(CTHun, (offsetxls + offsetcostp, offsetymid + CookImage.get_height() + 10))
                screen.blit(CHpL, (offsetxls, offsetymid + CookImage.get_height() + CoinIcon.get_height() + 20))
                screen.blit(CFiveL, (offsetxls + offsetcostp, offsetymid + CookImage.get_height() + CoinIcon.get_height() + 20))

                screen.blit(FigImageT, (offsetxm, offsetymid))
                screen.blit(AmIc, (offset1xm, offsetymid))
                screen.blit(CoinIcon, (offsetxm, offsetymid + CookImage.get_height() + 10))
                screen.blit(CHun, (offsetxm + offsetcostp, offsetymid + CookImage.get_height() + 10))
                screen.blit(CHpL, (offsetxm, offsetymid + CookImage.get_height() + CoinIcon.get_height() + 20))
                screen.blit(CTenL, (offsetxm + offsetcostp, offsetymid + CookImage.get_height() + CoinIcon.get_height() + 20))

                screen.blit(FigImageH, (offsetxr, offsetymid))
                screen.blit(AmIc, (offset1xr, offsetymid))
                screen.blit(CTWenL, (offset2xr, offsetymid))
                screen.blit(CoinIcon, (offsetxr, offsetymid + CookImage.get_height() + 10))
                screen.blit(CTHun, (offsetxr + offsetcostp, offsetymid + CookImage.get_height() + 10))
                screen.blit(CHpL, (offsetxr, offsetymid + CookImage.get_height() + CoinIcon.get_height() + 20))
                screen.blit(CTenL, (offsetxr + offsetcostp, offsetymid + CookImage.get_height() + CoinIcon.get_height() + 20))

                screen.blit(ThieImage, (offsetxm, offsetybot))
                screen.blit(BeerIc, (offset1xl, offsetybot))
                screen.blit(CFortL, (offset2xl, offsetybot))

                screen.blit(FigImageT, (offsetxm, offsetymid))
                screen.blit(AmIc, (offset1xm, offsetybot))
                screen.blit(CFortL, (offset2xm, offsetybot))
                screen.blit(CoinIcon, (offsetxm, offsetybot + CookImage.get_height() + 10))
                screen.blit(CFiHun, (offsetxm + offsetcostp, offsetybot + CookImage.get_height() + 10))
                screen.blit(CHpL, (offsetxm, offsetybot + CookImage.get_height() + CoinIcon.get_height() + 20))
                screen.blit(CFifT, (offsetxm + offsetcostp, offsetybot + CookImage.get_height() + CoinIcon.get_height() + 20))

                screen.blit(AmIc, (offset1xm, offsetymid))
                screen.blit(CTenL, (offset2xm, offsetymid))

                screen.blit(RegImage, (offsetxls, offsetybot))
                screen.blit(CoinIcon, (offsetxls, offsetybot + CookImage.get_height() + 10))
                screen.blit(CThHun, (offsetxls + offsetcostp, offsetybot + CookImage.get_height() + 10))
                screen.blit(CHpL, (offsetxls, offsetybot + CookImage.get_height() + CoinIcon.get_height() + 20))
                screen.blit(CFifT, (offsetxls + offsetcostp, offsetybot + CookImage.get_height() + CoinIcon.get_height() + 20))

                screen.blit(BuyImage, (offsetxr, 640))
                if FirstTh is False:
                    if chClick(CookImage, 10, 10, mouspos[0], mouspos[1]) and CurClList[0] is False:
                        CrewCh = 1
                        CookCre = MyCrew.Crew(1, 5)
                        PlayerShip.Resources.Food += 20
                        PlayerShip.CrewHp += 15
                        PlayerShip.Gold -= 200
                        PlayerShip.addcrewmem(CookCre)
                        CurClList[0] = True
                    elif chClick(CookImage, 10, 10, mouspos[0], mouspos[1]) and CurClList[0] is True:
                        CrewCh = 1
                        PlayerShip.Resources.Food -= 20
                        PlayerShip.CrewHp -= 15
                        PlayerShip.Gold += 200
                        CurClList[0] = False
                    if chClick(TechImage, offsetxm, offsetytop, mouspos[0], mouspos[1]) and CurClList[1] is False:
                        CrewCh = 2
                        TechCre = MyCrew.Crew(2, 3)
                        rectw = CookImage.get_width()
                        recth = CookImage.get_height()
                        ytoth = offsetytop - 2 + recth
                        PlayerShip.CrewHp += 5
                        PlayerShip.Resources.Tools += 20
                        PlayerShip.Gold -= 350
                        PlayerShip.addcrewmem(TechCre)
                        CurClList[1] = True
                    elif chClick(TechImage, offsetxm, offsetytop, mouspos[0], mouspos[1]) and CurClList[1] is True:
                        CrewCh = 2
                        rectw = CookImage.get_width()
                        recth = CookImage.get_height()
                        PlayerShip.CrewHp -= 5
                        PlayerShip.Resources.Tools -= 20
                        PlayerShip.Gold += 350
                        CurClList[1] = False
                    if chClick(PhyImage, offsetxr, offsetytop, mouspos[0], mouspos[1]) and CurClList[2] is False:
                        CrewCh = 3
                        PhyCre = MyCrew.Crew(3, 3)
                        rectw = CookImage.get_width()
                        recth = CookImage.get_height()
                        PlayerShip.Resources.Medicine += 35
                        PlayerShip.Gold -= 700
                        PlayerShip.addcrewmem(PhyCre)
                        PlayerShip.CrewHp += 20
                        CurClList[2] = True
                    elif chClick(PhyImage, offsetxr, offsetytop, mouspos[0], mouspos[1]) and CurClList[2] is True:
                        CrewCh = 3
                        PhyCre = MyCrew.Crew(3, 3)
                        rectw = CookImage.get_width()
                        recth = CookImage.get_height()
                        PlayerShip.Resources.Medicine -= 35
                        PlayerShip.Gold += 700
                        PlayerShip.addcrewmem(PhyCre)
                        PlayerShip.CrewHp -= 20
                        CurClList[2] = False
                    if chClick(FigImage, offsetxls, offsetymid, mouspos[0], mouspos[1]) and CurClList[3] is False:
                        CrewCh = 4
                        RegCre = MyCrew.Crew(4, 4)
                        rectw = CookImage.get_width()
                        recth = CookImage.get_height()
                        PlayerShip.Resources.Food += 5
                        PlayerShip.Resources.Tools += 5
                        PlayerShip.Resources.Medicine += 5
                        PlayerShip.Resources.Beer += 5
                        PlayerShip.Resources.Ammunition += 5
                        PlayerShip.Gold -= 200
                        PlayerShip.CrewHp += 5
                        PlayerShip.addcrewmem(RegCre)
                        CurClList[3] = True
                    elif chClick(FigImage, offsetxls, offsetymid, mouspos[0], mouspos[1]) and CurClList[3] is True:
                        CrewCh = 4
                        PlayerShip.Resources.Food -= 5
                        PlayerShip.Resources.Tools -= 5
                        PlayerShip.Resources.Medicine -= 5
                        PlayerShip.Resources.Beer -= 5
                        PlayerShip.Resources.Ammunition -= 5
                        PlayerShip.Gold += 200
                        PlayerShip.CrewHp -= 5
                        CurClList[3] = False
                    if chClick(FigImageT, offsetxm, offsetymid, mouspos[0], mouspos[1]) and CurClList[4] is False:
                        CrewCh = 5
                        FigOCre = MyCrew.Crew(5, 7)
                        PlayerShip.Resources.Ammunition += 10
                        PlayerShip.Gold -= 100
                        PlayerShip.CrewHp += 10
                        PlayerShip.addcrewmem(FigOCre)
                        CurClList[4] = True
                    elif chClick(FigImageT, offsetxm, offsetymid, mouspos[0], mouspos[1]) and CurClList[4] is True:
                        CrewCh = 5
                        FigOCre = MyCrew.Crew(5, 7)
                        PlayerShip.Resources.Ammunition -= 10
                        PlayerShip.Gold += 100
                        PlayerShip.CrewHp -= 10
                        PlayerShip.addcrewmem(FigOCre)
                        CurClList[4] = False
                    if chClick(FigImageH, offsetxr, offsetymid, mouspos[0], mouspos[1]) and CurClList[5] is False:
                        CrewCh = 6
                        FigTCre = MyCrew.Crew(6, 8)
                        PlayerShip.Resources.Ammunition += 20
                        PlayerShip.Gold -= 200
                        PlayerShip.CrewHp += 10
                        PlayerShip.addcrewmem(FigTCre)
                        CurClList[5] = True
                    elif chClick(FigImageH, offsetxr, offsetymid, mouspos[0], mouspos[1]) and CurClList[5] is True:
                        CrewCh = 6
                        FigTCre = MyCrew.Crew(6, 8)
                        PlayerShip.Resources.Ammunition -= 20
                        PlayerShip.Gold += 200
                        PlayerShip.CrewHp -= 10
                        PlayerShip.addcrewmem(FigTCre)
                        CurClList[5] = False
                    if chClick(RegImage, offsetxls, offsetybot, mouspos[0], mouspos[1]) and CurClList[6] is False:
                        CrewCh = 7
                        ThieCre = MyCrew.Crew(7, 6)
                        rectw = CookImage.get_width()
                        recth = CookImage.get_height()
                        PlayerShip.Resources.Beer += 40
                        PlayerShip.Gold -= 300
                        PlayerShip.addcrewmem(ThieCre)
                        PlayerShip.CrewHp += 15
                        CurClList[6] = True
                    elif chClick(RegImage, offsetxls, offsetybot, mouspos[0], mouspos[1]) and CurClList[6] is True:
                        CrewCh = 7
                        ThieCre = MyCrew.Crew(7, 6)
                        rectw = CookImage.get_width()
                        recth = CookImage.get_height()
                        PlayerShip.Resources.Beer -= 40
                        PlayerShip.Gold += 300
                        PlayerShip.addcrewmem(ThieCre)
                        PlayerShip.CrewHp -= 15
                        CurClList[6] = False
                    if chClick(ThieImage, offsetxm, offsetybot, mouspos[0], mouspos[1]) and CurClList[7] is False:
                        CrewCh = 8
                        FigThCre = MyCrew.Crew(8, 10)
                        rectw = CookImage.get_width()
                        recth = CookImage.get_height()
                        PlayerShip.Resources.Ammunition += 40
                        PlayerShip.Gold -= 500
                        PlayerShip.addcrewmem(FigThCre)
                        PlayerShip.CrewHp += 15
                        CurClList[7] = True
                    elif chClick(ThieImage, offsetxm, offsetybot, mouspos[0], mouspos[1]) and CurClList[7] is True:
                        CrewCh = 8
                        FigThCre = MyCrew.Crew(8, 10)
                        rectw = CookImage.get_width()
                        recth = CookImage.get_height()
                        PlayerShip.Resources.Ammunition -= 40
                        PlayerShip.Gold += 500
                        PlayerShip.addcrewmem(FigThCre)
                        PlayerShip.CrewHp -= 15
                        CurClList[7] = False
                    if chClick(BuyImage, offsetxr, 640, mouspos[0], mouspos[1]):
                        ResSel = True
                        CrewSelection = False
                        FirstTh = True
                        PlayerShip.CrewHpBeg = PlayerShip.CrewHp
                    if CrewCh != 0:
                        detSel(CrewCh, CrewSeleList)
                displaySel(CrewSeleList, screen, rectw, recth)
                CrewFC = len(CrewSeleList)
                CWeaLe = StrObj.render(str(PlayerShip.Gold), 1, (0, 0, 0))
                screen.blit(CWeaLe, (offsetxr, 600))
                screen.blit(CoinIcon, (offsetxr - 50, 600))
            if ResSel is True and FirstTh is True:
                screen.blit(BackGrouImage, (0, 0))
                CurGold = PlayerShip.Gold
                FoodAmt = 0
                offsetytop = 50
                offsetx = 200
                offsetxS = offsetx + FoodIc.get_width() + 5
                offsetxSN = offsetxS + SelcImg.get_width()
                offsetc = 70
                CCostL = StrObj.render("Cost", 1,(0, 0, 0))
                CHunFif = StrObj.render("150", 1, (0, 0, 0))
                CTHun = StrObj.render("200", 1, (0, 0, 0))
                CSevF = StrObj.render("75", 1, (0, 0, 0))
                CHun = StrObj.render("100", 1, (0, 0, 0))

                screen.blit(FoodIc, (offsetx, offsetytop))
                screen.blit(SelcImg, (offsetxS, offsetytop - 10))
                screen.blit(CCostL, (offsetx, offsetytop + FoodIc.get_height() + 5))
                screen.blit(CTFifL, (offsetx + offsetc, offsetytop + FoodIc.get_height() + 5))
                screen.blit(backgroundTypArea, (offsetx + FoodIc.get_width() + curSp + 10, offsetytop))
                screen.blit(StrZer, (offsetx + FoodIc.get_width() + curSp + 10, offsetytop))

                offsetytop1 = offsetytop + FoodIc.get_height() + 40
                screen.blit(ToolIc, (offsetx, offsetytop1))
                screen.blit(CCostL, (offsetx, offsetytop1 + FoodIc.get_height() + 5))
                screen.blit(CHunFif, (offsetx + offsetc, offsetytop1 + FoodIc.get_height() + 5))
                screen.blit(backgroundTypArea, (offsetx + FoodIc.get_width() + curSp + 10, offsetytop1))
                screen.blit(StrZer, (offsetx + FoodIc.get_width() + curSp + 10, offsetytop1))

                offsetytop2 = offsetytop1 + FoodIc.get_height() + 40
                screen.blit(MedIc, (offsetx, offsetytop2))
                screen.blit(CCostL, (offsetx, offsetytop2 + FoodIc.get_height() + 5))
                screen.blit(CTHun, (offsetx + offsetc, offsetytop2 + FoodIc.get_height() + 5))
                screen.blit(backgroundTypArea, (offsetx + FoodIc.get_width() + curSp + 10, offsetytop2))
                screen.blit(StrZer, (offsetx + FoodIc.get_width() + curSp + 10, offsetytop2))

                offsetytop3 = offsetytop2 + FoodIc.get_height() + 40
                screen.blit(BeerIc, (offsetx, offsetytop3))
                screen.blit(CCostL, (offsetx, offsetytop3 + FoodIc.get_height() + 5))
                screen.blit(CSevF, (offsetx + offsetc, offsetytop3 + FoodIc.get_height() + 5))
                screen.blit(backgroundTypArea, (offsetx + FoodIc.get_width() + curSp + 10, offsetytop3))
                screen.blit(StrZer, (offsetx + FoodIc.get_width() + curSp + 10, offsetytop3))

                offsetytop4 = offsetytop3 + FoodIc.get_height() + 40
                screen.blit(AmIc, (offsetx, offsetytop4))
                screen.blit(CCostL, (offsetx, offsetytop4 + FoodIc.get_height() + 5))
                screen.blit(CHun, (offsetx + offsetc, offsetytop4 + FoodIc.get_height() + 5))
                screen.blit(backgroundTypArea, (offsetx + FoodIc.get_width() + curSp + 10, offsetytop4))
                screen.blit(StrZer, (offsetx + FoodIc.get_width() + curSp + 10, offsetytop4))

                offsetytop5 = offsetytop4 + FoodIc.get_height() + 40
                screen.blit(backgroundTypArea, (offsetx, offsetytop5))
                CurGoldS = StrObj.render(str(PlayerShip.Gold), 1, (0, 0, 0))
                screen.blit(CurGoldS, (offsetx, offsetytop5))
                screen.blit(backgroundPT, (offsetx - 28, offsetytop + 15))
                screen.blit(backgroundPT, (offsetx - 28, offsetytop1 + 15))
                screen.blit(backgroundPT, (offsetx - 28, offsetytop2 + 15))
                screen.blit(backgroundPT, (offsetx - 28, offsetytop3 + 15))
                screen.blit(backgroundPT, (offsetx - 28, offsetytop4 + 15))

                offxsym = offsetx + FoodIc.get_width() + backgroundTypArea.get_width() + 20
                screen.blit(PlusMark, (offxsym, offsetytop))
                screen.blit(MinusMark, (offxsym + 40, offsetytop))
                screen.blit(PlusMark, (offxsym, offsetytop1))
                screen.blit(MinusMark, (offxsym + 40, offsetytop1))
                screen.blit(PlusMark, (offxsym, offsetytop2))
                screen.blit(MinusMark, (offxsym + 40, offsetytop2))
                screen.blit(PlusMark, (offxsym, offsetytop3))
                screen.blit(MinusMark, (offxsym + 40, offsetytop3))
                screen.blit(PlusMark, (offxsym, offsetytop4))
                screen.blit(MinusMark, (offxsym + 40, offsetytop4))
                FirstTh = False
            if ResSel is True and FirstTh is False:
                CurGold = PlayerShip.Gold
                temp = CurGold
                if FoodAdd is True:
                    StrFoodC += increF
                    screen.blit(backgroundTypArea, (offsetx + FoodIc.get_width() + curSp + 10, offsetytop))
                    PlayerShip.Resources.Food += increF
                    FoodDed = StrFoodC * 50
                    temp -= FoodDed + ToolDed + MedDed + BeerDed + AmmoDed
                    if temp < 0:
                        StrFoodC -= increF
                        PlayerShip.Resources.Food -= increF
                        FoodDed = StrFoodC * 50
                    StrFoodO = StrObj.render(str(StrFoodC), 1, (0, 0, 0))
                    screen.blit(StrFoodO, (offsetx + FoodIc.get_width() + 10, offsetytop))
                if ToolAdd is True:
                    StrToolC += increF
                    screen.blit(backgroundTypArea, (offsetx + FoodIc.get_width() + curSp + 10, offsetytop1))
                    PlayerShip.Resources.Tools += increF
                    ToolDed = StrToolC * 150
                    temp -= FoodDed + ToolDed + MedDed + BeerDed + AmmoDed
                    if temp < 0:
                        StrToolC -= increF
                        PlayerShip.Resources.Tools -= increF
                        ToolDed = StrToolC * 150
                    StrFoodO = StrObj.render(str(StrToolC), 1, (0, 0, 0))
                    screen.blit(StrFoodO, (offsetx + FoodIc.get_width() + 10, offsetytop1))
                if MedAdd is True:
                    StrMedC += increF
                    screen.blit(backgroundTypArea, (offsetx + FoodIc.get_width() + curSp + 10, offsetytop2))
                    PlayerShip.Resources.Medicine += increF
                    MedDed = StrMedC * 200
                    temp -= FoodDed + ToolDed + MedDed + BeerDed + AmmoDed
                    if temp < 0:
                        StrMedC -= increF
                        PlayerShip.Resources.Medicine -= increF
                        MedDed = StrMedC * 200
                    StrFoodO = StrObj.render(str(StrMedC), 1, (0, 0, 0))
                    screen.blit(StrFoodO, (offsetx + FoodIc.get_width() + 10, offsetytop2))
                if BeerAdd is True:
                    StrBeerC += increF
                    screen.blit(backgroundTypArea, (offsetx + FoodIc.get_width() + curSp + 10, offsetytop3))
                    PlayerShip.Resources.Beer += increF
                    BeerDed = StrBeerC * 75
                    temp -= FoodDed + ToolDed + MedDed + BeerDed + AmmoDed
                    if temp < 0:
                        StrBeerC -= increF
                        PlayerShip.Resources.Beer -= increF
                        BeerDed = StrBeerC * 75
                    StrFoodO = StrObj.render(str(StrBeerC), 1, (0, 0, 0))
                    screen.blit(StrFoodO, (offsetx + FoodIc.get_width() + 10, offsetytop3))
                if AmmoAdd is True:
                    StrAmmoC += increF
                    screen.blit(backgroundTypArea, (offsetx + FoodIc.get_width() + curSp + 10, offsetytop4))
                    PlayerShip.Resources.Ammunition += increF
                    AmmoDed = StrAmmoC * 100
                    temp -= FoodDed + ToolDed + MedDed + BeerDed + AmmoDed
                    if temp < 0:
                        StrAmmoC -= increF
                        PlayerShip.Resources.Ammunition -= increF
                        AmmoDed = StrAmmoC * 100
                    StrFoodO = StrObj.render(str(StrAmmoC), 1, (0, 0, 0))
                    screen.blit(StrFoodO, (offsetx + FoodIc.get_width() + 10, offsetytop4))
                if FoodMinus is True:
                    StrFoodC -= increF
                    screen.blit(backgroundTypArea, (offsetx + FoodIc.get_width() + curSp + 10, offsetytop))
                    PlayerShip.Resources.Food -= increF
                    FoodDed = StrFoodC * 50
                    if StrFoodC < 0:
                        StrFoodC += increF
                        PlayerShip.Resources.Food += increF
                        FoodDed = StrFoodC * 50
                    StrFoodO = StrObj.render(str(StrFoodC), 1, (0, 0, 0))
                    screen.blit(StrFoodO, (offsetx + FoodIc.get_width() + 10, offsetytop))
                if ToolMinus is True:
                    StrToolC -= increF
                    screen.blit(backgroundTypArea, (offsetx + FoodIc.get_width() + curSp + 10, offsetytop1))
                    PlayerShip.Resources.Tools -= increF
                    ToolDed = StrToolC * 150
                    if StrToolC < 0:
                        StrToolC += increF
                        PlayerShip.Resources.Tools += increF
                        ToolDed = StrToolC * 150
                    StrFoodO = StrObj.render(str(StrToolC), 1, (0, 0, 0))
                    screen.blit(StrFoodO, (offsetx + FoodIc.get_width() + 10, offsetytop1))
                if MedMinus is True:
                    StrMedC -= increF
                    screen.blit(backgroundTypArea, (offsetx + FoodIc.get_width() + curSp + 10, offsetytop2))
                    PlayerShip.Resources.Medicine -= increF
                    MedDed = StrMedC * 200
                    if StrMedC < 0:
                        StrMedC += increF
                        PlayerShip.Resources.Medicine += increF
                        MedDed = StrMedC * 200
                    StrFoodO = StrObj.render(str(StrMedC), 1, (0, 0, 0))
                    screen.blit(StrFoodO, (offsetx + FoodIc.get_width() + 10, offsetytop2))
                if BeerMinus is True:
                    StrBeerC -= increF
                    screen.blit(backgroundTypArea, (offsetx + FoodIc.get_width() + curSp + 10, offsetytop3))
                    PlayerShip.Resources.Beer -= increF
                    BeerDed = StrBeerC * 75
                    if StrBeerC < 0:
                        StrBeerC += increF
                        PlayerShip.Resources.Beer += increF
                        BeerDed = StrBeerC * 75
                    StrFoodO = StrObj.render(str(StrBeerC), 1, (0, 0, 0))
                    screen.blit(StrFoodO, (offsetx + FoodIc.get_width() + 10, offsetytop3))
                if AmmoMinus is True:
                    StrAmmoC -= increF
                    screen.blit(backgroundTypArea, (offsetx + FoodIc.get_width() + curSp + 10, offsetytop4))
                    PlayerShip.Resources.Ammunition -= increF
                    AmmoDed = StrAmmoC * 100
                    if StrAmmoC < 0:
                        StrAmmoC += increF
                        PlayerShip.Resources.Ammunition += increF
                        AmmoDed = StrAmmoC * 100
                    StrFoodO = StrObj.render(str(StrAmmoC), 1, (0, 0, 0))
                    screen.blit(StrFoodO, (offsetx + FoodIc.get_width() + 10, offsetytop4))
                if chClick(BuyImage, offsetx, offsetytop5 + 60, mouspos[0], mouspos[1]):
                    GameStart = True
                    ResSel = False
                    FirstTh = True
                screen.blit(CoinIcon, (offsetx - 50, offsetytop5))
                CurGold -= FoodDed + ToolDed + MedDed + BeerDed + AmmoDed
                screen.blit(backgroundTypArea, (offsetx, offsetytop5))
                CurGoldS = StrObj.render(str(CurGold), 1, (0, 0, 0))
                screen.blit(CurGoldS, (offsetx, offsetytop5))
                screen.blit(BuyImage, (offsetx, offsetytop5 + 60))
            if GameStart is True:
                if FirstTh is True:
                    screen.blit(backgroundP, (0, 0))
                    screen.blit(BackGrouGamImage, (0, 0))
                    yposb = BackGrouGamImage.get_height() - WaveThrImg.get_height()
                    screen.blit(WaveThrImg, (0, yposb))
                    yposb = BackGrouGamImage.get_height() - 350
                    screen.blit(ShipImg, (10, yposb))
                    yposb = BackGrouGamImage.get_height() - WaveTwoImg.get_height()
                    screen.blit(WaveTwoImg, (0, yposb))
                    yposb = BackGrouGamImage.get_height() - WaveOneImg.get_height()
                    screen.blit(WaveOneImg, (0, yposb))
                    screen.blit(FisImg, (900, 600))
                    screen.blit(NextDayIc, (600, 600))
                    screen.blit(MedicineImage, (600, 700))
                    screen.blit(ToolImage, (900, 700))
                    ypos = yposb - 150
                    screen.blit(JourIm, (600, 0))
                    PlayerEvents.genrevent(screen, PlayerShip)
                GameOverMess = "You did not survive the trip."
                GameOverMessSurv = "After a long trek, you reach your destination."
                TexGMO = StrObj.render(GameOverMess, 1, (0, 0, 0))
                TexGMOSurv = StrObj.render(GameOverMessSurv, 1, (0, 0, 0))
                writeshipinfo(PlayerShip, screen)
                if PlayerFis is True and PlaEv is False and TotFish == 4:
                    messfishlimit = "No more fishing for the day."
                    messfishlimito = StrObj.render(messfishlimit, 1, (0, 0, 0))
                    screen.blit(JourIm, (600, 0))
                    screen.blit(messfishlimito, (610, 5))
                if PlayerFis is True and PlaEv is False and TotFish < 4:
                    screen.blit(JourIm, (600, 0))
                    PlayerActi.fishing(PlayerShip, screen)
                    TotFish += 1
                if isMedCl is True and PlaEv is False:
                    screen.blit(JourIm, (600, 0))
                    PlayerActi.healcrew(screen)
                if PlayerRep is True and PlaEv is False:
                    screen.blit(JourIm, (600, 0))
                    PlayerActi.repairship(screen)
                if PlayerChAct == "ALL" and PlaEv is False:
                    screen.blit(JourIm, (600, 0))
                    PlayerActi.healcrewall(PlayerShip, screen)
                if PlayerChAct == "10H" and PlaEv is False:
                    screen.blit(JourIm, (600, 0))
                    amoutoheal = int(PlayerChAct[0:2])
                    PlayerActi.healcrewother(PlayerShip, screen, amoutoheal)
                if PlayerChAct == "20H" and PlaEv is False:
                    screen.blit(JourIm, (600, 0))
                    amoutoheal = int(PlayerChAct[0:2])
                    PlayerActi.healcrewother(PlayerShip, screen, amoutoheal)
                if PlayerChAct == "30H" and PlaEv is False:
                    screen.blit(JourIm, (600, 0))
                    amoutoheal = int(PlayerChAct[0:2])
                    PlayerActi.healcrewother(PlayerShip, screen, amoutoheal)
                if PlayerChAct == "40H" and PlaEv is False:
                    screen.blit(JourIm, (600, 0))
                    amoutoheal = int(PlayerChAct[0:2])
                    PlayerActi.healcrewother(PlayerShip, screen, amoutoheal)
                if PlayerChAct == "ALLREP" and PlaEv is False:
                    screen.blit(JourIm, (600, 0))
                    PlayerActi.repairshipall(PlayerShip, screen)
                if PlayerChAct == "SOMREP" and PlaEv is False:
                    screen.blit(JourIm, (600, 0))
                    PlayerActi.repairshipother(PlayerShip, screen)
                if PlayerChAct[2:] == "RP" and PlaEv is False:
                    screen.blit(JourIm, (600, 0))
                    amoutorep = int(PlayerChAct[0:2])
                    PlayerActi.repairshipotheram(PlayerShip, screen, amoutorep)
                if PlayerCh == "ATTC":
                    screen.blit(JourIm, (600, 0))
                    PlayerEvents.shipeventattcargo(PlayerShip, screen)
                if PlayerCh == "IGNC" and PlaEv is True:
                    screen.blit(JourIm, (600, 0))
                    PlayerEvents.shipeventigncargo(PlayerShip, screen)
                    PlaEv = False
                if PlayerCh == "ATTP" and PlaEv is True:
                    screen.blit(JourIm, (600, 0))
                    PlayerEvents.shipeventattpir(PlayerShip, screen)
                if PlayerCh == "IGNP" and PlaEv is True:
                    screen.blit(JourIm, (600, 0))
                    PlayerEvents.shipeventignpir(PlayerShip, screen)
                    if PlayerEvents.EventTyp == "0":
                        PlaEv = False
                if PlayerCh == "BRP" and PlaEv is True:
                    screen.blit(JourIm, (600, 0))
                    PlayerEvents.shipeventbribpir(PlayerShip, screen)
                    PlaEv = False
                if PlayerCh == "FLP" and PlaEv is True:
                    screen.blit(JourIm, (600, 0))
                    PlayerEvents.shipeventfleepir(PlayerShip, screen)
                    PlaEv = False
                if PlayerCh == "ATTN" and PlaEv is True:
                    screen.blit(JourIm, (600, 0))
                    PlayerEvents.shipeventattnav(PlayerShip, screen)
                if PlayerCh == "FLN" and PlaEv is True:
                    screen.blit(JourIm, (600, 0))
                    PlayerEvents.shipeventfleenav(PlayerShip, screen)
                    PlaEv = False
                if PlayerCh == "IGNN" and PlaEv is True:
                    screen.blit(JourIm, (600, 0))
                    PlayerEvents.shipeventignnav(PlayerShip, screen)
                    if PlayerEvents.EventTyp == "0":
                        PlaEv = False
                if PlayerCh == "BRN" and PlaEv is True:
                    screen.blit(JourIm, (600, 0))
                    PlayerEvents.shipeventbribnav(PlayerShip, screen)
                    if PlayerEvents.EventTyp == "0":
                        PlaEv = False
                if PlayerCh == "OBIL" and PlaEv is True:
                    screen.blit(JourIm, (600, 0))
                    PlayerEvents.shipeventob(PlayerShip, screen)
                    PlaEv = False
                if PlayerCh == "LTNON" and PlaEv is True:
                    screen.blit(JourIm, (600, 0))
                    PlayerEvents.shipeventltnonnavy(PlayerShip, screen)
                    PlaEv = False
                if PlayerCh == "LTNAV" and PlaEv is True:
                    screen.blit(JourIm, (600, 0))
                    PlayerEvents.shipeventltnavy(PlayerShip, screen)
                    PlaEv = False
                if PlayerCh == "ATTREGSH" and PlaEv is True:
                    screen.blit(JourIm, (600, 0))
                    PlayerEvents.sharkeventregshatt(PlayerShip, screen)
                    PlaEv = False
                if PlayerCh == "NAVAREGSH" and PlaEv is True:
                    screen.blit(JourIm, (600, 0))
                    PlayerEvents.sharkeventregshnavaw(PlayerShip, screen)
                    PlaEv = False
                if PlayerCh == "ATTKINSH" and PlaEv is True:
                    screen.blit(JourIm, (600, 0))
                    PlayerEvents.sharkeventkinshatt(PlayerShip, screen)
                if PlayerCh == "NAVAKINSH" and PlaEv is True:
                    screen.blit(JourIm, (600, 0))
                    PlayerEvents.sharkeventkinshnavaw(PlayerShip, screen)
                if PlayerCh == "FLSHKIN" and PlaEv is True:
                    screen.blit(JourIm, (600, 0))
                    PlayerEvents.sharkeventkinshflee(PlayerShip, screen)
                    PlaEv = False
                if PlayerCh == "BRIBARAB" and PlaEv is True:
                    screen.blit(JourIm, (600, 0))
                    PlayerEvents.barreleventbrinab(PlayerShip, screen)
                    PlaEv = False
                if PlayerCh == "IGNBAR" and PlaEv is True:
                    screen.blit(JourIm, (600, 0))
                    PlayerEvents.barreleventign(PlayerShip, screen)
                    PlaEv = False
                if PlayerCh == "HEPLA" and PlaEv is True:
                    PlayerEvents.plagueeventhl(PlayerShip, screen)
                    PlaEv = False
                if PlayerCh == "WAOUPLA" and PlaEv is True:
                    PlayerEvents.plagueeventwaout(PlayerShip, screen)
                    PlaEv = False
                screen.blit(backgroundPB, (0, 500))
                writeshipinfo(PlayerShip, screen)
                if TotDays == 0:
                    screen.blit(backgroundP, (0, 0))
                    screen.blit(TexGMOSurv)
                    screen.blit(HomIcon, (800, 600))
                    PlayerShip.Resources.Food = 0
                    PlayerShip.Resources.Tools = 0
                    PlayerShip.Resources.Medicine = 0
                    PlayerShip.Resources.Beer = 0
                    PlayerShip.Resources.Ammunition = 0
                    GameStart = False
                    GameOver = True
                if PlayerShip.Resources.Food <= 0 or PlayerShip.CrewHp <= 0 or PlayerShip.ShipHp <= 0:
                    screen.blit(backgroundP, (0, 0))
                    screen.blit(TexGMO, (300, 400))
                    screen.blit(HomIcon, (800, 600))
                    PlayerShip.Resources.Food = 0
                    PlayerShip.Resources.Tools = 0
                    PlayerShip.Resources.Medicine = 0
                    PlayerShip.Resources.Beer = 0
                    PlayerShip.Resources.Ammunition = 0
                    GameStart = False
                    GameOver = True
                FirstTh = False
        if GameStart is False and GameOver is True and isClHome is True:
            screen.blit(CoverImage, (0, 0))
            screen.blit(StartIcon, (600, 260))
            screen.blit(TutrIcon, (600, 265 + StartIcon.get_height()))
            screen.blit(ExitIcon, (600, 270 + (StartIcon.get_height() * 2)))
            GameMaiSc = True
            GameOver = False
        if NextD is True:
            screen.blit(backgroundP, (0, 0))
            screen.blit(BackGrouGamImage, (0, 0))
            yposb = BackGrouGamImage.get_height() - WaveThrImg.get_height()
            screen.blit(WaveThrImg, (0, yposb))
            yposb = BackGrouGamImage.get_height() - 350
            screen.blit(ShipImg, (10, yposb))
            yposb = BackGrouGamImage.get_height() - WaveTwoImg.get_height()
            screen.blit(WaveTwoImg, (0, yposb))
            yposb = BackGrouGamImage.get_height() - WaveOneImg.get_height()
            screen.blit(WaveOneImg, (0, yposb))
            screen.blit(FisImg, (900, 600))
            screen.blit(NextDayIc, (600, 600))
            screen.blit(MedicineImage, (600, 700))
            screen.blit(ToolImage, (900, 700))
            screen.blit(JourIm, (600, 0))
            PlayerEvents.genrevent(screen, PlayerShip)
            TotDays -= 1
            screen.blit(backgroundPB, (0, 500))
            PlayerShip.Resources.Food -= CrewFC
            TotFish = 1
            PlaEv = True
            writeshipinfo(PlayerShip, screen)
            NextD = False
        FirstTh = False
    pygame.display.flip()
