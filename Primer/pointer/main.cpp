#include<iostream>
#include<cmath>
using namespace std;

int main(){
  int ival = 256, ival2 = 512;
  int *pi = &ival;

  int **ppi = &pi;

  //  int *pi2 = *ppi;

  cout<<"The value of ival\n"
      <<"direct value: " <<ival<<"\n"
      <<"indirect value: "<<*pi<<"\n"
      <<"doubly indirect value: "<<**ppi<<endl;

    cout<<"&ival: "<<&ival<<endl;
    cout<<"pi:"<<pi<<endl;
    cout<<"&pi: "<<&pi<<endl;
			cout<<"ppi: "<<ppi<<endl;
			cout<<"*ppi : "<<*ppi<<endl;

  return 0;
  
}
