#include <iostream>

using namespace std;

int main(){

  const int SIZE = 50;
  char buf[SIZE];

  cout << "in text: ";
  cin.read( buf, 20 );

  cout << "char num: " << cin.gcount() <<endl;

  cout << "in detail: ";
  cout.write( buf, 20 );
  cout << endl;

  return 0;
}
