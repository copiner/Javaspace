#include<iostream>
using namespace std;

void swap(int,int);
int main(){
  int i = 10;
  int j = 20;
  cout<<"Before swap: "<< i <<"--"<<j<<endl;
  swap(i,j);
  cout<<"After swap: "<< i <<"--"<<j<<endl;
  return 0;
}
void swap(int v1,int v2){
  int temp = v2;
  v2 = v1;
  v1 = temp;
}
  
