def parsesnakes(data):
	snakes = []

	for snake in data['snakes']['data']:
		x = [snake['body']['data'][i]['x'] for i in range(snake['length'])]
		y = [snake['body']['data'][i]['y'] for i in range(snake['length'])]

		if snake == data['you']:
			snakes.insert(0,list(zip(y,x)))
		else:
			snakes.append(list(zip(y,x)))

	return snakes