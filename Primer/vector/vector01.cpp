#include<iostream>
#include<vector>
using namespace std;

int main(){
  vector< vector<int> > b(6,vector<int>(5,1));

  cin>>b[1][1];
  cin>>b[2][2];
  cin>>b[3][3];
  
  for(int i=0;i<b.size();i++){
    for(int j=0;j<b[i].size();j++){
      cout<<b[i][j]<<" ";
    }
    cout<<"\n";
  }
}
