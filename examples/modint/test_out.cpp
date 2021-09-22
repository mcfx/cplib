// Original Code:

// #include <cstdio>
// 
// #include "cplib/math/modint.hpp"
// 
// typedef Mint<int, 998244353> mint;
// 
// int P;
// #pragma cplib mint_mod P
// typedef Mint_dyn<> mint2;
// 
// int main() {
//   mint a, b;
//   scanf("%d%d", &a, &b);
//   printf("%d\n", a / 100);
//   printf("%d\n", a - b * b);
// 
//   mint2 c;
//   scanf("%d%d", &c, &P);
//   printf("%d\n", c / 100);
//   printf("%d\n", c * 4);
// }

unsigned int inv_general_32(unsigned int a,unsigned int P){unsigned int b=P-2,r=1;for(;b;b>>=1,a=(unsigned long long)a*a%P)if(b&1)r=(unsigned long long)r*a%P;return r;}
#include <cstdio>


typedef int mint;
int P;
typedef int mint2;
int main() {
   mint a, b;
   scanf("%d%d", &a, &b);
   printf("%d\n", (unsigned int)((((unsigned long long)(a)*(unsigned long long)(828542813)))%998244353));
   printf("%d\n", (unsigned int)(((unsigned long long)((signed long long)(a)-(signed long long)(((unsigned long long)(b)*(unsigned long long)(b))))+996491787298144256ull)%998244353));
   mint2 c;
   scanf("%d%d", &c, &P);
   printf("%d\n", (unsigned int)((((unsigned long long)(c)*(unsigned long long)(inv_general_32(100,P))))%P));
   printf("%d\n", (unsigned int)((((unsigned int)(c)*(unsigned int)(4)))%P));
}
