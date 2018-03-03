import bottle
import os
import random
import snakechoice

@bottle.route('/')
def static():
    return "the server is running"


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data.get('game_id')
    board_width = data.get('width')
    board_height = data.get('height')

    head_url = ''

    #head_url = 'https://i.pinimg.com/736x/d6/11/d4/d611d43cc3146764a204787ee96fed5a.jpg' % (
    #    bottle.request.urlparts.scheme,
    #    bottle.request.urlparts.netloc
    #)

    # TODO: Do things with data

    return {
        'color': '#CACFFF',
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_url': head_url,
        'name': 'Mariah Scarey',
        'head_type': 'tongue',
        'tail_type': 'fat-rattle'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json
    snakes = parsesnakes(data)
    omnom = parsefood(data)
    board,goal,head = tonumpy(snakes,omnom, board_width, board_height)
    direction = astar(board,head,goal)

    # up, down, left, right
    directions = ['up', 'down', 'left', 'right']
    direction = random.choice(directions)
    return {
        'move': direction,
        'taunt': 'All I want for Christmas is your life'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug = True)
