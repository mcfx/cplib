unsigned int inv_998244353(unsigned int a){unsigned int b=998244353u-2,r=1;for(;b;b>>=1,a=(unsigned long long)a*a%998244353u)if(b&1)r=(unsigned long long)r*a%998244353u;return r;}
#include <vector>
int Mint_start;
template<typename T,T P,typename U=T>struct Mint{};template<signed int P,typename U>struct Mint<signed int,P,U>{signed int v;Mint(){}Mint(signed int x):v(x){}operator signed int()const{return v;}};template<unsigned int P,typename U>struct Mint<unsigned int,P,U>{unsigned int v;Mint(){}Mint(unsigned int x):v(x){}operator unsigned int()const{return v;}};template<signed long long P,typename U>struct Mint<signed long long,P,U>{signed long long v;Mint(){}Mint(signed long long x):v(x){}operator signed long long()const{return v;}};template<unsigned long long P,typename U>struct Mint<unsigned long long,P,U>{unsigned long long v;Mint(){}Mint(unsigned long long x):v(x){}operator unsigned long long()const{return v;}};
int Mint_end;
typedef Mint<int, 998244353, __int128_t> mint;
mint s[100];
mint work(mint x) {
   
   return ((((unsigned int)(x)+(unsigned int)(1)))%998244353);
}

mint const & work2(mint & x) {
   
   return x;
}


struct test {
   mint u;
};

int main() {
   mint lst;
   mint X, Y, Z;
   for(int i = 1; i < 100; i++)
      lst=(s[i]=(((((unsigned long long)(((unsigned long long)(s[i - 1])*(unsigned long long)(50)))+(unsigned long long)(((unsigned long long)(i)*(unsigned long long)(i)))))%998244353)));
   mint a = 100, b = 100;
   mint c = ((((unsigned long long)(((unsigned long long)(((((__uint128_t)(((__uint128_t)(((unsigned long long)(a)*(unsigned long long)(a)))*(__uint128_t)(a)))*(__uint128_t)(a)))%998244353))*(unsigned long long)(a)))+(unsigned long long)(((unsigned long long)(b)*(unsigned long long)(b)))))%998244353);
   c=(((((unsigned long long)(c)+(unsigned long long)(((unsigned long long)(a)*(unsigned long long)(b)))))%998244353));
   c=(((((unsigned long long)(c)*(unsigned long long)(inv_998244353(b))))%998244353));
   *(s + 10);
   work(2);
   test d;
   ((((unsigned int)(d.u)+(unsigned int)(2u)))%998244353);
   Mint<long long, 5> e;
   ((((unsigned char)(e)+(unsigned char)(1ll)))%5);
   ((((unsigned int)(work2(c))*(unsigned int)(2)))%998244353);
   c=(((((unsigned int)(c=(((((unsigned int)(c)+(unsigned int)(2)))%998244353)))+(unsigned int)(3)))%998244353));
   c=(((((unsigned int)(c)+(unsigned int)((111))))%998244353));
   std::vector<mint> s;
   ((((unsigned int)(s.back())+(unsigned int)(c)))%998244353);
   (((unsigned long long)((signed long long)(((unsigned long long)(c)*(unsigned long long)(c)))-(signed long long)(((unsigned long long)(a)*(unsigned long long)(a))))+996491787298144256ull)%998244353);
   (((unsigned int)((signed int)(((unsigned int)(((unsigned int)(c)+(unsigned int)(c)))+(unsigned int)(c)))-(signed int)(a))+998244353u)%998244353);
}
