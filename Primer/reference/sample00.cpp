#include<iostream>
#include<vector>

using namespace std;

int main(){
  
}

vector<int>::const_iterator look_up(const vector<int> &vec, int value, int &occurs){
  vector<int>::const_iterator res_iter = vec.end();
  occurs = 0;
  for(vector<int>::const_iterator iter = vec.begin();iter != vec.end(); ++iter){
    if(*iter == value){
      if(res_iter == vec.end())
	res_iter = iter;
      ++occurs;
    }
  }
  return res_iter;
}
