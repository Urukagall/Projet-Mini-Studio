<<<<<<< Updated upstream
#Import librairies
import pygame
import math
import pygame.time

#Import Classes
from Class.projectile import Projectile
from Class.player import Player
from Class.enemy import Enemy
from Class.score import Score


#Init the pygame & clock
pygame.init()
clock = pygame.time.Clock()

# Create Window
displayHeight = 1080
displayWidth = 1920
backgroundColor = (200,200,200)
screen = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Endless Scroll")

#Import background model
backGround = pygame.image.load("img/back.png").convert()
backGround = pygame.transform.scale(backGround, (1920, 1080))
backGroundHeight = backGround.get_height()

#Pre-requisite for the screen scrolling
scroll = 0 
tiles = math.ceil(displayHeight / backGroundHeight) + 1

#Import missile model
missile = pygame.image.load("img/missile.png")
missile = pygame.transform.scale(missile, (50, 50))
missileWidth = missile.get_width()

#Import boulles 
classicBullet =  pygame.image.load("img/bullet.png")
classicBullet = pygame.transform.scale(classicBullet, (50, 50))
classicBulletWidth = classicBullet.get_width()

#Bullets & CD
bullets = []
missileCooldown = 0
bulletCoolDown = 0
scoreTime = 0

#Create Player
imgPlayer = pygame.image.load("img/emeu.jpg").convert()
imgPlayer = pygame.transform.scale(imgPlayer, (50, 50))

player = Player(10, 5, 50, displayWidth, displayHeight, 30, 60, 15, 100)

#Create Enemy
imgEnemy = pygame.image.load("img/enemy.png").convert()
imgEnemy = pygame.transform.scale(imgEnemy, (50, 50))

enemy1 = Enemy(50, 2, 300, 0, 50, displayWidth, displayHeight, 100, imgEnemy, 10, 4, math.pi/2)
enemy2 = Enemy(50, 2, 1200, 0, 50, displayWidth, displayHeight, 100, imgEnemy, 10, 4, math.pi/2)
enemy3 = Enemy(50, 2, 500, 0, 50, displayWidth, displayHeight, 100, imgEnemy, 10, 4, math.pi/2)
enemyList = [enemy1, enemy2, enemy3]


#Initiate dash coordinates
timerDash = [0 , 0]

#Initiate score
score = Score()

# Main Loop
running = True
while running:
    font = pygame.font.Font(None, 36)
    # run the game at a constant 60fps
    clock.tick(60)
    #Close window on Escape press
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running=False
        elif events.type == pygame.KEYDOWN:
            if events.key == pygame.K_ESCAPE:
                running=False
    
     #draw scrolling background 
    for i in range(0, tiles):
      screen.blit(backGround,(0,(-1 * i) * backGroundHeight - scroll))

    #scroll background
    scroll -= 5

    #reset scroll
    if abs (scroll) > backGroundHeight:
        scroll = 0

    # Slow movement and dash

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LSHIFT]:
        player.speed = player.slowSpeed
    elif pressed[pygame.K_SPACE] and timerDash[1] == 0:
        timerDash[1] = player.cooldownDash
        timerDash[0] = player.timeDash
        player.speed = player.dashSpeed
    elif timerDash[0] == 0: 
        player.speed = player.basicSpeed

    if timerDash[0] > 0:
        timerDash[0] -= 1
    elif timerDash[0] == 0 and timerDash[1] > 0:
        timerDash[1] -= 1

     #PLAYER Y movement
    if pressed[pygame.K_UP]:
        velY = -1
    elif pressed[pygame.K_DOWN]:
        velY = 1
    else :
        velY = 0
    # PLAYER X movement
    if pressed[pygame.K_RIGHT]:
        velX = 1
    elif pressed[pygame.K_LEFT]:
        velX = -1
    else :
        velX = 0
        
    player.move(velX, velY)

    # Change each bullet location depending on velocity
    for bullet in bullets:
        bullet.y -= bullet.velocity
    
    #Enemy
    for enemy in enemyList:
        rect = pygame.Rect(enemy.x, enemy.y, enemy.size, enemy.size)
        enemy.shoot()
        
        screen.blit(enemy.image, (enemy.x, enemy.y))
        if enemy.y > enemy.displayHeight:
            enemy.health = 0
            enemyList.pop(enemyList.index(enemy))

        #Collision bullet & enemy
        for bullet in bullets:
            bulletRect = pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.width)
            if rect.colliderect(bulletRect):
                enemy.takeDmg(10)
                score.score_increment(10)
                bullets.pop(bullets.index(bullet))

            if(enemy.health <= 0):
                score.score_increment(enemy.score)
                enemyList.pop(enemyList.index(enemy))
                break
        
        playerRect = pygame.Rect(player.X, player.Y, 100, 100)
        if rect.colliderect(playerRect):
            player.takeDmg(10)
            score.score_increment(10)
            enemyList.pop(enemyList.index(enemy))

    #Add a bullet to the bullets list on press
    if pressed[pygame.K_z]:
         if pygame.time.get_ticks() - bulletCoolDown >= 250:
            bullets.append(Projectile(player.X, player.Y, classicBulletWidth, classicBullet))
            bulletCoolDown = pygame.time.get_ticks()
    if pressed[pygame.K_x]:
        if pygame.time.get_ticks() - missileCooldown >= 500:
            bullets.append(Projectile(player.X, player.Y, missileWidth, missile))
            missileCooldown = pygame.time.get_ticks()

    #Score grows automatically
    if pygame.time.get_ticks() - scoreTime >= 3000:
        score.score_increment(30)
        scoreTime = pygame.time.get_ticks()
        
    #Draw player model on screen
    screen.blit(imgPlayer, (player.X, player.Y))
    
    #Draw each missile model on screen
    for bullet in bullets:
        if bullet.y > 0 and bullet.y < 1920 :
            screen.blit(bullet.image, (bullet.x, bullet.y))
        else:
            bullets.pop(bullets.index(bullet))

    scoreText = font.render(f'Score: {score.score}', True, (255, 255, 255))
    screen.blit(scoreText, (10, 10))
    pygame.display.update()

