import os, importlib
from util import randstr

SRC_ROOT = os.path.dirname(os.path.abspath(__file__))
LIB_ROOT = os.path.join(os.path.dirname(SRC_ROOT), 'cplib')


def import_file(fn):
    spec = importlib.util.spec_from_file_location('lib_' + randstr(), fn)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if 'get_dummy_cpp_code' not in dir(mod):
        mod.get_dummy_cpp_code = lambda: ''
    if 'get_lara_code' not in dir(mod):
        mod.get_lara_code = lambda: '', ''
    return mod


def dfs_lib(cur):
    if cur != '' and os.path.isfile(LIB_ROOT + cur + '/__init__.py'):
        libs[cur[1:].replace('/', '.')] = import_file(LIB_ROOT + cur + '/__init__.py')
    for x in os.listdir(LIB_ROOT + cur):
        if os.path.isdir(LIB_ROOT + cur + '/' + x):
            dfs_lib(cur + '/' + x)


libs = {}
dfs_lib('')
