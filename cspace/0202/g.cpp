#include <iostream>

using namespace std;

int main(){

  char p;
  cout << " input text: \n";

  while( cin.peek() != '\n' ){
    //p = cin.get();
    //cout << p;
    cout << ( p = cin.get() );
  }

  cout << endl;

  return 0;
}
