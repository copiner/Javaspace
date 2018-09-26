#include<iostream>
#include<cstring>  
using namespace std;

int main(){
  const char *st = "The expense of spirit\n";
  int len = 0;

  const char *p = st;
  //  cout<<st<<endl;
  //  cout<<*st<<endl;

  while(*p++){
    ++len;
    cout<<len<<" : "<<*st;
    st++;
  }
  return 0;
}
