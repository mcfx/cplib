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