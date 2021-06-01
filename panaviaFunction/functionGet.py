from json import load


def getJSON(arg):
    '''  '''

    with open('panaviaSetting/{}'.format(arg), 'r') as fileVariable:

        return load(fileVariable)
