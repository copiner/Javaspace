#include<iostream>
using namespace std;

int main(){
  //指向 const对象的 const指针
  const double pi = 3.14159;
  const double *const pi_ptr = &pi;
  //pi_ptr 是指向被定义为 const的 double 类型对象的  const指针

  cout<<"pi_ptr: "<<pi_ptr<<endl;
  cout<<"*pi_ptr: "<<*pi_ptr<<endl;

  //pi_ptr 指向的对象的值以及它的地址本身都不能被修改
  const double cpi = 3.0;
  //pi_ptr = &cpi;

  //*pi_ptr = 2.0;
  return 0;
}
