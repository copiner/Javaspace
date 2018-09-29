#include<iostream>
#include<vector>
using namespace std;

int main(){
  vector<int> a(10,1);
  
  vector<int>::iterator t;

  for(t = a.begin(); t != a.end(); t++){
    cout <<*t<<" ";
  }
  cout <<endl;
  
  for(vector<int>::iterator it = a.begin(); it!= a.end(); ++it){
    cout<<*it<<' ';
  }
  return 0;
}
