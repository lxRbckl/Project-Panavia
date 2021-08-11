# Project Panavia by Alex Arbuckle #


# Import <
import dash
from os import getcwd
from requests import get
from random import uniform
from json import load, dump
from ipinfo import getHandler

# >


# Declaration <
path = getcwd()
path = path.replace('Layout', '')

# >


def getGraph():
    '''  '''

    with open('{}/Panavia.json'.format(path), 'r') as fileVariable:


        return load(fileVariable)


def setGraph(arg):
    '''  '''

    with open('{}/Panavia.json'.format(path), 'w') as fileVariable:

        dump(arg, fileVariable, indent = 4)


def getStyle(arg):
    '''  '''

    with open('{}/Resource/{}.json'.format(path, arg), 'r') as fileVariable:

        return load(fileVariable)


def getCenter():
    '''  '''

    try:

        var = getHandler('7ec1c1bc96db16').getDetails(get('http://ip.42.pl/raw').text)
        return [float(i) + uniform(-0.0099999, 0.0099999) for i in var.loc.split(',')]

    except:

        return [39.0941493, -94.5812837]


# Run <
app = dash.Dash(suppress_callback_exceptions = True)
server = app.server

# >
