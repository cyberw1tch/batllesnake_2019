def parsesnakes(data):
	snakes = []

	for snake in data['snakes']:
		x = [snake['body']['data'][i]['x'] for i in snake['length']
		y = [snake['body']['data'][i]['y'] for i in snake['length']

	list(zip(y,x))
