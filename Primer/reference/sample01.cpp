#include<iostream>

using namespace std;

class Huge{
public:
  double stuff[1000];
};
extern int calc(const Huge &);

int main(){
  Huge table[1000];

  int sum = 0;

  for(int ix=0;ix<1000;++ix){
    sum += calc(table[ix]);
  }
  return 0;
}
