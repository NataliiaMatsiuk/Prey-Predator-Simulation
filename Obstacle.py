from Cell import *

class Obstacle(Cell):
    def __init__(self, offset_coordinate, owner, image = '#'):
        super().__init__(offset_coordinate, owner)
        self.__image = image


   