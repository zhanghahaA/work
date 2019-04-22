#include <iostream>
#include <string.h>
using namespace std;
class XS{
public:
	virtual void dispXM()=0;
	virtual void dispXB()=0;
	virtual void dispNL()=0;
};
class CZS:public XS{
public:
	CZS(char * m="张三",int b=1,int n=14);
	void dispXM();
	void dispXB();
	void dispNL();
protected:
	char xm[9];
	int xb,nl;
};
CZS::CZS(char *m,int b,int n)
{
strcpy(xm,m);
xb=b,nl=n;
}
void CZS::dispXM()
{
	cout<<"name:"<<xm<<endl;
}
void CZS::dispXB()
{	
	if(xb==1)
	cout<<"Man"<<endl;
	if(xb==0)
		cout<<"Woman"<<endl;
	
}
void CZS::dispNL()
{
	cout<<"age:"<<nl<<endl;
}
class GZS:public XS{
public:
	GZS(char * m="张三",int b=1,int n=17);
	void dispXM();
	void dispXB();
	void dispNL();
protected:
	char xm[9];
	int xb,nl;
};
GZS::GZS(char *m,int b,int n)
{
strcpy(xm,m);
xb=b,nl=n;
}
void GZS::dispXM()
{
	cout<<"name:"<<xm<<endl;
}
void GZS::dispXB()
{
	if(xb==1)
	cout<<"Man"<<endl;
	if(xb==0)
		cout<<"Woman"<<endl;
}
void GZS::dispNL()
{
	cout<<"age:"<<nl<<endl;
}
class DXS:public XS{
public:
	DXS(char * m="张三",int b=1,int n=20);
	void dispXM();
	void dispXB();
	void dispNL();
protected:
	char xm[9];
	int xb,nl;
};
DXS::DXS(char *m,int b,int n)
{
strcpy(xm,m);
xb=b,nl=n;
}
void DXS::dispXM()
{
	cout<<"name:"<<xm<<endl;
}
void DXS::dispXB()
{
		if(xb==1)
	cout<<"Man"<<endl;
	if(xb==0)
		cout<<"Woman"<<endl;
}
void DXS::dispNL()
{
	cout<<"age:"<<nl<<endl;
}
void displayP(XS *p)
{
     p->dispXM();
	 p->dispXB();
	 p->dispNL();
}
void displayR( XS &p)
{
	   p.dispXM();
	 p.dispXB();
	 p.dispNL();
}
void main()
{
	CZS czs("赵一",1,12);
	GZS gzs("钱二",0,15);
	DXS dxs("孙三",1,18);
	XS *p;//定义抽象基类的指针变量p
	p=&czs;//将初中生对象czs的地址赋给p
  displayP(p);
	p=&gzs;//将高中生对象czs的地址赋给p
  displayP(p);
	p=&dxs;//将大学生对象czs的地址赋给p
  displayP(p);
	cout<<"\n----------------------------------------\n";
	XS &r1=czs;//定义抽象基类的引用变量r1为czs的别名
	displayR(r1);
	XS &r2=gzs;//定义抽象基类的引用变量r2为czs的别名
	displayR(r2);
	XS &r3=dxs;//定义抽象基类的引用变量r3为czs的别名
	displayR(r3);
	cout<<"\n----------------------------------------\n";
}