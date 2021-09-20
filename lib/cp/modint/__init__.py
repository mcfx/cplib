import os

path = os.path.dirname(__file__)


def get_lara_code():
    s = open(os.path.join(path, 'modint.lara')).read()
    return s[:s.find('aspectdef main')], 'applyModint'


def get_pseudo_cpp_code():
    return open(os.path.join(path, 'modint.hpp')).read()
