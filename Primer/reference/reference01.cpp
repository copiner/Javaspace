#include<iostream>

using namespace std;

int main(){
  int ival = 1024;
  int &refVal = ival;
  
  int *pi = &ival;

  cout<<"&refVal: "<<&refVal<<endl;
  cout<<"refVal: "<<refVal<<endl;
  
  int *&ptrVal = pi;
  
  cout<<"ptrVal: "<<ptrVal<<endl;

  cout<<"&ptrVal "<<&ptrVal<<endl;
  cout<<"*&ptrVal: "<<*&ptrVal<<endl;

  return 0;
}