pygame.quit()
=======
#Import librairies
import pygame
import math
import pygame.time
import random

#Import Classes
from Class.projectile import Projectile
from Class.player import Player
from Class.enemy import Enemy
from Class.score import Score
from Class.button import Button
from Class.boss import Boss

#Import Patterns
from Pattern.enemiesPattern import *

#Init the pygame & clock
pygame.init()
clock = pygame.time.Clock()

# Create Window
displayHeight = 1080
displayWidth = 1920
backgroundColor = (200,200,200)
screen = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Bullet Hell")

#Import background model
backGround = pygame.image.load("img/back.png").convert()
backGround = pygame.transform.scale(backGround, (100, 100))
backGroundHeight = backGround.get_height()
backGroundWidth = backGround.get_width()

#Pre-requisite for the screen scrolling
trueScroll = 0 
tilesHeight = math.ceil(displayHeight / backGroundHeight) + 1
tilesWidth = math.ceil(displayWidth / backGroundWidth) + 1

#Import missile model
missile = pygame.image.load("img/missile.png")
missile = pygame.transform.scale(missile, (missile.get_width(), missile.get_height()))
missileWidth = missile.get_width()

#Import bullets 
classicBullet =  pygame.image.load("img/bullet.png")
classicBullet = pygame.transform.scale(classicBullet, (classicBullet.get_width()*2, classicBullet.get_height()*2))
bigBall = pygame.image.load("img/bigBall.png")
bigBall = pygame.transform.scale(bigBall, (50, 50))

#Import ultimate
ultimateShoot = pygame.image.load("img/bigBall.png")
ultimateShoot = pygame.transform.scale(ultimateShoot, (100, 100))
ultimateShootWidth = ultimateShoot.get_width()

ultimateSound = pygame.mixer.Sound("sound/seismic_charge.mp3")
ultimateSound.set_volume(0.2)

# Import Music

bulletHellSound = pygame.mixer.Sound("sound/Bullet_Hell.mp3")
bulletHellSound.set_volume(0.2)

#projectileList & CD
projectileList = []
missileCooldown = 0
bulletCoolDown = 0
ultimateCooldown = 0
scoreTime = 0

particleList = []
shaking = False
screenShake = 40

#Create Player
imgPlayer = pygame.image.load("img/player.png")
imgPlayer = pygame.transform.scale(imgPlayer, (50, 50))

player = Player(10, 5, 50, displayWidth, displayHeight, 30, 60, 15, 5, projectileList, classicBullet, missile)



#Create Enemy
#Load different images
imgRailgun = pygame.image.load("img/railgun.png")
imgRailgun = pygame.transform.scale(imgRailgun, (50, 50))
imgEnemy = pygame.image.load("img/bozo.png")
imgEnemy = pygame.transform.scale(imgEnemy, (50, 50))

