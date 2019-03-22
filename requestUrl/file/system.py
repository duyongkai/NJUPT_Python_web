import sys

def import_modules(dir = r'E:\Users\dyk\Source\Libs\Python', file = '__init__.py'):
    try:
        if not dir in sys.path:
            sys.path.append(dir)
        if not file in sys.modules:
            module = __import__(file)
        else:
            eval('import ' + file)
            module = eval('reload(' + file + ')')
        return module
    except:
        return ModuleNotFoundError

def saveFinish_cmd():
    print('<successful!>')
    input('press any key to continue...')
