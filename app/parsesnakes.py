def parsesnakes(data):
        #gets coordinance of all snakes and differentiates from this snake
	snakes = []

	for snake in data['board']['snakes']:
		x = [snake[i]['body']['x'] for i in range(len(snake['body']))]
		y = [snake[i]['body']['y'] for i in range(len(snake['body']))]

		if snake == data['you']:
			snakes.insert(0,list(zip(y,x)))
		else:
			snakes.append(list(zip(y,x)))

	return snakes
