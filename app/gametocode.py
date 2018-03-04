import numpy as np
import time
import astar

#def main():

    #t1 = time.time()

    #sneks = [[(17,17),(17,18)],[(9,3),(9,4)]]
    #snack = [(5,4),(3,3)]

    #board,goal,head = tonumpy(sneks,snack,20,20)
    #direction = astar.astar(board, head,goal)
    #print (direction)
    #t2 = time.time()
    #print(t2-t1)

def tonumpy (enemies ,food, width, height):

    code_board = np.zeros((height,width), dtype=int)
    #print(code_board)

    for block in enemies:
        if block is not enemies[0]:
            code_board[block[0][0]+1][block[0][1]] = 1
            code_board[block[0][0]][block[0][1]+1] = 1
            code_board[block[0][0]-1][block[0][1]] = 1
            code_board[block[0][0]][block[0][1]-1] = 1
        for coord in block[:-1]:
            code_board[coord[0]][coord[1]] = 1

    print(code_board,food[0],enemies[0][0])
    return code_board,food[0],enemies[0][0]
    #print(code_board)

#if __name__=="__main__":
    #main()
