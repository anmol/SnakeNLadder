'''
Created on Jun 2, 2018

@author: agautam1
'''
from random import randint, sample
from sets import Set
import math

class player:
    def __init__(self, name):
        self.position = None
        self.is_active = False
        self.name = name


class cell:
    def __init__(self):
        self.player = Set()
        self.snake = None
        self.ladder = None
        
    def is_empty(self):
        if self.player is None:
            return True
        return False
    
    def set_snake(self, tail):
        self.snake = tail
        
    def set_ladder(self, top):
        self.ladder = top
        

class board:
    def __init__(self, order):
        #num_snake + num_ladders <
        self.order = order
        self.size = pow(order,2)
        self.board_cells = []
        for i in xrange(self.size):
            self.board_cells.append(cell())
        self.set_snakes_and_ladders()
            
    #assuming 10 snakes and 10 ladders in a 10x10 board
    def set_snakes_and_ladders(self):
        event_list = sample(xrange(1, self.size-2), 4 * self.order)
        event_list.sort()
        #print event_list
        for i in xrange(1, (2 * self.order) + 1):
            if i%2 == 0:
                ladder_base = event_list.pop(0)
                ladder_head = event_list.pop()
                self.board_cells[ladder_base].set_ladder(ladder_head)
            else:
                snake_head = event_list.pop()
                snake_tail = event_list.pop(0)
                self.board_cells[snake_head].set_snake(snake_tail)
                
    def roll_die_to_activate(self):
        print "player inactive, rolling the die to get lucky."
        face = randint(1,6)
        print "die outputs : ", face
        
        if face not in (1,6):
            return 0
        elif face == 1:
            return 1
        else:
            return 2
        
    def print_board(self):
        for i in xrange(self.size):
            index = i 
            if self.board_cells[i].snake:
                #transform = "\xF0\x9F\x94\xB4"
                transform = str(self.board_cells[i].snake)
            elif self.board_cells[i].ladder:
                #transform = "\xF0\x9F\x94\xB5"
                transform = str(self.board_cells[i].ladder)
            else:
                transform = ""
            print "[ " + str(index).ljust(3) + " " + str([x for x in self.board_cells[i].player]).ljust(5) + " " + transform.ljust(3) + " ]",
            if i%self.order == (self.order - 1):
                print '\n'
        
    def roll_die_to_move(self):
        face = randint(1,6)
        print "die outputs : ", face
        if face == 6:
            print "Hurray! We hit the maximum: 6 , will run more..."
            face = face + self.roll_die_to_move()
        return face
    
if __name__ == '__main__':
    b = board(6)
    print b.roll_die_to_move()
            
            

        
            
    
            
        
            
        
        
        