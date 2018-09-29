#include<iostream>

using namespace std;

int main(){
  int errNumb = 0;
  int myErrNumb = 1;

  int *const curErr = &errNumb;

  cout<<"curErr: "<<curErr<<endl;
  cout<<"*curErr: "<<*curErr<<endl;

  *curErr = 2;//right

  cout<<"curErr: "<<curErr<<endl;
  cout<<"*curErr: "<<*curErr<<endl;

  //  curErr = &myErrNumb;//error
  return 0;
}
