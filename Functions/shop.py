import pygame
import sys
from Class.button import Button
from Functions.shopBullet import shopBullet
from Functions.shopConsumable import shopConsumable
from Functions.shopShip import shopShip
from Functions.shopSkin import shopSkin


buttonSurface = pygame.image.load("img/ui/button.png")
buttonSurface = pygame.transform.scale(buttonSurface, (buttonSurface.get_width()/1.3, buttonSurface.get_height()/1.3))
imgCoin = pygame.image.load("img/ui/coin.png")
imgCoin = pygame.transform.scale(imgCoin, (80, 40))

RESUME_BUTTON = Button(buttonSurface, 960, 850, "Return", False, None, None, buttonSurface)

# Upgrade Button 
SHIP_BUTTON = Button(buttonSurface, 800, 700, "Ship Upgrade", False, None, None, buttonSurface)

# Skin Button 
SKIN_BUTTON = Button(buttonSurface, 1150, 700, "Skin shop", False, None, None, buttonSurface)

# Consumable Button
CONSUMABLE_BUTTON = Button(buttonSurface, 800, 550, "Power-Up", False, None, None, buttonSurface)

# Upgrade Button bullet
#BULLET_BUTTON = Button(buttonSurface, 1150, 550, "Bullet Upgrade", False, None, None, buttonSurface)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("asset/font.ttf", size)

MENU_TEXT = get_font(100).render("SHOP", True, "#b68f40")
MENU_TEXT_RECT = MENU_TEXT.get_rect(center=(960, 100))
MENU_UPGRADE = get_font(30).render("Upgrade", True, "#b68f40")
MENU_UPGRADE_RECT = MENU_UPGRADE.get_rect(center=(960, 480))

def shop(SCREEN, BG, player, main_menu, gameManager):
    running = True
    while running:
        MENU_MONEY = get_font(20).render(str(player.money), True, "#b68f40")
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(MENU_TEXT, MENU_TEXT_RECT)
        SCREEN.blit(imgCoin,(0 ,50))
        SCREEN.blit(MENU_MONEY, (100,60))

        #for button in [RESUME_BUTTON, SHIP_BUTTON, BULLET_BUTTON, CONSUMABLE_BUTTON, SKIN_BUTTON]:
        for button in [RESUME_BUTTON, SHIP_BUTTON, CONSUMABLE_BUTTON, SKIN_BUTTON]:
            button.changeColor(MENU_MOUSE_POS, SCREEN)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESUME_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    main_menu(False)
                if SHIP_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    shopShip(SCREEN, BG, player, main_menu, gameManager, shop)
                if CONSUMABLE_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    shopConsumable(SCREEN, BG, player, main_menu, gameManager, shop)
                # if BULLET_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                #     shopBullet(SCREEN, BG, player, main_menu, gameManager, shop)
                if SKIN_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    shopSkin(SCREEN, BG, player, main_menu, gameManager, shop)
        pygame.display.update()
