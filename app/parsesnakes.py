def parsesnakes(data):
        #gets coordinance of all snakes and differentiates from this snake
	snakes = []

	for snake in data['board']['snakes']:
		x = [snake[j]['body'][i]['x'] for i in range(len(snake['body'])) for j in range(len(snake))]
		y = [snake[j]['body'][i]['y'] for i in range(len(snake['body']))for j in range(len(snake))]

		if snake == data['you']:
			snakes.insert(0,list(zip(y,x)))
		else:
			snakes.append(list(zip(y,x)))

	return snakes
