#include<iostream>
using namespace std;

class CA{
public:
  int ca_var;
  int add(int a,int b);
  int add(int a);
  CA(int c);
};

CA::CA(int c){
  ca_var = c;
};

int CA::add(int a,int b){
  return a+b;
}

int CA::add(int a){
  return a + ::ca_var;
}

int main(){
  int m,n;
  CA ca(8);
  m = ca.add(2,3);
  n = ca.add(6);
  cout<<"m: "<<m<<"n: "<<n<<endl;
  return 0;
}

