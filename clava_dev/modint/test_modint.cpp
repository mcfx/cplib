#include<vector>

int Mint_start;
template<typename T,T P,typename maxCalcType=long long>struct Mint
{
    T v;
    Mint(T=0){}
    Mint operator+(Mint)const{return v;}
    Mint operator-(Mint)const{return v;}
    Mint operator*(Mint)const{return v;}
    Mint operator/(Mint)const{return v;}
    Mint operator+(T)const{return v;}
    Mint operator-(T)const{return v;}
    Mint operator*(T)const{return v;}
    Mint operator/(T)const{return v;}
    Mint&operator+=(Mint){return*this;}
    Mint&operator-=(Mint){return*this;}
    Mint&operator*=(Mint){return*this;}
    Mint&operator/=(Mint){return*this;}
    Mint&operator=(Mint){return*this;}
    static Mint mod(maxCalcType x){return Mint((x%P+P)%P);}
    operator T()const{return v;}
};
int Mint_end;

typedef Mint<int,998244353,__int128_t> mint;

mint s[100];

mint work(mint x){
    return x+1;
}

const mint&work2(mint&x){
    return x;
}

struct test
{
    mint u;
};

int main()
{
    mint lst;
    mint X,Y,Z;
    for(int i=1;i<100;i++)
        lst=s[i]=s[i-1]*50+mint(i)*i;
    mint a=100,b=100;
    mint c=a*a*a*a*a+b*b;
    c+=a*b;
    c/=b;
    *(s+10);
    work(2);
    test d;
    d.u+mint::mod(998244355);
    Mint<long long,5>e;
    e+1ll;
    work2(c)*2;
    (c+=2)+=3;
    c+=(111);

    std::vector<mint>s;
    s.back()+c;

    c*c-a*a;
    c+c+c-a;
}