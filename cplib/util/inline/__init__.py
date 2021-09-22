import os

path = os.path.dirname(__file__)


def get_lara_code():
    s = open(os.path.join(path, 'inliner.lara')).read()
    return [(s[:s.find('aspectdef main')], 'inlineFunctions', 0, 990)]
