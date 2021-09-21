import os, shutil, subprocess
import config
from util import randstr
from lib import libs

SRC_ROOT = os.path.dirname(os.path.abspath(__file__))
LIB_ROOT = os.path.join(os.path.dirname(SRC_ROOT), 'cplib')


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
        lc, la = lib.get_lara_code()
        if lc:
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


def get_dummy_cpp_code(libname, used_libs):
    if libname in used_libs:
        return ''
    used_libs.add(libname)
    lib = libs[libname]
    return lib.get_dummy_cpp_code()


def pre_pragma_use(code, used_libs):
    lines = code.split('\n')
    res_lines = []
    for line in lines:
        if line.startswith('#pragma cplib use '):
            libname = line[18:]
            res_lines.append(get_dummy_cpp_code(libname, used_libs))
        elif line.startswith('#include"cplib/'):
            libname = line.strip()[15:-1].replace('/', '.')
            res_lines.append(get_dummy_cpp_code(libname, used_libs))
        elif line.startswith('#include "cplib/'):
            libname = line.strip()[16:-1].replace('/', '.')
            res_lines.append(get_dummy_cpp_code(libname, used_libs))
        else:
            res_lines.append(line)
    res_code = '\n'.join(res_lines)
    return res_code


if __name__ == '__main__':
    code = open('test.cpp').read().replace('\r', '\n')
    prefix_comments = '// Original Code:\n\n' + '\n'.join(map(lambda x: '// ' + x, code.split('\n'))) + '\n' * 2
    used_libs = set()
    code = pre_pragma_use(code, used_libs)
    code = clava_work(code, used_libs)
    # print(code)
    code = prefix_comments + code
    open('test_out.cpp', 'w').write(code)
