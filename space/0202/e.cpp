#include <iostream>

using namespace std;

int main(){

  int sum = 0;

  cout << "intergate blankspace any: " << endl;

  int i;

  while( cin >> i){

    sum += i;
    while( cin.peek() == ' '){
      cin.get();
    }
    if(cin.peek() == '\n'){
      break;
    }
  }

  cout << "result: " << sum << endl;

  return 0;
  
}
