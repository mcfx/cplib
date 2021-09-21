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
