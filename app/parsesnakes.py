def parsesnakes(data):
	snakes = []

	for snake in data['snakes']['data']:
		x = [snake['body']['data'][i]['x'] for i in range(snake['length'])]
		y = [snake['body']['data'][i]['y'] for i in range(snake['length'])]

<<<<<<< HEAD
		if snake == data['you']:
			snakes.insert(0,list(zip(y,x)))
		else:
			snakes.append(list(zip(y,x)))

	return snakes
=======
	list(zip(y,x))
>>>>>>> 5f24b044f623fcb0d947859f6f581ef32467d0da
