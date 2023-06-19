from game.components.power_ups.power_up import PowerUp
from game.utils.constants import BULLET_ENEMY,BULLET_TYPE

class Guns(PowerUp):
    def __init__(self):
        super().__init__(BULLET_ENEMY, BULLET_TYPE)