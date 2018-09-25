#include<iostream>
#include<string>

using namespace std;

int main(){
  string str("fa.disney.com");
  int size = str.size();

  for(int i = 0; i<size;++i){
    if(str[i] == '.'){
      str[i] = '_';
    }
  }

  cout<<"str: "<<str<<endl;

  replace(str.begin(),str.end(),'_','.');

  cout<<"str: "<<str<<endl;
		      
  return 0;
}
