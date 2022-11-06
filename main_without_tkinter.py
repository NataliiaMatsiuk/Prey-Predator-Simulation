
from Ocean_without_tkinter import *
from Cell import *
from Prey import Prey
from Predator import *
from Obstacle import *
import Exc
import time
import tkinter as tk

def validate(number_of_objects, where):
    if number_of_objects > where.getSize():
        raise Exc.NumberIsTooLargeException('The number of objects must be less then the size of the ocean')
    elif number_of_objects <= 0:
        raise Exc.NumberIsLessThenZero('The number of objects must be greater then zero')
    else:
        return number_of_objects

def validate_iter(iter_number, where):
    if iter_number <= 0:
        raise Exc.NumberIsLessThenZero('The number of iterations must be greater then zero')
    else:
        return iter_number
    

def main(): 
    # create ocean   
    ocean1 = Ocean()
    try:
        # try to enter the numbers of obstacles, prey and predators
        obstacles, prey, predators = [int(x) for x in input("Enter number of obstacles, prey and predators (total amount must be <= 200) separated by whitespace: ").split()]
        # validate if entered numbers are less then the size of the ocean
        for i in (obstacles, prey, predators):
            validate(i, ocean1)
        validate(obstacles+prey+predators, ocean1)
    except Exc.NumberIsTooLargeException as err:
            print(f'{err.message}')
    else:     
        # assign number of objects to ocean's attributes   
        ocean1.numObstacles = obstacles
        ocean1.numPrey = prey
        ocean1.numPredators = predators
        try:
            # try to enter the number of iterations
            iter_number = int(input('Enter number of iterations: '))
            # validate if the number of iterations is greater then zero
            validate_iter(iter_number, ocean1)
        except Exc.NumberIsLessThenZero as err:
            print(f'{err.message}')
        else:
            # add objects to the ocean
            ocean1.addObjects()
            k = 0
                     
            while k <= iter_number:
                numPrey = 0
                numPredators = 0
                obj_lst = ocean1.get_cells()
                
                for j in obj_lst:
                    if isinstance(j, Predator):
                        numPredators += 1
                    elif isinstance(j, Prey):
                        numPrey += 1
                # if the number of prey or the number of predators equal to zero - end the loop
                if numPrey == 0 or numPredators == 0:
                    break
                else:
                    # show the ocean
                    # ocean1.show_ocean()
                    ocean1.show_with_tkinter()
                    print(f'Iteration: {k}')
                    print(f'The number of prey is {numPrey}, the number of predators is {numPredators}')
                  
                    time.sleep(0.1)
                    for j in obj_lst:
                        if not isinstance(j, Obstacle):
                            j.process()
                 
                    k += 1
               
main()