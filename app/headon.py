def detect_headon(direction, board, start, snakes):

    #set the snake head to 0, we're not worried about colliding with it
    board[start[0],start[1]] = 0
    
    #offset start based on which direction we're heading 
    if direction == 'right':
        start[1] += 1
    if direction == 'left':
        start[1] -= 1
    if direction == 'up':
        start[0] -= 1
    if direction == 'down':
        start[0] += 1

if (
        board[start[0]+1,start[1]] == 1 or
        board[start[0]-1,start[1]] == 1 or
        board[start[0],start[1]+1] == 1 or
        board[start[0],start[1]-1] == 1 ):

    #potential head-on detected
