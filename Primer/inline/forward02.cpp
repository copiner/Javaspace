#include<iostream>
using namespace std;

inline int max(int a,int b){
  return a>b?a:b;
};

int main(){

  int k = max(4,8);
  cout<<k<<endl;
  return 0;
}
