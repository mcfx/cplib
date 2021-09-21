import os


def randstr(n=20):
    return os.urandom((n + 2) // 2).hex()[:n]
