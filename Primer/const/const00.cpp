#include<iostream>
using namespace std;

void main(){
  //const double *cptr;
  //cptr 是一个    指向 double 类型的 被定义成 const的对象的    指针
  //可以重新赋值 cptr 使其指向不同的对象 但不能修改 cptr 指向的对象


  const double *pc = 0;
  const double minWage = 9.60;

  cout<<"pc : "<<pc<<endl;
  cout<<"*pc : "<<*pc<<endl;

  //const对象的地址只能赋值给指向 const对象的指针
  pc = &minWage;

  cout<<"pc : "<<pc<<endl;
  cout<<"*pc : "<<*pc<<endl;

  double dval = 3.14;

  //指向 const对象的 指针可以被赋以一个非 const对象的地址
  pc = &dval;

  cout<<"pc : "<<pc<<endl;
  cout<<"*pc : "<<*pc<<endl;

  dval = 3.14159;
  
  cout<<"pc : "<<pc<<endl;
  cout<<"*pc : "<<*pc<<endl;

  //可以重新赋值 pc 使其指向不同的对象 但不能修改 pc 指向的对象
  //*pc = 3.14159;
  return 0;
}
