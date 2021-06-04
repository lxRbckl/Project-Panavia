from requests import get
from random import uniform
from ipinfo import getHandler
from panaviaFunction.functionGetJSON import getJSON


def getLocation():
    '''  '''

    setting = getJSON('settingStyle.json')
    var = getHandler(setting['getLocation']['ipinfoKey'])
    var = var.getDetails(get('http://ip.42.pl/raw').text).loc.split(',')

    return [float(i) + uniform(-0.0099999, 0.0099999) for i in var]
