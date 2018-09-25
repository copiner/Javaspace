//STL (standard template library) vector string ...
#include<iostream>
#include<vector>
using namespace std;

int main(){
  vector<int> a(10,0);

  cin>>a[2];
  cin>>a[5];
  cin>>a[6];

  for(int i=0; i<a.size();i++){
    cout<<a[i]<<endl;
  }
  return 0;
}
