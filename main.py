import os
import bottle

ROOT = os.path.join(os.environ.get('HTML_PATH', '.'))
AUTH = os.environ.get('BASIC_AUTH', ':').split(':', 1)
PORT = int(os.environ.get('PORT', '8080'))

app = bottle.Bottle()


def check(username, password):
    return [username, password] == AUTH


@app.route('<path:path>')
@bottle.auth_basic(check)
def server_static(path):
    if path.endswith('/'):
        path += 'index.html'
    return bottle.static_file(path, root=ROOT)


if __name__ == '__main__':
    bottle.run(app, host='0.0.0.0', port=PORT)
