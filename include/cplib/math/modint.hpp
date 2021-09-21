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
    static Mint mod(maxCalcType x){return Mint((x%P+P)%P);}
    //operator T()const{return v;}
    T val()const{return v;}
};