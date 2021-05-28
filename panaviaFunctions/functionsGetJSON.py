from json import load


def getJSON(arg):
    '''  '''

    with open('panaviaSettings/{}'.format(arg), 'r') as fileVariable:


        return load(fileVariable)
