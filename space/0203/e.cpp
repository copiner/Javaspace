#include <fstream>
#include <iostream>

using namespace std;

int main(){

  ifstream in("text");
  if(!in){
    cerr << "open file fail r" << endl;
  }

  ofstream out("test",ios::app);
  if(!out){
    cerr << "open file fail w" << endl;
  }

  char x;

  while(in >> x){
    out << x;
  }

  out.close();
  in.close();

  return 0;

}
