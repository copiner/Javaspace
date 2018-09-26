#include<iostream>
using namespace std;

class A{
  friend class B;
private:
  int x = 10;
public:
  int y = 30;
};

class B{
public:
  void print(A a){
    cout<<a.x<<endl;
    cout<<a.y<<endl;
  }
};

int main(){
  A a;
  B b;
  b.print(a);
  return 0;
}
