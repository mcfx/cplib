import os, shutil, argparse, subprocess
import config
from util import randstr
from lib import libs

SRC_ROOT = os.path.dirname(os.path.abspath(__file__))
LIB_ROOT = os.path.join(os.path.dirname(SRC_ROOT), 'cplib')


def clava_pass(code, lara_aspects):
    path = '/tmp/cplib_' + randstr()
    os.mkdir(path)
    os.chdir(path)
    shutil.copyfile(SRC_ROOT + '/assets/clava.config', path + '/clava.config')
    open(path + '/code.cpp', 'w').write(code)
    lara_calls = '\n'.join(map(lambda x: '    call %s();' % x[0], lara_aspects))
    print('clava_pass:', *(x[0] for x in lara_aspects))
    lara_code = [x[1] for x in lara_aspects]
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


def clava_work(code, used_libs):
    lara_aspects = {}
    for libname in used_libs:
        lib = libs[libname]
        for aspect in lib.get_lara_code():
            lc = aspect[0]
            la = aspect[1]
            prio = aspect[2] if len(aspect) > 2 else 0
            _pass = aspect[3] if len(aspect) > 3 else 0
            if _pass not in lara_aspects:
                lara_aspects[_pass] = []
            lara_aspects[_pass].append((prio, la, lc))
    for _pass in sorted(lara_aspects.keys()):
        code = clava_pass(code, [(x[1], x[2]) for x in sorted(lara_aspects[_pass])])
    return code


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
    def get_lara_cpp_code(libname):
        if libname in used_libs:
            return ''
        used_libs.add(libname)
        libs_storage[libname] = {}
        lib = libs[libname]
        for name, funcx in lib.pragma_callbacks().items():
            pragma_callbacks[name] = (libname,) + funcx
        return lib.get_lara_cpp_code()
    lines = code.split('\n')
    res_lines = []
    pragma_callbacks = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith('#pragma cplib use '):
            for libname in line[18:].split():
                res_lines.append(get_lara_cpp_code(libname))
        elif line.startswith('#include"cplib/'):
            libname = line.strip()[15:-5].replace('/', '.')
            res_lines.append(get_lara_cpp_code(libname))
        elif line.startswith('#include "cplib/'):
            libname = line.strip()[16:-5].replace('/', '.')
            res_lines.append(get_lara_cpp_code(libname))
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
                res_lines.append(line)
                #raise Exception('unknown pragma')
        else:
            res_lines.append(line)
        i += 1
    res_code = '\n'.join(res_lines)
    return res_code


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CPLib Compiler')
    parser.add_argument('source_file', help='Source file')
    parser.add_argument('-o', dest='output_file', help='Output file')
    args = parser.parse_args()
    code = open(args.source_file).read().replace('\r', '\n')
    prefix_comments = '// Original Code:\n\n' + '\n'.join(map(lambda x: '// ' + x.replace('\t', ' ' * 4), code.split('\n'))) + '\n' * 2
    used_libs = set()
    libs_storage = {}
    code = pre_pragma_use(code, used_libs, libs_storage)
    code = clava_work(code, used_libs)
    code = post_process(code, used_libs, libs_storage)
    # print(code)
    code = prefix_comments + code
    open(args.output_file, 'w').write(code)
