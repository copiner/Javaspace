//gdb  objdump  
#include<iostream>

using namespace std;

int main(){
  int a = 6;
  int &r = a;
  int *p = &a;
  int x = r;

  cout<<"&a: "<<&a<<endl;
  cout<<"p: "<<p<<endl;
  cout<<"&r: "<<&r<<endl;
  //r������һ�����֣������Ĳ����൱�ڶ�a�Ĳ�����ȡ��ַ����ȡ��a�ĵ�ַ
  //����&�����ǻ�ȡ�����������ͱ����ĵ�ַ��

  cout<<"x: "<<x<<endl;
  cout<<"&x: "<<&x<<endl;
  
  return 0;
}
