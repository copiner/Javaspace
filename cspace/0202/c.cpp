#include <iostream> //in out stream   C92 C99

using namespace std;

int addArray( int *array, int n );

int main(){

  int data[] = {9,8,7,6,5,4,3,2,1,0};
  int size = sizeof(data) / sizeof(data[0]);

  //cout (console out)-- basic_ostream -- ostream  -- iostream
  //std::cout ÃüÃû¿Õ¼ä
  //<<ÖØÔØ
  cout << "result: " << addArray(data, size) << endl;

  return 0;
}

int addArray( int *array, int n ){
  int sum = 0;
  int i;

  for( i=0; i<n; i++){
    sum += *array++;
  }

  return sum;
}
