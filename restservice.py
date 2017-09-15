#!/usr/bin/env python2
#encoding: UTF-8

# Encoding por defecto
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Configuración local
from datetime import *
import locale
locale.setlocale(locale.LC_ALL, '')

# Librerías
import re
import logging
import pymongo
from time import time
from bottle import route, run
from json import dumps
from bson.objectid import ObjectId
from bson.json_util import dumps

def format_json(resultado):
    pretty = dumps(resultado, sort_keys=False, indent=4, separators=(',', ': '))
    pretty = re.sub('[\r\n]', '<br>', pretty)
    pretty = re.sub('\s{4}', '&nbsp;&nbsp;&nbsp;&nbsp;', pretty)
    return pretty

@route('/helloworld')
def index():
    init_time = time()
    resultado = {
        'date': init_time,
        'message': 'Hello, World!'
    }
    return format_json(resultado)
