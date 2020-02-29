#include <fstream>
#include <iostream>

using namespace std;

int main(){
  
  ifstream in;
  //ifstream in("text");
  in.open("text");
  if(!in){
    cerr << "open file fail" << endl;
  }

  char x;
  while(in >> x){

    cout << x;
    
  }

  cout << endl;
  in.close();

  return 0;
}
