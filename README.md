*Cassandra Chaput*

*Indiana University*

*CSCI-B351 | Intro to AI*

*Fall 2022*


# CONNECT-4 AI GAME

## SUMMARY:

### Algorithms
- We will implement a minimax search algorithm. The minimax tree alternates between Player 1 and Player 2 . The minimax algorithm will use a heuristic to assign a value to each board state on the fringe. The advantageous states will be represented as larger for the advantage of yellow, and smaller for the advantage of red. This will be useful when implementing the use of forward checking ( check the value of the board before deciding if it is a potential positive move) before expanding the state. This will cut down on the states expanded, as the non advantageous states will be ruled out immediately rather than being expanded. 
- Due to to the nature of the minimax algorithm paired with an efficient heuristic function, will allow us to gain the full advantage of A* search. Prior to this being implemented, we do aim to incorporate a Breadth First Search algorithm before the implementation of A*. This will be done to ensure the data structure of the board and player classes are appropriate, as changing things too late will result in a total rewrite. This will also be done to showcase the difference that an efficient algorithm can have on a final programs runtime.

### Third-Party Libraries and Technologies
- Replit will be used in order for all of the group members to have the ability to contribute to the coding section of the project. Replit has the capability for real-time editing between multiple users at once. There is a live chat feed, for easy communication between all of us as well. 
- NumPy has a function called zeros(). This will create a matrix full of zeroes, representing the empty slots/positions. The flip() function will reverse the order of an array of elements along a specified axis, preserving the shape of the array. We can use this to print the board for each player. This package will also allow us to create the board object as it allows for n-th row matrices. 
- Pygame has a module for drawing shapes (pygame.draw). We will use this to draw the game board, and pieces. The board will be one large rectangle with 42 white circles indicating open spaces/holes in the board (7 columns by 6 rows). We will also be using pygame.draw to illustrate each players move/drop into the board. There will be up to 21 yellow circles and 21 red circles, each indicating a players move/drop. In order for our game to be displayed we will use pygame.display() and pygame.display.update()