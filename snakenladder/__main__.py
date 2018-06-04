'''
Created on Jun 2, 2018

@author: agautam1
'''
from board import board, player
from time import sleep
import sys

players = []
iteration = 0

def initialize_players(num_players):
    for i in xrange(num_players):
        prompt = "Please enter the name of the player"+str(i)
        players.append(player(raw_input(prompt)))
        
def play(index, board):
    print "Player " + players[(index)].name + " playing..."
    sleep(3)
    if not players[index].is_active:
        ret = board.roll_die_to_activate()
        if ret == 1:
            players[index].position = 0
            players[index].is_active = True
            board.board_cells[players[index].position].player.add(players[index].name)
            
        if ret == 2:
            players[index].position = 0
            players[index].is_active = True
            offset = board.roll_die_to_move()
            if not (players[index].position + offset >= board.size):
                players[index].position += offset
                if board.board_cells[players[index].position].snake:    
                    players[index].position = board.board_cells[players[index].position].snake
                elif board.board_cells[players[index].position].ladder:
                    players[index].position = board.board_cells[players[index].position].ladder
                #set cell
                board.board_cells[players[index].position].player.add(players[index].name)
            else:
                print "chance cancelled as board crossed!"
                return players[index].position
    else:
        old_pos = players[index].position
        offset = board.roll_die_to_move()
        if not (players[index].position + offset >= board.size):
            players[index].position += offset
            if board.board_cells[players[index].position].snake:    
                players[index].position = board.board_cells[players[index].position].snake
            elif board.board_cells[players[index].position].ladder:
                players[index].position = board.board_cells[players[index].position].ladder
            #set cell
            board.board_cells[players[index].position].player.add(players[index].name)
            board.board_cells[old_pos].player.remove(players[index].name)
        else:
            print "chance cancelled as board crossed!"
            return players[index].position
        
        
    return players[index].position
        
def main():
    order = int(raw_input("Please enter the order of the board."))
    num_players = int(raw_input("Please enter number of players"))
    b = board(order)
    initialize_players(num_players)
    #b.print_board()
    #sys.exit(0)
    i = iteration
    while (True):
        b.print_board()
        position = play(i, b)
        if position == (pow(order,2) - 1):
            print players[i].name + " Wins! Game Over"
            break
        i = (i + 1) % len(players)
        
if __name__ == '__main__':
    main()