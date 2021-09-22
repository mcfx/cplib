#include <cstdio>

#pragma cplib use util.inline

int a;

#pragma cplib inline
void test1() { a++; }

#pragma cplib inline
int test2(int x) { return ++a + x; }

int main() {
  test1();
  int x, a;
  scanf("%d", &x);
  printf("%d\n", test2(x));
  if (test2(x))
    printf("%d\n", test2(x + 1));
}