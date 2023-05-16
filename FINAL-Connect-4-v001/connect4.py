# main driver file that imports all other classes and calls main loop
# edit player/AI, AI/AI, or AI/input, or input/input game modes here.
import Board

b = Board.Board()
print(b)
print("\n\nBoard Depth: " + str(b.depth))

point = (0,0)
gV = b.isValidMove(point)
print("Valid? : " + str(gV))
g = b.makeMove(point,1)
print(g)
print("\n\nBoard Depth: " + str(g.depth))