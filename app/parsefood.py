def parsefood(data):
	foods = []

	for food in data['food']['data']:
		
		x = food['x']
		y = food['y']
		
		foods.append((y,x))

	return foods
