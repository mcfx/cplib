#include <cstdio>

#include "cplib/math/modint.hpp"

typedef Mint<int, 998244353> mint;

int P;
#pragma cplib mint_mod P
typedef Mint_dyn<> mint2;

int main() {
  mint a, b;
  scanf("%d%d", &a, &b);
  printf("%d\n", a / 100);
  printf("%d\n", a - b * b);

  mint2 c;
  scanf("%d%d", &c, &P);
  printf("%d\n", c / 100);
  printf("%d\n", c * 4);
}