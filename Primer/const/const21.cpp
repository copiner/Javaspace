#include<iostream>

using namespace std;

int main(){
  const double pi = 3.1415;
  const double *const pi_ptr = &pi;

  cout<<"pi_ptr: "<<pi_ptr<<endl;
  cout<<"*pi_ptr: "<<*pi_ptr<<endl;

  const double cpi = 3.0;
  //  pi_str = &cpi;//error
  //  *pi_ptr = 2.0;//error

  return 0;
}
