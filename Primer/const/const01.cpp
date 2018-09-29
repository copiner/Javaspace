#include<iostream>

using namespace std;

int main(){

  const double *pc = 0;
  const double minWage = 9.60;

  pc = &minWage;
  cout<<"*pc: "<<*pc<<endl;

  double dval = 3.14;

  pc = &dval;
  cout<<"*pc: "<<*pc<<endl;

  //  *pc = 3.1415; //error
  cout<<"*pc: "<<*pc<<endl;
  return 0;
			  
}
