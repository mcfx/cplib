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
        lc, la, opt = lib.get_lara_code()
        if lc:
            lara_code.append(lc)
            lara_aspects.append((opt, la))
    lara_aspects.sort()
    lara_calls = '\n'.join(map(lambda x: '    call %s();' % x[1], lara_aspects))
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


def post_process(code, used_libs, libs_storage):
    s = []
    for libname in used_libs:
        lib = libs[libname]
        p = lib.post_process_priority()
        if p is not None:
            s.append((p, lib, libname))
    s.sort()
    for _, lib, libname in s:
        code = lib.post_process(code, libs_storage[libname])
    return code


def pre_pragma_use(code, used_libs, libs_storage):
    def get_dummy_cpp_code(libname):
        if libname in used_libs:
            return ''
        used_libs.add(libname)
        libs_storage[libname] = {}
        lib = libs[libname]
        for name, funcx in lib.pragma_callbacks().items():
            pragma_callbacks[name] = (libname,) + funcx
        return lib.get_dummy_cpp_code()
    lines = code.split('\n')
    res_lines = []
    pragma_callbacks = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith('#pragma cplib use '):
            libname = line[18:]
            res_lines.append(get_dummy_cpp_code(libname))
        elif line.startswith('#include"cplib/'):
            libname = line.strip()[15:-5].replace('/', '.')
            res_lines.append(get_dummy_cpp_code(libname))
        elif line.startswith('#include "cplib/'):
            libname = line.strip()[16:-5].replace('/', '.')
            res_lines.append(get_dummy_cpp_code(libname))
        elif line.startswith('#pragma cplib '):
            pos = line.find(' ', 14)
            if pos == -1:
                pos = len(line)
            tp = line[14:pos]
            if tp in pragma_callbacks:
                libname, ptype, func = pragma_callbacks[tp]
                if ptype == 1:
                    nline = func(line[pos + 1:], lines[i + 1], code, libs_storage[libname])
                    res_lines.append(nline)
                    i += 1
                else:
                    raise Exception('unknown pragma callback type')
            else:
                raise Exception('unknown pragma')
        else:
            res_lines.append(line)
        i += 1
    res_code = '\n'.join(res_lines)
    return res_code


if __name__ == '__main__':
    code = open('../include/test.cpp').read().replace('\r', '\n')
    prefix_comments = '// Original Code:\n\n' + '\n'.join(map(lambda x: '// ' + x.replace('\t', ' ' * 4), code.split('\n'))) + '\n' * 2
    used_libs = set()
    libs_storage = {}
    code = pre_pragma_use(code, used_libs, libs_storage)
    code = clava_work(code, used_libs)
    code = post_process(code, used_libs, libs_storage)
    # print(code)
    code = prefix_comments + code
    open('../include/test_out.cpp', 'w').write(code)
