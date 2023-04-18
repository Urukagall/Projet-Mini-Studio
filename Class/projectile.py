import pygame
import math
import pygame
class Projectile():
    def __init__(self, x, y, width, image, velocity, damage, isHoming, displayWidth, displayHeight, projectileList, speed, player=False, enemyList = [], playerPos = (0,0)):
        self.isPlayer = player
        self.x = x
        self.y = y
        self.velocity = velocity
        self.damage = damage

        self.size = width
        self.image = image
        self.angle = 0
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight

        self.isHoming = isHoming
        self.speed = speed
        self.enemyList = enemyList
        self.playerPos = playerPos
        self.rotationSpeed = 10

        projectileList.append(self)
        
        
    def update(self, enemyList):
        self.enemyList = enemyList
        if(self.isHoming):
            self.chase()
        else:
            self.x += self.velocity[0] * self.speed
            self.y += self.velocity[1] * self.speed
            # Calculer l'angle de rotation nécessaire pour pointer vers l'ennemi
            angle_radians = math.atan2(self.velocity[0] * self.speed, self.velocity[1] * self.speed)
            angle_degrees = math.degrees(angle_radians)
            # Faire pivoter l'image du missile de l'angle calculé
            self.angle = angle_degrees +180

        '''The bullet is destroyed when exiting the screen'''
        #del(self) doesnt actually delete the instance for some reason
        if self.x < 0 - self.size:
            del(self)
            return True
        elif self.x > self.displayWidth + self.size:
            del(self)
            return True
        if self.y < 0 - self.size:
            del(self)
            return True
        elif self.y > self.displayHeight + self.size:
            del(self)
            return True

    def chase(self):
        if(self.isPlayer):
            distance = 10000
            target = pygame.Vector2(self.x, -1000)
            for enemy in self.enemyList:
                if distance > pygame.math.Vector2.distance_to(pygame.math.Vector2(enemy.x, enemy.y), pygame.math.Vector2(self.x, self.y)):
                    distance = pygame.math.Vector2.distance_to(pygame.math.Vector2(enemy.x, enemy.y), pygame.math.Vector2(self.x, self.y))
                    target = pygame.Vector2(enemy.x, enemy.y)
                    
            dx = target.x - self.x
            dy = target.y - self.y
            distance = math.sqrt((dx ** 2) + (dy ** 2))
            # Déplacer le missile vers la cible avec une vitesse constante
            self.x += dx / distance * self.speed
            self.y += dy / distance * self.speed
            # Calculer l'angle de rotation nécessaire pour pointer vers l'ennemi
            angle_radians = math.atan2(dx, dy)
            angle_degrees = math.degrees(angle_radians)
            # Faire pivoter l'image du missile de l'angle calculé
            self.angle = angle_degrees +180
            # rotated_image = pygame.transform.rotate(self.image, -angle_degrees - 90)
            
        else:
            pass