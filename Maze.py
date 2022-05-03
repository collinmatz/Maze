from re import I
import matplotlib.pyplot as plt
import random

class Maze():

    mazeWidth = mazeHeight = 0

    class Cell():
        def __init__(self, i, j):
            self.v = 0
            self.i = i
            self.j = j
            self.par = super()
                
        def getTop(self):
            if self.i - 1 > 0:
                return [self.i-1, self.j]
            else:
                return None
        def getBot(self):
            if self.i < Maze.mazeHeight:
                return [self.i+1, self.j]
            else:
                return None
        def getLeft(self):
            if self.j - 1 > 0:
                return [self.i, self.j-1]
            else:
                return None
        def getRight(self):
            if self.j+1 < Maze.mazeWidth:
                return [self.i, self.j+1]
            else:
                return None


    def __init__(self, width, height):
        mazeHeight = height
        mazeWidth = width
        self.w = width
        self.h = height
        maze = []
        # initialize maze
        for i in range(self.h):
            line = []
            for j in range(self.w):
                line.append(self.Cell(i, j))
            maze.append(line)
        self.maze = maze
        self.generateMaze()


    def generateMaze(self):
        walls = [] # queue of walls to process

        startH = int(random.random()*self.h)
        startW = int(random.random()*self.w)

        # pick a random height and width to start at, do not start on edge
        if startH == 0:
            startH += 1
        elif startH == self.h - 1:
            startH -= 1
        if startW == 0:
            startW += 1
        elif startW == self.w - 1:
            startW -= 1

        # mark cell as known, add adjacent cells idx to queue
        cell = self.maze[startH][startW]
        cell.v = 1
        walls.append([startW, startH-1])
        walls.append([startW, startH+1])
        walls.append([startW-1, startH])
        walls.append([startW+1, startH])

        # loop through all walls until there are no more cells to process
        while walls:
            wall = random.choice(walls)
            cell = self.maze[wall[0]][wall[1]]
            cell.v = 1
            sCells = self.surroundingCells(self.maze[wall[0]][wall[1]])

            if sCells < 2:
                if wall[0] - 1 > -1:
                    walls.append([wall[0]-1, wall[1]])
                if wall[0] < self.w - 1:
                    walls.append([wall[0]+1, wall[1]])
                if wall[1] - 1 > -1:
                    walls.append([wall[0], wall[1]-1])
                if wall[1] < self.h - 1:
                    walls.append([wall[0], wall[1]+1])
            walls.remove(wall)

    
    """
    surroundingCells
    @param cell : Maze.Cell object

    Desc: Returns the number of known cells that surround a designated cell
    """
    def surroundingCells(self, cell):
        sCells = 0
        if cell.getLeft() is not None:
            if cell.getLeft().v == 1:
                sCells += 1
        if cell.getRight() is not None:
            if cell.getRight().v == 1: 
                sCells += 1
        if cell.getTop() is not None:
            if cell.getTop().v == 1:
                sCells += 1
        if cell.getBot() is not None:
            if cell.getBot().v == 1:
                sCells += 1
        return sCells
                

    def draw(self):
        maze = []
        for row in self.maze:
            line = []
            for cell in row:
                line.append(cell.v)
            maze.append(line)

        fig, ax = plt.subplots()
        ax.pcolormesh(maze)
        ax.set_title('Maze')
        plt.xticks([])
        plt.yticks([])
        plt.show()
    