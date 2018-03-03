import numpy as np


def main():

    sneks = [[(0,0),(0,1)][(9,3),(9,4)]]

    tonumpy(sneks,10,10)

def tonumpy (enemies ,width, height):
    
    code_board = np.zeros((height,width), dtype=int)
    print(code_board)

if __name__=="__main__":
    main()
