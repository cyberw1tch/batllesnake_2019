def parsesnakes(data):
    #gets coordinance of all snakes and differentiates from this snake
    snakes = []
    x = []
    y = []

    for snake in data['board']['snakes']:
        #x = [snake[j]['body'][i]['x'] for i in range(len(snake['body'])) for j in range(len(snake))]
        #y = [snake[j]['body'][i]['y'] for i in range(len(snake['body']))for j in range(len(snake))]

        for i in range(len(snake)):
            for j in range(len(snake[i]['body'])):
                x.append(snake[i]['body'][j]['x'])
                y.append(snake[i]['body'][j]['y'])
                    
        #if snake == data['you']:
    	    #snakes.insert(0,list(zip(y,x)))
        #else:
        snakes.append(list(zip(y,x)))
    
    print (snakes)
    return snakes
