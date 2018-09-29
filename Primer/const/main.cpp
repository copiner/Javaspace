#include<iostream>

using namespace std;

int main(){  
  const int bufSize = 512;

  //int *ptr = &bufSize; //error

  const int *ptr = &bufSize;//right

  return 0;
}
