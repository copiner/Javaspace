#include<iostream>

using namespace std;

int main(){
  double dval = 3.14159;

  const int &ir = 1024;


  const int &ir2 = dval;
  //equal
  //  int temp = dval;
  //  const int &ir2 = temp;
  
  const double &dr = dval + 1.0;
  
}
