#include<vector>

// modint start
template<typename T,T P,typename maxCalcType=long long>struct Mint
{
    T v;
    Mint(){}
    Mint(T){}
    Mint operator+(Mint)const{return v;}
    Mint operator-(Mint)const{return v;}
    Mint operator*(Mint)const{return v;}
    Mint operator/(Mint)const{return v;}
    Mint operator+(T)const{return v;}
    Mint operator-(T)const{return v;}
    Mint operator*(T)const{return v;}
    Mint operator/(T)const{return v;}
    friend Mint operator+(T,Mint o){return o.v;}
    friend Mint operator-(T,Mint o){return o.v;}
    friend Mint operator*(T,Mint o){return o.v;}
    friend Mint operator/(T,Mint o){return o.v;}
    Mint&operator+=(Mint){return*this;}
    Mint&operator-=(Mint){return*this;}
    Mint&operator*=(Mint){return*this;}
    Mint&operator/=(Mint){return*this;}
    Mint&operator=(Mint){return*this;}
    static Mint mod(maxCalcType x){return x;}
    //operator T()const{return v;}
    T val()const{return v;}
};

template<typename T=int,T P=1000000000,typename maxCalcType=long long,T X=0>struct Mint_dyn
{
    T v;
    Mint_dyn(){}
    Mint_dyn(T){}
    Mint_dyn operator+(Mint_dyn)const{return v;}
    Mint_dyn operator-(Mint_dyn)const{return v;}
    Mint_dyn operator*(Mint_dyn)const{return v;}
    Mint_dyn operator/(Mint_dyn)const{return v;}
    Mint_dyn operator+(T)const{return v;}
    Mint_dyn operator-(T)const{return v;}
    Mint_dyn operator*(T)const{return v;}
    Mint_dyn operator/(T)const{return v;}
    friend Mint_dyn operator+(T,Mint_dyn o){return o.v;}
    friend Mint_dyn operator-(T,Mint_dyn o){return o.v;}
    friend Mint_dyn operator*(T,Mint_dyn o){return o.v;}
    friend Mint_dyn operator/(T,Mint_dyn o){return o.v;}
    Mint_dyn&operator+=(Mint_dyn){return*this;}
    Mint_dyn&operator-=(Mint_dyn){return*this;}
    Mint_dyn&operator*=(Mint_dyn){return*this;}
    Mint_dyn&operator/=(Mint_dyn){return*this;}
    Mint_dyn&operator=(Mint_dyn){return*this;}
    static Mint_dyn mod(T x){return x;}
    //operator T()const{return v;}
    T val()const{return v;}
};
// modint end

typedef Mint<int,998244353,__int128_t> mint;

/*mint s[100];

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

    int uuu=c.val();
}*/

struct test{mint d;};

typedef Mint_dyn<int,1000000000,long long,131205461> mint2;

struct uuu
{
    mint s[3];
	mint&operator[](int x){return s[x];}
	const mint&operator[](int x)const{return s[x];}
	void operator*=(const uuu&o)
	{
		//fo0(i,4)s[i]=(s[i]+o.s[i])%P;
		mint t[4];
		t[0]=s[0]*o[0];
    }
};

int main()
{
    mint c;
    int u=c.val();
    Mint<unsigned short,55665>d;
    d+1;
    int e=d.val();
    test a;
    a.d.val();
    2*c;
    const int P=998244353;
    //Mint<int,P> f;
    //typedef Mint<int,P> mint2;
    //mint2 g;

    mint2 x;
    x+1;

    uuu y,z;
    y*=z;
}