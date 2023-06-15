from game.components.enemies.enemy import Enemy
from game.components.enemies.enemytwo import EnemyTwo
from game.components.enemies.enemythree import EnemyThree

class EnemyManager:
    def __init__(self):
        self.enemies = []
    
    def update(self, game):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies, game)

    def add_enemy(self):
        if len(self.enemies) < 1:
            enemy = Enemy()
            enemytwo = EnemyTwo()
            enemyThree = EnemyThree()
            self.enemies.append(enemy)
            self.enemies.append(enemytwo)
            self.enemies.append(enemyThree)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
        for enemytwo in self.enemies:
            enemytwo.draw(screen)
        for enemyThree in self.enemies:
            enemyThree.draw(screen)