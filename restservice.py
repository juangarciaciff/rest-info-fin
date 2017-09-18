from sys import argv
import bottle
from bottle import route, run

bottle.debug(True)

@route('/')
def index():
    return "<h1>Hola Mundo2!!!</h1>"

if __name__ == '__main__':
    #run(host='0.0.0.0', port=argv[1])
    run(host='0.0.0.0', port='80')
