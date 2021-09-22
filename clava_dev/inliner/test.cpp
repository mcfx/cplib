

int foo(){return 10;}

int a=2;
namespace test1
{
    int b=5;
#pragma cplib inline
int test(int x,int y)
{
    int sum=y;
    for(int i=0;i<x;i++)sum+=i;
    return sum+a+b;
}
}

namespace test2x
{
    #pragma cplib inline
    long long test2(bool u)
    {
        return u?test1::test(10,u):foo();
    }
}

namespace test3x
{
    using namespace test2x;
    using namespace test1;
    namespace uuu {
    #pragma cplib inline
    long long test3(bool u)
    {
        if (u)return test2(false);
        return 114514^test(100,200);
    }
    }
}

int o;

#pragma cplib inline
void test4(int x)
{
    o=x;
    return;
}

#pragma cplib inline
int test5(int x,int y)
{
    return x+y;
}

int main()
{
    int a=1;
    int b=test1::test(1,55);
    int c=1+test1::test(b,a)+1;

    int d=test2x::test2(true);
    int e=test3x::uuu::test3(false);

    test4(5);
    int val = test1::test(2,33);
    if(1)if(test1::test(2,33)){

    }

    test5(test5(1,test5(2,3)),4);

    return test1::test(10,1);
}

/*#pragma cplib inline
int test(int x){return x;}

int main()
{
    if(1)if(test(10)){2;}else{1;}
    test(test(10));
}*/