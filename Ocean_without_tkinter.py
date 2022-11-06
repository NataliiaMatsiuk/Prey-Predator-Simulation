from Cell import *
from Obstacle import *
from Prey import *
from Predator import *
import Exc
import random
import numpy
import tkinter as tk
import time

window = tk.Tk()


class Ocean:
    # cells - array 2D
    def __init__(self, columns = 20, rows = 10, numPrey = 150, numPredators = 20, numObstacles = 75):
        self.__columns = columns
        self.__rows    = rows
        self.__cells = []
        self.__size = self.__columns * self.__rows 
        self.__numPrey = numPrey
        self.__numPredators = numPredators
        self.__numObstacles = numObstacles
        
        self.arr = numpy.zeros((self.__rows, self.__columns))
  
    def __str__(self) -> str:
        return f'The ocean contains of: {self.__cells}'

    def __del__(self):
        print(f'dtor: Ocean({self.__columns}, {self.__rows})')

    def __repr__(self):        
        return repr(self.__cells)

    def initCells(self):
        pass

    def show_ocean(self):
        for r in self.arr:
            for c in r:
                if c == 0:
                    print("-", end = " ")
                elif c == 1:
                    print('#', end = " ")
                elif c == 2:
                    print('f', end = " ")
                elif c == 3:
                    print('S', end = " ")
            print()

    def show_with_tkinter(self):
        for r in range(0, self.__rows):
            for c in range(0, self.__columns):
                frame = tk.Frame(
                    master=window,
                    relief=tk.RAISED,
                    borderwidth=1)
                frame.grid(row=r, column=c)
                if self.arr[r][c] == 0:
                    pr = "-"
                elif self.arr[r][c]== 1:
                    pr = '#'
                elif self.arr[r][c] == 2:
                    pr = 'f'
                elif self.arr[r][c]== 3:
                    pr = 'S'
                label = tk.Label(master=frame, text=f"{pr}")
                # lab['text'] = pr
                label.pack()
        window.update()  

    def getNumObstacles(self):
        return self.__numObstacles

    def setNumObstacles(self, a):
        self.__numObstacles = a

    numObstacles = property(getNumObstacles, setNumObstacles)
    
    def getNumPrey(self):
        return self.__numPrey

    def setNumPrey(self, a):
        self.__numPrey = a

    numPrey = property(getNumPrey, setNumPrey)

    def getnumPredators(self):
        return self.__numPredators

    def setnumPredators(self, a):
        self.__numPredators = a
    
    numPredators = property(getnumPredators, setnumPredators)

    def getSize(self):
        return self.__size

    def addtoarray(self, coord, value, object):
        # coord - tuple of coordinates of the cell
        self.arr[coord[0]][coord[1]] = value
        for cell in self.__cells:
            if cell.getOffset() == coord:
                self.remove(cell)             
                break
        self.__cells.append(object)    

    def removeFromArr(self, coord):
        self.arr[coord[0]][coord[1]] = 0
        for cell in self.__cells:
            if cell.getOffset() == coord:
                self.remove(cell)
                break


    def remove(self, a):
        if not a in self.__cells:
            return
        self.__cells.remove(a)
         

    def get_columns(self):
        return self.__columns

    def set_columns(self, columns):
        self.__columns = columns

    columns = property(get_columns, set_columns)

    def get_rows(self):
        return self.__rows

    def set_rows(self, rows):
        self.__rows = rows

    rows = property(get_rows, set_rows)

    def get_cells(self):
        return self.__cells

    def set_cells(self, cells):
        self.__cells = cells

    cells = property(get_cells, set_cells)

    def displayBorder(self):
        pass

    def displayCells(self): 
        return self.__columns * self.__rows 

    def displayStats(self):
        print(f'The number of prey: {self.__numPrey}, the number of predators: {self.__numPredators}')
        pass


    # object 1 - obstacle, 2 - prey, 3 - predator
    def addObjects(self):
        self.addObject(1)
        self.addObject(2)
        self.addObject(3)

        obst_lst = []
        prey_lst = []
        pred_lst = []
        obj_list = []
        for i in range(0, self.__rows):
            for j in range(0, self.__columns):
                if self.arr[i][j] == 1:
                    self.__cells.append(Obstacle((i,j), self))
                elif self.arr[i][j] == 2:
                    self.__cells.append(Prey((i,j), self))
                elif self.arr[i][j] == 3:
                    self.__cells.append(Predator((i,j), self))
           

    def updateObjects(self):
        pass

    def addObject(self, object):
        num = 0
        if object == 1:
            base = self.__numObstacles
        elif object == 2:
            base = self.__numPrey
        elif object == 3:
            base = self.__numPredators
        else:
            raise Exc.InvalidObject('You are trying to add invalid object')

        while num < base:
            cell_row, cell_col = self.getEmptyCellCoord()
            self.arr[cell_row][cell_col] = object
            num += 1

    def getEmptyCellCoord(self):
        rrow = random.randint(0, self.__rows-1)
        rcol = random.randint(0, self.__columns-1)
        if not self.isCellValue(rrow, rcol, 0):
            rrow, rcol = self.getEmptyCellCoord()
        return rrow, rcol      
      
    def isCellValue(self, coord_x, coord_y, value):
        if self.arr[coord_x][coord_y] == value:
            return True
        else:
            return False

 
