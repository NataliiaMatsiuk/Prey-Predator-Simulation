Prey – Predator Game
The goal for this project is to create a simple two-dimensional predator-prey simulation. In this simulation the prey are fish and the predators are sharks. These critters live in ocean of a 10 x 20 grid of cells. Only one critter may occupy a cell at a time. The grid is enclosed, so a critter is not allowed to move off the edges of the ocean. Time is simulated in time steps. Each critter performs some action every time step.
The fish behave according to the following model: 
Move. Every time step, randomly try to move up, down, left, or right. If the neighboring cell in the selected direction is occupied or would move the fish off the grid, then the fish stays in the current cell.
Breed. If the fish survives for six time steps, then at the end of the time step (that is; after moving) the fish will breed. This is simulated by creating a new fish in an adjacent (up, down, left, or right) cell that is empty. If there is no empty cell available, then no breeding occurs. Once an offspring is produced, the fish cannot produce an offspring until six more time steps have elapsed.
The sharks behave according to the following model: 
Move. Every time step, if there is an adjacent fish (up, down, left, or right), then the shark will move to that cell and eat the fish. Otherwise, the shark moves according to the same rules as the fish. Note that a shark cannot eat other sharks.

Starve. If a shark has not eaten a fish within the last six time steps, then at the end of the six time step it will starve and die. The shark should then be removed from the grid of cells.
Also the ocean contains obstacles which do not do anything during the game.
To implement this simulation a program was written using Python. The ocean was drawn using ASCII characters of "#" for an obstacle, "f" for a fish, "S" for a shark or "-" for an empty space. 
The class named Cell was created that encapsulates basic data common to obstacles, fish and sharks. This class has an abstract method named Move that is defined in the derived classes of Prey and Predator. 

The game was initialized with the number of obstacles, fish and sharks which are inputs by user as well as the number of iterations. The game lasts until the number of iteration was goaled or the number of fish or sharks equal to zero. 
