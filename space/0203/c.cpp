#include <fstream>
#include <iostream>

using namespace std;

int main(){
  
  ofstream out;
  //ofstream out("text",ios::app);
  out.open("text",ios::app);
  if(!out){
    cerr << "open file fail" << endl;
    return 0;
  }

  for(int i=0; i<10; i++){

    out << i;
    
  }

  out << endl;
  out.close();

  return 0;
}
