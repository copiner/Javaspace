#include<iostream>
using namespace std;

void pswap(int *,int *);
int main(){
  int i = 10;
  int j = 20;
  cout<<"Before swap: "<< i <<"--"<<j<<endl;
  pswap( &i,&j );
  cout<<"After swap: "<< i <<"--"<<j<<endl;
  return 0;
}
void pswap(int *v1,int *v2){
  int tmp = *v2;
  *v2 = *v1;
  *v1 = tmp;
}
  
