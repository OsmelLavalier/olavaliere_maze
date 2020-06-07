
#created by Osmel E. Lavalier M. 

import random
import os
import sys

class Cell:
    def __init__(self, y=0, x=0):
        self.x = x
        self.y = y
        self.display = '*'

class Maze:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.matrix = list()
        self.stack = list()
        self.visited = list()
        self.initialize()

    def initialize(self):
        for y in range(self.h):
            self.matrix.append([])
            for x in range(self.w):
                self.matrix[y].append(Cell(y, x))

    def in_field(self, y, x):
        if x < 1 or x > self.w-2:
            return False
        if y < 1 or y > self.h-2:
            return False
        return True

    def is_visited(self, y, x):
        return (y, x) in self.visited

    def unvisited_neighbours(self, node):
        neighbours = list()

        dd = ((2, 0), (-2, 0), (0, 2), (0, -2))

        for (yy, xx) in dd:
            dy = node.y + yy
            dx = node.x + xx
            
            if self.in_field(dy, dx):
                if not self.is_visited(dy, dx):
                    neighbours.append(self.matrix[dy][dx])
        if len(neighbours) == 0:
            return [] 

        return neighbours

    def traverse(self, start_cell):

        self.matrix[start_cell.y][start_cell.x].display = ' '
        self.visited.append((start_cell.y, start_cell.x))
        self.stack.append(start_cell)

        while len(self.stack) > 0:
            current_cell = self.stack.pop()
            self.move(current_cell, self.stack)

                
    def move(self, cell, s):
        flag = True 

        while flag:
            adjacent_cells = self.unvisited_neighbours(cell)

            if len(adjacent_cells) == 0:
                flag = False 
                continue

            neighbour =  adjacent_cells[random.randint(0, len(adjacent_cells)-1)]

            if (neighbour.y < cell.y and neighbour.x == cell.x): #up
                self.matrix[cell.y-1][cell.x].display = ' '
                self.matrix[neighbour.y][neighbour.x].display = ' '

                self.visited.append((neighbour.y, neighbour.x))
                s.append(neighbour)

                cell = neighbour

            if (neighbour.y > cell.y and neighbour.x == cell.x): #down
                self.matrix[cell.y+1][cell.x].display = ' '
                self.matrix[neighbour.y][neighbour.x].display = ' '
                
                self.visited.append((neighbour.y, neighbour.x))
                s.append(neighbour)

                cell = neighbour
                
            if (neighbour.x < cell.x and neighbour.y == cell.y): #left
                self.matrix[cell.y][cell.x-1].display = ' '
                self.matrix[neighbour.y][neighbour.x].display = ' '

                self.visited.append((neighbour.y, neighbour.x))
                s.append(neighbour)

                cell = neighbour
                
            if (neighbour.x > cell.x and neighbour.y == cell.y): #right
                self.matrix[cell.y][cell.x+1].display = ' '
                self.matrix[neighbour.y][neighbour.x].display = ' '

                self.visited.append((neighbour.y, neighbour.x))
                s.append(neighbour)

                cell = neighbour

    def print_maze(self):
        for y in range(self.h):
            for x in range(self.w):
                print(self.matrix[y][x].display, end=' ')
            print()
    
def choose_starting_position():
    start_y, start_x = int(sys.argv[1]), int(sys.argv[2])
     
    if (start_y % 2 == 0 or start_x % 2 == 0):
        print('Coordinates cannot be composite integers.')
        return False
    
    return start_y, start_x

def main():
    if choose_starting_position():
        y,x = choose_starting_position() 
    
        m = Maze(21, 21)
        m.traverse(Cell(y, x))
        m.print_maze()

if __name__ == '__main__':
    main()

