from requests import get
from ipinfo import getHandler
from panaviaFunction.functionGetJSON import getJSON


def getLocation():
    '''  '''

    setting = getJSON('settingStyle.json')
    var = getHandler(setting['getLocation']['ipinfoKey'])
    var = var.getDetails(get('http://ip.42.pl/raw').text)

    return var.loc.split(',')
