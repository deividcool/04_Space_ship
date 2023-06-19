from game.components.power_ups.power_up import PowerUp
from game.utils.constants import SPEED,SPEED_TYPE

class SpaceShip(PowerUp):
    def __init__(self):
        super().__init__(SPEED, SPEED_TYPE)