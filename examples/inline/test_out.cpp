// Original Code:

// #include <cstdio>
// 
// #pragma cplib use util.inline
// 
// int a;
// 
// #pragma cplib inline
// void test1() { a++; }
// 
// #pragma cplib inline
// int test2(int x) { return ++a + x; }
// 
// int main() {
//   test1();
//   int x, a;
//   scanf("%d", &x);
//   printf("%d\n", test2(x));
//   if (test2(x))
//     printf("%d\n", test2(x + 1));
// }

#include <cstdio>
int a;


void test1() {
   a++;
}



int test2(int x) {
   
   return ++a + x;
}

int main() {
   {do{using ::a; {
      a++;
   }
   }while(0);}
   ;
   int x, a;
   scanf("%d", &x);
   int _CPLTMP_R17_18_;{int _CPLTMP_A0_17_18=x;do{int x=_CPLTMP_A0_17_18;using ::a; {
      {_CPLTMP_R17_18_=++a + x;break;}
   }
   }while(0);}
   printf("%d\n", _CPLTMP_R17_18_);
   int _CPLTMP_R18_7_;{int _CPLTMP_A0_18_7=x;do{int x=_CPLTMP_A0_18_7;using ::a; {
      {_CPLTMP_R18_7_=++a + x;break;}
   }
   }while(0);}
   if(_CPLTMP_R18_7_) { int _CPLTMP_R19_20_;{int _CPLTMP_A0_19_20=x + 1;do{int x=_CPLTMP_A0_19_20;using ::a; {    {_CPLTMP_R19_20_=++a + x;break;} } }while(0);} printf("%d\n", _CPLTMP_R19_20_); }
}
