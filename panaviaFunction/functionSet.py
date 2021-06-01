from json import dump


def setJSON(arg):
    '''  '''

    with open('panaviaSetting/{}'.format(arg), 'w') as fileVariable:

        dump(fileVariable, arg, indent = 4)
