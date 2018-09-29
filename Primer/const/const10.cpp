#include<iostream>
using namespace std;

void main(){
  //定义一个 const指针    指向一个 const或一个非 const对象
  int errNumb = 0;
  int myErrNumb = 1;
  int *const curErr = &errNumb;
  //curErr是一个       指向 int 类型对象的    const指针
  //不能赋给  curErr其他的地址值   但可以修改 curErr指向的值
   *curErr = 2;

  //试图给 const指针赋值会在编译时刻被标记为错误
  //curErr = &myErrNumb;

  cout<<"curErr: "<<curErr<<endl;
  cout<<"*curErr: "<<*curErr<<endl;

}
