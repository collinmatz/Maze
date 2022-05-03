import matplotlib.pyplot as plt
import random

class Maze():

    class Cell():
        def __init__(self):
            self.k = False
            self.v = 0

    def __init__(self, width, height):
        self.w = width
        self.h = height
        maze = []
        # initialize maze
        for _ in range(self.h):
            line = []
            for _ in range(self.w):
                line.append(self.Cell())
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
            if wall[0] - 1 != -1:
                if [wall[0]-1, wall[1]] not in walls:
                    walls.append([wall[0]-1, wall[1]])
            if wall[0] + 1 != self.w - 1:
                if [wall[0]+1, wall[1]] not in walls:
                    walls.append([wall[0]+1, wall[1]])
            if wall[1] - 1 != - 1:
                if [wall[0], wall[1]-1] not in walls:
                    walls.append([wall[0], wall[1]-1])
            if wall[1] + 1 != self.h - 1:
                if [wall[0], wall[1]+1] not in walls:
                    walls.append([wall[0], wall[1]+1])
            walls.remove(wall)
                
        





    def draw(self):
        fig, ax = plt.subplots()
        ax.pcolormesh(self.maze)
        ax.set_title('Maze')
        plt.xticks([])
        plt.yticks([])
        plt.show()
    