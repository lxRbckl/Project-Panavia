from json import dump


def setJSON(arg):
    '''  '''

    with open('panaviaSetting/settingFigure.json', 'w') as fileVariable:

        dump(fileVariable, arg, indent = 4)
