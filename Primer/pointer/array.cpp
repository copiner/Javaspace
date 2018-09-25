#include<iostream>
using namespace std;

int main(){
  int ia[10];
  int *iter = &ia[0];
  int *iter_end = &ia[10];

  while(iter != iter_end){
    do_something_with_value(*iter);
    ++iter;
  }
}
