import pygame
import random

from game.components.power_ups.shield import Shield
from game.components.power_ups.gunsx3 import Guns
from game.components.power_ups.speedship import SpaceShip
from game.utils.constants import SPACESHIP_SHIELD,SPACESHIP

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(10000, 30000)
        self.duration = random.randint(3, 5)
        self.power_up_type = None


    def generate_power_up(self):
        power_up_type = random.choice(['shield', 'guns', 'speed'])
    
        if power_up_type == 'shield':
            power_up = Shield()
        elif power_up_type == 'guns':
            power_up = Guns()
        
        elif power_up_type == 'speed':
            power_up = SpaceShip()

        self.power_up_type = power_up_type
        self.when_appears += random.randint(10000, 30000)
        self.power_ups.append(power_up)
    
    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time > self.when_appears:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed,self.power_ups)

            if game.player.rect.colliderect(power_up):
                if self.power_up_type == 'shield':
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.power_up_type = True
                    game.player.power_up_time_up = power_up.start_time + (self.duration * 5000)
                    game.player.set_image((50,75), SPACESHIP_SHIELD)
                    self.power_ups.remove(power_up)
                if self.power_up_type == 'guns':
                    game.player.guns =+ 2    
                    self.power_ups.remove(power_up)
                if self.power_up_type == 'speed':
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.speed += 2    
                    game.player.power_up_type = True
                    game.player.power_up_time_up = power_up.start_time + (self.duration * 2000)
                    game.player.set_image((30,50), SPACESHIP)
                    self.power_ups.remove(power_up)
            else: 
                game.player.set_image((40,65), SPACESHIP)


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)       

    def reset(self):
        now = pygame.time.get_ticks()
        self.power_ups = []
        self.when_appears = random.randint(10000, 30000)    