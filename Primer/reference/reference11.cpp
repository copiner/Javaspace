#include<iostream>

using namespace std;

int main(){
  int ival = 1024;
  int &refVal = ival;

  int min_val = 0;
  
  cout<<"&refVal: "<<&refVal<<endl;
  cout<<"refVal: "<<refVal<<endl;
  //refVal = min_val;
  refVal += 2;

  int ii = refVal;

  int *pi = &refVal;

  cout<<"&refVal: "<<&refVal<<endl;
  cout<<"refVal: "<<refVal<<endl;

  cout<<"ii: "<<ii<<endl;

  cout<<"pi: "<<pi<<endl;
  cout<<"*pi: "<<*pi<<endl;
}
