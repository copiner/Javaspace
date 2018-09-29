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
  //r仅仅是一个名字，对它的操作相当于对a的操作，取地址即是取的a的地址
  //所以&符号是获取不到引用类型变量的地址的

  cout<<"x: "<<x<<endl;
  cout<<"&x: "<<&x<<endl;
  
  return 0;
}
