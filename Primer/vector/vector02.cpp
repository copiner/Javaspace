#include <iostream>
#include<vector>
using namespace std;

int main(){
  const int elem_size = 10;
  vector<int> ivec(elem_size);

  int ia[elem_size];
  
  print_vector(ivec);
  cout<<" "<<endl;
  print_array(ia);
  return 0;
  
}

void print_vector(vector<int> ivec){
  if(ivec.empty()){
    return;
  }

  for(int ix=0;ix<ivec.size();++ix){
    cout<<ivec[ix]<<' ';
  }
}

void print_array(ia){
  int len = sizeof(ia)/sizeof(ia[0]);
  for(int i=0;i<len;++i){
    ia[i] = i;
  }
  for(int j=0;j<len;++j){
    cout<<ia[j]<<' ';
  }
}
