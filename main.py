import os
import bottle

ROOT = os.path.join(os.environ.get('HTML_PATH', '.'))
AUTH = os.environ.get('BASIC_AUTH', None)
PORT = int(os.environ.get('PORT', '8080'))


def check(username, password):
    return ':'.join([username, password]) == AUTH


def server_static(path):
    if path.endswith('/'):
        path += 'index.html'
    return bottle.static_file(path, root=ROOT)

if AUTH is not None:
    server_static = bottle.auth_basic(check)(server_static)

server_static = bottle.route('<path:path>')(server_static)

if __name__ == '__main__':
    bottle.run(host='0.0.0.0', port=PORT)
