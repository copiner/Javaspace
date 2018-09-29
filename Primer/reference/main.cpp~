//Type &name <--> Type *const name
#include<iostream>

using namespace std;

int main(){
  int a = 9;
  int b = 8;

  int *const pc = &a;
  
  int *pa = &a;

  int &ra = a;

  cout<<"&ra: "<<&ra<<endl;
  cout<<"ra: "<<ra<<endl;
  cout<<"pc: "<<pc<<endl;
  cout<<"*pc: "<<*pc<<endl;
  cout<<"*pa: "<<*pa<<endl;
  *pa = b;

  cout<<"&ra: "<<&ra<<endl;
  cout<<"ra: "<<ra<<endl;
  cout<<"pc: "<<pc<<endl;
  cout<<"*pc: "<<*pc<<endl;
  cout<<"*pa: "<<*pa<<endl;

  return 0;
}
