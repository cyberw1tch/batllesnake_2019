def parsefood(data):
    #get food coordinance from server
	foods = []

	for food in data['board']['food']:
		
		x = food['x']
		y = food['y']
		
		foods.append((y,x))

	return foods
