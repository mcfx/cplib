import os, shutil, importlib, subprocess
import config

SRC_ROOT = os.path.dirname(os.path.abspath(__file__))
LIB_ROOT = os.path.join(os.path.dirname(SRC_ROOT), 'lib')


def randstr(n=20):
    return os.urandom((n + 2) // 2).hex()[:n]


def import_file(fn):
    spec = importlib.util.spec_from_file_location('lib_' + randstr(), fn)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def dfs_lib(cur):
    if cur != '' and os.path.isfile(LIB_ROOT + cur + '/__init__.py'):
        libs[cur[1:].replace('/', '.')] = import_file(LIB_ROOT + cur + '/__init__.py')
    for x in os.listdir(LIB_ROOT + cur):
        if os.path.isdir(LIB_ROOT + cur + '/' + x):
            dfs_lib(cur + '/' + x)


libs = {}
dfs_lib('')


def clava_work(code, used_libs):
    path = '/tmp/cplib_' + randstr()
    os.mkdir(path)
    os.chdir(path)
    shutil.copyfile(SRC_ROOT + '/assets/clava.config', path + '/clava.config')
    open(path + '/code.cpp', 'w').write(code)

    lara_code = []
    lara_aspects = []
    for libname in used_libs:
        lib = libs[libname]
        if 'get_lara_code' in dir(lib):
            lc, la = lib.get_lara_code()
            lara_code.append(lc)
            lara_aspects.append(la)
    lara_calls = '\n'.join(map(lambda x: '    call %s();' % x, lara_aspects))
    lara_code.append('''aspectdef main
%s
end
''' % lara_calls)
    lara_code = '\n\n'.join(lara_code)
    open(path + '/main.lara', 'w').write(lara_code)
    subprocess.run([config.JAVA11_PATH, '-jar', config.CLAVA_PATH, '-c', path + '/clava.config'])
    res = open(path + '/woven/code.cpp').read()
    os.chdir(SRC_ROOT)
    shutil.rmtree(path)
    return res


def get_pseudo_cpp_code(libname, used_libs):
    if libname in used_libs:
        return ''
    used_libs.add(libname)
    lib = libs[libname]
    if 'get_pseudo_cpp_code' in dir(lib):
        return lib.get_pseudo_cpp_code()
    return ''


def pre_pragma_use(code, used_libs):
    lines = code.split('\n')
    res_lines = []
    for line in lines:
        if line.startswith('#pragma cplib use '):
            libname = line[18:]
            res_lines.append(get_pseudo_cpp_code(libname, used_libs))
        else:
            res_lines.append(line)
    res_code = '\n'.join(res_lines)
    return res_code


if __name__ == '__main__':
    code = open('test.cpp').read().replace('\r', '\n')
    used_libs = set()
    code = pre_pragma_use(code, used_libs)
    code = clava_work(code, used_libs)
    # print(code)
    open('test_out.cpp', 'w').write(code)
