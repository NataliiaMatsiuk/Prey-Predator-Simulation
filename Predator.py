from Prey import Prey


class Predator(Prey):
    def __init__(self, offset_coordinate, owner, image = 'S', timeToFeed = 6):
        super().__init__(offset_coordinate, owner)
        self.__image = image
        self.__timeToFeed = timeToFeed

    def __del__(self):
        super().__del__()

    def process(self):
        if not self.__timeToFeed == 0:
            self.__timeToFeed -= 1
            prey_coord_list = super(Prey, self).getPreyNeighborCoord()
            empty_coord_list = super(Prey, self).getEmptyNeighborCoord(0)
            if len(prey_coord_list):
                prey_coord = prey_coord_list[0]        
                self.moveFrom(super(Prey,self).getOffset(), prey_coord)
                self.__timeToFeed = 6
            else:
                if len(empty_coord_list):
                    empty_coord = empty_coord_list[0]  
                    self.moveFrom(super(Prey,self).getOffset(), empty_coord)
        else:
            super(Prey, self).getOwner().removeFromArr(super(Prey,self).getOffset())

        


    def moveFrom(self, frm, to):
        owner =  super(Prey, self).getOwner()
        owner.removeFromArr(to)
        super(Prey, self).setOffset(to)
        owner.arr[frm[0]][frm[1]] = 0
        owner.arr[to[0]][to[1]] = 3
    
        
        
    