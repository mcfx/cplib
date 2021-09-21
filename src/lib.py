import os, importlib
from util import randstr

SRC_ROOT = os.path.dirname(os.path.abspath(__file__))
LIB_ROOT = os.path.join(os.path.dirname(SRC_ROOT), 'cplib')


def fix_call(mod, func_name, res):
    if func_name not in dir(mod):
        mod.__dict__[func_name] = lambda: res
    func = mod.__dict__[func_name]

    def foo(*args, **kwargs):
        rt = func(*args, **kwargs)
        if type(res) is tuple:
            return rt + res[len(rt):]
        return rt
    mod.__dict__[func_name] = foo


def import_file(fn):
    spec = importlib.util.spec_from_file_location('lib_' + randstr(), fn)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    fix_call(mod, 'get_dummy_cpp_code', '')
    fix_call(mod, 'get_lara_code', ('', '', 0))
    fix_call(mod, 'post_process_priority', None)
    return mod


def dfs_lib(cur):
    if cur != '' and os.path.isfile(LIB_ROOT + cur + '/__init__.py'):
        libs[cur[1:].replace('/', '.')] = import_file(LIB_ROOT + cur + '/__init__.py')
    for x in os.listdir(LIB_ROOT + cur):
        if os.path.isdir(LIB_ROOT + cur + '/' + x):
            dfs_lib(cur + '/' + x)


libs = {}
dfs_lib('')
