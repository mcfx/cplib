# CPLib

CPLib is the abbreviation of Competitive Programming Library. It aims to be a general template and optimization library for competitive programming.

The idea is similar to [cLay](http://rsujskf.s602.xrea.com/files/clay.html), but I hope it to be easier to maintain, having less hard-coded rules, and C++ compatible. Also, I want to implement some optimizations, such as loop-blocking/unrolling, auto SIMD, etc. on the source code level.

## Templates proposal
General templates are not implemented yet. I want to implement in cLay like formats (see https://codeforces.com/contest/1556/submission/127359517 for example).

I hope the templates can use global arrays (for example, the array in segment tree) instead of struct members. Also, I want to use global functions as callback functions (for example, the maintain function in segment tree). If we use `std::function` or function pointers, the running speed depends on how smart is the compiler.

To pass these arguments into the templates, I think pragmas is a good idea (see the modint part below for more information).

## Implemented packages
Currently there are very few implemented packages.

### math.modint
This package implements a typical modint template. It allows common operations, but it's more efficient.

It traversals each expression, computes the possible min/max of them, and finds a method which has mininum number of modulo.

See [examples/modint/](examples/modint/) for examples.

### util.inline
This package can inline functions on source code level. Add `#pragma cplib inline` in front of your function, every call will be inline.

See [examples/inline/](examples/inline/) for examples.

### util.minimize
This package tries to minimize the code. However, it only detects repeating segments, and replace them using macro definitions.

## Usage
Download Clava at [https://github.com/specs-feup/clava](https://github.com/specs-feup/clava), and fill the path into `src/config.py`.

Install python packages from `src/requirements.txt`.

Then you can run `python src/compile.py input.cpp -o output.cpp` to "compile" files.

You need to add `include` to your IDE's include paths to make IDE happy.

To include a package, use `#include "cplib/xxx/xxx.hpp"` or `#pragma cplib use xxx.xxx`.

## Others
If you have some ideas about the template proposals, or the project, please open issues.

This project is very immature, and needs a lot of time to develop, welcome for your contribute.

Clava runs very slow (~5s on my computer for a regular source code), if there is better replacement, please tell me!