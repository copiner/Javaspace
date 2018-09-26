#include<iostream>
#include<cstring>

using namespace std;

int main(){
  const char *st = "The expense of spirit\n";
  int len = 0;

  const char *p = st;

  while(*p++){
    len++;
    cout<<len<<": "<<st<<endl;
    st++;
  }
  return 0;
}
