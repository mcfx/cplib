#include<bits/stdc++.h>

#pragma cplib use cp.modint

const int N=2505,P=998244353;
typedef Mint<int,998244353> mint;

struct data
{
	mint s[4];
	mint&operator[](int x){return s[x];}
	const mint&operator[](int x)const{return s[x];}
	void reset(){for(int i=0;i<4;i++)s[i]=0;}
	void operator+=(const data&o)
	{
		for(int i=0;i<4;i++)s[i]+=o[i];
	}
	void operator*=(const data&o)
	{
		//fo0(i,4)s[i]=(s[i]+o.s[i])%P;
		mint t[4];
		t[0]=s[0]*o[0];
		t[1]=s[0]*o[1]+s[1]*o[0];
		t[2]=s[0]*o[2]+mint(2)*s[1]*o[1]+s[2]*o[0];
		t[3]=s[0]*o[3]+s[1]*o[2]*3+s[2]*o[1]*3+s[3]*o[0];
		for(int i=0;i<4;i++)s[i]=t[i];
	}
	data add1()const
	{
		data t;
		t[0]=s[0];
		t[1]=s[0]+s[1];
		t[2]=s[0]+s[1]*2+s[2];
		t[3]=s[0]+s[1]*3+s[2]*3+s[3];
		return t;
	}
}f[N][N];

std::vector<int>p[N];
int n,r,b,m,st[N],dep[N],fa[N];

bool chk(int x,int y){return x<=r&&y<=b;}

int main()
{
    scanf("%d%d%d",&n,&r,&b);
	int sc=0;
	for(int i=1;i<=n*2;i++)
	{
		char t[5];
        scanf("%s",t);
		if(t[1]=='u')
		{
			fa[++m]=st[sc];
			dep[m]=dep[st[sc]]+1;
			p[st[sc]].push_back(m);
			st[++sc]=m;
		}
		else
		{
			--sc;
		}
	}
	//fo1(i,n)out,fa[i],' ';out,'\n';
	for(int i=0;i<=n;i++)for(int j=0;j<=n;j++)f[i][j][0]=1;
	for(int i=n;i;i--)
	{
		for(int j=0;j<=dep[i];j++)if(!chk(dep[i]-j,j))f[i][j].reset();
		//dbg,'/',i;
		//fo(j,0,dep[i])dbg,'@',f[i][j][0],f[i][j][1],f[i][j][2],f[i][j][3];
		for(int j=0;j<dep[i];j++)
		{
			f[i][j]+=f[i][j+1].add1();
		}
		for(int j=0;j<dep[i];j++)f[fa[i]][j]*=f[i][j];
	}
	data ans=f[0][0];
	//fo0(i,4)out,ans[i],' ';out,'\n';
	// (n-b)*b*b
	mint ta=(P-1)*ans[3]+n*ans[2];
	printf("%d\n",ta.val());
}