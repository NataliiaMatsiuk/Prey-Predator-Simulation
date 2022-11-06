from abc import ABC, abstractmethod
import random

class Cell(ABC):
    # owner  - instance of Ocean
    def __init__(self, offset_coordinate, owner, image = '-'):
        super().__init__()
        self.__offset_coordinate = offset_coordinate
        self.__image = image
        self.__owner = owner


    def __str__(self):
        return f'The cell has coordinates {self.__offset_coordinate}'

    def __repr__(self):
        return f'(Cell: {self.__offset_coordinate}'
    
    def getOwner(self):
        return self.__owner

    def getOffset(self):
        return self.__offset_coordinate[0], self.__offset_coordinate[1]

    def setOffset(self, aCoord):
        self.__offset_coordinate = aCoord

    offset = property(getOffset, setOffset)

    def getImage(self):
        return self.__image
   
    def display(self):
        print(f'{self.__image}')
    
    def process(self):
        pass
      
    def moveFrom(self, frm, to):
        pass
    
    def getPreyNeighborCoord(self):
        return self.getEmptyNeighborCoord(2)

    def getEmptyNeighborCoord(self, value):
        # direction = random.randint(1,4)
        dir_lst = []   
        N = self.north(value)
        E = self.east(value)
        S = self.south(value)
        W = self.west(value)
        n = 0
        while n < 1:
            n += 1
            if N != None:
                dir_lst.append(N)
                break
            elif E != None:
                dir_lst.append(E)
                break
            elif S != None:
                dir_lst.append(S)
                break
            elif W != None:
                dir_lst.append(W)
                break
            else:
                continue
               
        return dir_lst

    def getCellAt(self, aCoord):
        return self.__owner.arr[aCoord[1]][aCoord[0]]

    def assignCellAt(self, aCoord, aCell):
        self.__owner.arr[aCoord[1]][aCoord[0]] = aCell
    
    def getEmptyCellCoord(self):
        rrow = random.randint(0, self.owner.__rows)
        rcol = random.randint(0, self.owner.__columns)
        if self.owner.arr[rrow][rcol] == 0:
            return rrow, rcol

    def east(self, value):
        if not self.__offset_coordinate[1] == self.__owner.columns-1:
            if self.__owner.isCellValue(self.__offset_coordinate[0], self.__offset_coordinate[1]+1, value):
                return self.__offset_coordinate[0], self.__offset_coordinate[1]+1
            else:
                return None

    def north(self, value):
        if not self.__offset_coordinate[0] == 0:
            if self.__owner.isCellValue(self.__offset_coordinate[0]-1, self.__offset_coordinate[1], value):
                return self.__offset_coordinate[0]-1, self.__offset_coordinate[1]
            else:
                return None

    def south(self, value):
        if not self.__offset_coordinate[0] == self.__owner.rows-1:
            if self.__owner.isCellValue(self.__offset_coordinate[0]+1, self.__offset_coordinate[1], value):
                return self.__offset_coordinate[0]+1, self.__offset_coordinate[1]
            else:
                return None

    def west(self, value):
        if not self.__offset_coordinate[1] == 0:
            if self.__owner.isCellValue(self.__offset_coordinate[0], self.__offset_coordinate[1]-1, value):
                return self.__offset_coordinate[0], self.__offset_coordinate[1]-1
            else:
                return None

    def __del__(self):
        pass
       