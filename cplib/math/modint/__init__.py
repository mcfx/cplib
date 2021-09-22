import os, re, random
from Crypto.Util.number import isPrime

path = os.path.dirname(__file__)


def get_lara_code():
    s = open(os.path.join(path, 'modint.lara')).read()
    return [(s[:s.find('aspectdef main')], 'applyModint', 1000, -1)]  # must be first, since clava breaks template


def get_lara_cpp_code():
    return open(os.path.join(path, 'modint.hpp')).read()


def get_dummy_header_code():
    return open(os.path.join(path, 'modint.hpp')).read()


mint_dyn_re_1 = re.compile('^typedef Mint_dyn<(.+), *(.+)> *(.+);$')
mint_dyn_re_2 = re.compile('^typedef Mint_dyn<(.+)> *(.+);$')
mint_dyn_re_3 = re.compile('^typedef Mint_dyn<> *(.+);$')


def pragma_mint_mod(arg, line, code, storage):
    for t in mint_dyn_re_1.findall(line) + mint_dyn_re_2.findall(line) + mint_dyn_re_3.findall(line):
        if len(t) == 3:
            a, b, c = t
        elif len(t) == 2:
            a, c = t
            b = '1000000000'
        else:
            a = 'int'
            b = '1000000000'
            c = t
        b = int(b)
        while True:
            u = random.randint(b * 9 // 10, b * 11 // 10)
            if isPrime(u) and str(u) not in code:
                break
        storage[str(u)] = arg
        return 'typedef Mint_dyn<%s, %d, long long, %d> %s;' % (a, b, u, c)
    raise Exception('unknown mint_dyn arguments')


def pragma_callbacks():
    return {'mint_mod': (1, pragma_mint_mod)}


def post_process_priority():
    return 1


def post_process(code, storage):
    for dn, mod in storage.items():
        code = code.replace(dn, '0', 1).replace(dn, mod)
    return code
