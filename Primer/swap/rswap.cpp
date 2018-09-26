#include<iostream>
using namespace std;

void rswap(int &,int &);
int main(){
  int i = 10;
  int j = 20;

  int &ri = i, &rj = j;
  cout<<"Before swap: "<< i <<"--"<<j<<endl;
  rswap(i,j);
  cout<<"After swap: "<< i <<"--"<<j<<endl;
  return 0;
}
void rswap(int &v1,int &v2){
  int tmp = v2;
  v2 = v1;
  v1 = tmp;
}
  
