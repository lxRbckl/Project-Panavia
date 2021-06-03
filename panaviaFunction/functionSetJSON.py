from json import dump


def setJSON(arg):
    '''  '''

    with open('panaviaSetting/settingFigure.json', 'w') as fileVariable:

        dump(arg, fileVariable, indent = 4)
