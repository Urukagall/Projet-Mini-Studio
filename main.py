#Import librairies
import pygame, sys
import pygame.time

#Import Classes
from Class.player import Player
from Class.button import Button
from Class.gameManager import GameManager
from Functions.jsonReader import *

#Import Patterns
from Functions.enemiesPattern import *
from Functions.options import gameOptions
from Functions.shop import shop
from Functions.play import *
from Functions.credits import credits
from Functions.howToPlay import howToPlay
from Functions.saveReader import saveReader
from SaveFiles.templatePaste import templatePaste

pygame.init()

# Logo windows
icon = pygame.image.load("img/emeu.jpg")
pygame.display.set_icon(icon)

buttonSurface = pygame.image.load("img/assets/button.png")
buttonSurface = pygame.transform.scale(buttonSurface, (buttonSurface.get_width()/1.3, buttonSurface.get_height()/1.3))

#Import missile model
missile = pygame.image.load("img/bullets/missile.png")
missile = pygame.transform.scale(missile, (missile.get_width(), missile.get_height()))
missileWidth = missile.get_width()

#Import bullets 
classicBullet =  pygame.image.load("img/bullets/bullet.png")
classicBullet = pygame.transform.scale(classicBullet, (classicBullet.get_width()*2, classicBullet.get_height()*2))

# Import Carreau modele
carreauBlue =  pygame.image.load("img/bullets/carreau.png")
carreauBlue = pygame.transform.scale(carreauBlue, (carreauBlue.get_width()*2, carreauBlue.get_height()*2))


#projectileList & CD
projectileList = []

imgPlayer = pygame.image.load("img/ships/player.png")
imgPlayer = pygame.transform.scale(imgPlayer, (50, 50))

SCREEN = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Menu")  

BG = pygame.image.load("img/assets/background.png")
BG = pygame.transform.scale(BG, (1920, 1080))

gameManager = GameManager()

menuMusic = pygame.mixer.Sound("sound/menu_music.ogg")
menuMusic.set_volume(0.2 * gameManager.sound)

def darken(image, percent = 50):
    '''Creates a  darkened copy of an image, darkened by percent (50% by default)'''
    newImg = image.copy()
    dark = pygame.Surface(newImg.get_size()).convert_alpha()
    newImg.set_colorkey((0,0,0))
    dark.fill((0,0,0,percent/100*255))
    newImg.blit(dark, (0,0))
    return newImg

darkCarreau = darken(carreauBlue,45).convert_alpha()
darkBullet = darken(classicBullet).convert_alpha()
darkMissile = darken(missile,60).convert_alpha()

player = Player(10, 5, 50, 1920, 1080, 30, 120, 15, 5, projectileList, darkBullet, darkMissile, darkCarreau)

# take the template file to copy to the main json files
templatePaste()

# Take the save from the save.json
saveReader(player)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)

def main_menu():
    running = True
    while running:
        if menuMusic.get_num_channels() == 0:
            menuMusic.play(-1)
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(960, 100))

        PLAY_BUTTON = Button(buttonSurface, 960, 250, "Play", False, None, play, buttonSurface)
        SHOP_BUTTON = Button(buttonSurface, 960, 400, "Shop", False, None, gameOptions, buttonSurface)
        OPTIONS_BUTTON = Button(buttonSurface, 960, 550, "Options", False, None, gameOptions, buttonSurface)
        HOW_TO_PLAY_BUTTON = Button(buttonSurface, 960, 700, "How to play", False, None, howToPlay, buttonSurface)
        CREDITS_BUTTON = Button(buttonSurface, 960, 850, "Credit", False, None, credits, buttonSurface)
        QUIT_BUTTON = Button(buttonSurface, 960, 1000, "Quit", False, None, None, buttonSurface)

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, SHOP_BUTTON, QUIT_BUTTON, HOW_TO_PLAY_BUTTON, CREDITS_BUTTON]:
            button.changeColor(MENU_MOUSE_POS, SCREEN)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    menuMusic.stop()
                    play(player, gameManager)
                if SHOP_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    shop(SCREEN, BG, player, main_menu, gameManager)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    gameOptions(SCREEN, BG, player, main_menu, gameManager, menuMusic)
                if HOW_TO_PLAY_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    howToPlay(SCREEN, BG, player, main_menu)
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    credits(SCREEN, BG, player, main_menu)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    running = False
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        
main_menu()