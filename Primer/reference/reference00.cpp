#include<iostream>
using namespace std;

void main(){
  //引用类型由类型标识符和一个取地址操作符来定义 引用必须被初始
  int ival = 1024;
  int &refVal = ival;

  //指向指针的引用
  int *&ptrVal = &ival;

  cout<<"&refVal: "<<&refVal<<endl;

  cout<<"&ptrVal "<<&ptrVal<<endl;
  cout<<"*&ptrVal: "<<*&ptrVal<<endl;
}