enemy1 = Enemy(True, 50, 2, 300, 0, 50, displayWidth, displayHeight, 100, imgRailgun, bigBall, 4, 10, 5, projectileList, 1, "left")
enemy2 = Enemy(True,50, 2, 1200, 0, 50, displayWidth, displayHeight, 100, imgEnemy, bigBall, 10, 3, 10, projectileList, 1, "left")
enemy3 = Enemy(True,50, 2, 500, 0, 50, displayWidth, displayHeight, 100, imgEnemy, bigBall, 10, 3, 10, projectileList, 1, "left")
enemy4 = Enemy(True, 50, 1, 500, 0, 50, displayWidth, displayHeight, 100, imgEnemy, classicBullet, 4, 4, 30, projectileList, 1, "left", 0, 10, 1, 0, 2, bigBall)
enemy5 = Enemy(False, 50, 0.5, 500, 0, 50, displayWidth, displayHeight, 100, imgEnemy, classicBullet, 1, 4, 90, projectileList, 0.5, "left", 3, 1, 1, 0, 3, bigBall)
#enemyList = [enemy1, enemy2, enemy3, enemy4, enemy5]
enemyList = [enemy5]

#create boss
bossSize = 300
bossImg = pygame.image.load("img/boss1.png")
bossImg = pygame.transform.scale(bossImg, (bossSize, bossSize))
boss = Boss(1000, 1, 0, 0, bossSize, 1920, 1080, 1000, bossImg, projectileList, "Left", enemyList)
boss.changePattern(1)
bossFight = True


# Create Button
button_surface = pygame.image.load("img/button.png")
button_surface = pygame.transform.scale(button_surface, (200, 75))

button = Button(button_surface, 500, 500, "Change Weapon price:30", True, 30, Button.ChangeWeapon, imgEnemy)
button2 = Button(button_surface, 900, 700, "Do nothing", False, 0, Button.ChangeWeapon, None)

buttonList = [button, button2]

#Initiate dash coordinates
timerDash = [0 , 0]

#Initiate score
score = Score()

# Main Loop
running = True

# Font importe

font = pygame.font.Font(None, 36)

def rotate(image, rect, angle):
    """Rotate the image while keeping its center."""
    # Rotate the original image without modifying it.
    new_image = pygame.transform.rotate(image, angle)
    # Get a new rect with the center of the old rect.
    rect = new_image.get_rect(center=rect.center)
    return new_image, rect

