from json import dump


def setJSON(arg):
    '''  '''

    with open('panaviaSettings/{}'.format(arg), 'w') as fileVariable:

        dump(fileVariable, arg, indent = 4)
