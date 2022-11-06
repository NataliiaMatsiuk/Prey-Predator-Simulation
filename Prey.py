from Cell import *

class Prey(Cell):
    def __init__(self, offset_coordinate, owner, image = 'f', timeToReproduce = 6):
        super().__init__(offset_coordinate, owner)
        self.__image = image
        self.__timeToReproduce = timeToReproduce

    def __del__(self):
        super().__del__()
    
    def getstatus(self):
        return self

    def process(self): 
        empty_coord_list = super().getEmptyNeighborCoord(0)
        if len(empty_coord_list):
            empty_coord = empty_coord_list[0] 
            prev_coord = super().getOffset()       
            self.moveFrom(super().getOffset(), empty_coord)

            if self.__timeToReproduce == 0:
                self.reproduce(prev_coord)
                self.__timeToReproduce = 6
                
        if not self.__timeToReproduce == 0:        
            self.__timeToReproduce -= 1
        

    def moveFrom(self, frm, to):
        owner = super().getOwner()
        super().setOffset(to)
        owner.arr[frm[0]][frm[1]] = 0
        owner.arr[to[0]][to[1]] = 2
   
        
    def reproduce(self, anOffset):    
        owner = super().getOwner()
        new_prey = Prey(anOffset, owner)
        owner.cells.append(new_prey)
        owner.arr[anOffset[0]][anOffset[1]] = 2
        

