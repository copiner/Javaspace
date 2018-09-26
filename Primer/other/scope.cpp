#include<iostream>
//using namespace std;

//namespace scope

int main(){
  std::cout<<"scope :"<<std::endl;
  return 0;
}
//class scope

class Oil{
public:
  int test();
  
}
int Oil::test(){
  return 1;
}

//global scope

int a;

void test(){
  int a = ::a;
}