while running:
    # run the game at a constant 60fps
    clock.tick(60)

    
    #Close window on Escape press
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running=False
        elif events.type == pygame.KEYDOWN:
            if events.key == pygame.K_ESCAPE:
                running=False
        if events.type == pygame.MOUSEBUTTONDOWN:
            for button in buttonList:
                button.checkForInput(pygame.mouse.get_pos(), player)
        for button in buttonList:
            button.changeColor(pygame.mouse.get_pos())
    # Play music in Loop
    
    if bulletHellSound.get_num_channels() == 0:
        bulletHellSound.play()
    
    #draw scrolling background
    
    scroll = int(trueScroll)

    #screen shake
    if shaking:
        scroll += random.randint(0, screenShake) - screenShake/2

    for i in range(0, tilesHeight):
        for j in range(0, tilesWidth):
            screen.blit(backGround, (j*backGround.get_width(), i*backGround.get_height() - trueScroll))
    
    trueScroll += 1
    # reset scroll
    if trueScroll >= backGround.get_height():
        trueScroll = 0

    # Slow movement and dash
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LSHIFT]:
        player.speed = player.slowSpeed
    elif pressed[pygame.K_SPACE] and timerDash[1] == 0:
        timerDash[1] = player.cooldownDash
        timerDash[0] = player.timeDash
        player.speed = player.dashSpeed
    elif timerDash[0] == 0: 
        player.speed = player.basicSpeed

    if timerDash[0] > 0:
        timerDash[0] -= 1
    elif timerDash[0] == 0 and timerDash[1] > 0:
        timerDash[1] -= 1

    #PLAYER Y movement
    if pressed[pygame.K_UP]:
        velY = -1
    elif pressed[pygame.K_DOWN]:
        velY = 1
    else :
        velY = 0

    # PLAYER X movement
    if pressed[pygame.K_RIGHT]:
        velX = 1
    elif pressed[pygame.K_LEFT]:
        velX = -1
    else :
        velX = 0
        
    player.move(velX, velY)
    playerHitbox = pygame.Rect(0,0, player.size/8, player.size/8)
    # center the hitbox on the ship's cockpit
    playerRect = pygame.Rect(player.X+player.size/2 - playerHitbox.width/2, player.Y+player.size/2, playerHitbox.width, playerHitbox.height)

    for bullet in projectileList:
        if bullet.update(enemyList) == True:
            projectileList.pop(projectileList.index(bullet))
        bulletRect = pygame.Rect(bullet.x, bullet.y, bullet.image.get_width(), bullet.image.get_height())
        rotated_image, bulletRect = rotate(bullet.image, bulletRect, bullet.angle)
        screen.blit(rotated_image, (bullet.x, bullet.y))
        if bullet.isPlayer == False:
            #pygame.draw.rect(screen, (255,0,0), bulletRect)
            if playerRect.colliderect(bulletRect):
                player.getHit()
                projectileList.pop(projectileList.index(bullet))
    

    #Enemy
    for enemy in enemyList:
        enemy.update(player)
        rect = pygame.Rect(enemy.x, enemy.y, enemy.size, enemy.size)
        
        screen.blit(enemy.image, (enemy.x, enemy.y))
        if enemy.y > enemy.displayHeight:
            enemy.health = 0
            enemyList.pop(enemyList.index(enemy))

        #Collision bullet & enemy
        for bullet in projectileList:
            if bullet.isPlayer == True:
                bulletRect = pygame.Rect(bullet.x, bullet.y, bullet.size, bullet.size)
                if rect.colliderect(bulletRect):
                    enemy.takeDmg(bullet.damage, enemyList)
                    score.score_increment(10)
                    projectileList.pop(projectileList.index(bullet))

                if(enemy.health <= 0):
                    player.money += 10
                    score.score_increment(enemy.score)
                    break
        if rect.colliderect(playerRect):
            player.getHit()
            score.score_increment(10)
            enemyList.pop(enemyList.index(enemy))

    #Boss
    if bossFight:
        #Change attack pattern base on health
        if boss.health < 500:
            boss.changePattern(2)
        elif boss.health < 300:
            boss.changePattern(3)

        boss.update(player)
        rect = pygame.Rect(boss.x, boss.y, boss.size, boss.size)
        
        screen.blit(boss.image, (boss.x, boss.y))
        if boss.y > boss.displayHeight:
            boss.move(0,-1)

        #Collision bullet & enemy
        for bullet in projectileList:
            if bullet.isPlayer == True:
                bulletRect = pygame.Rect(bullet.x, bullet.y, bullet.size, bullet.size)
                if rect.colliderect(bulletRect):
                    boss.takeDmg(bullet.damage)
                    score.score_increment(10)
                    projectileList.pop(projectileList.index(bullet))

                if(boss.health <= 0):
                    player.money += 100
                    score.score_increment(boss.score)
                    break
        if rect.colliderect(playerRect):
            player.getHit()
            score.score_increment(10)


    for particle in particleList:
        if(particle.draw(screen, projectileList)):
            particleList.pop(particleList.index(particle))
            shaking = False
        else:
            shaking = True
        
        if(particle.doDamage):
            for enemy in enemyList:
                enemy.takeDmg(player.ultimateDmg, enemyList)

    #Add a bullet to the projectileList list on press
    if pressed[pygame.K_w]:
        if player.cooldown <= 0:
            player.shoot()
            if player.speed != player.slowSpeed:
                if player.missileCooldown <= 0:
                    player.shootHoming()
                    player.missileCooldown = player.timeBetweenMissiles
            player.cooldown = player.timeBetweenShots
    if pressed[pygame.K_x]:
        if player.ultimateCooldown <= 0:
            #play sfx
            ultimateSound.play()
            player.shootUltimate(particleList)
            player.ultimateCooldown = player.timeBetweenUltimates
    
    player.cooldown -= 1
    player.missileCooldown -= 1
    player.ultimateCooldown -= 1

    

    #Score grows automatically
    if pygame.time.get_ticks() - scoreTime >= 3000:
        score.score_increment(30)
        scoreTime = pygame.time.get_ticks()
        
    #Draw player model on screen
    screen.blit(imgPlayer, (player.X, player.Y))
    
    #Write player's score & remaining lives 
    scoreText = font.render(f'Score: {score.score}', True, (255, 255, 255))
    screen.blit(scoreText, (10, 10))
    livesText = font.render(f'Lives: {player.lives}', True, (255, 255, 255))
    screen.blit(livesText, (10, 30))
    ultimateText = font.render(f'Ultimate in: {math.ceil(player.ultimateCooldown/60)}', True, (255, 255, 255))
    screen.blit(ultimateText, (10, 50))
    ultimateText = font.render(f'Money: {player.money}', True, (255, 255, 255))
    screen.blit(ultimateText, (10, 70))

    for button in buttonList:
        screen.blit(button.image, button.rect)
        screen.blit(button.text, button.text_rect)
    
    if pressed[pygame.K_LSHIFT]:
        pygame.draw.rect(screen, (0,255,0), playerRect)

    pygame.display.update()

pygame.quit()
>>>>>>> Stashed changes
