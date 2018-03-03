import numpy as np


def main():

    tonumpy(10,10)

def tonumpy ( width, height):
    
    code_board = np.zeros((height,width), dtype=int)
    print(code_board)

if __name__=="__main__":
    main()
