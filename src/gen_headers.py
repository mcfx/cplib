import os, shutil
from lib import libs

SRC_ROOT = os.path.dirname(os.path.abspath(__file__))
HEADER_ROOT = os.path.join(os.path.dirname(SRC_ROOT), 'include/cplib')
if os.path.exists(HEADER_ROOT):
    shutil.rmtree(HEADER_ROOT)

for libname, lib in libs.items():
    fn = HEADER_ROOT + '/' + libname.replace('.', '/') + '.hpp'
    os.makedirs(os.path.dirname(fn), exist_ok=True)
    code = lib.get_dummy_header_code()
    open(fn, 'w').write(code)
