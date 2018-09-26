#include<iostream>
#include<string>
using namespace std;

class Person{
public:
  void display(){//inline default
    cout<<"name: "<<name<<endl;
  }
  string name;
};
int main(){
  Person P;
  P.name = "Luna";
  P.display();
  return 0;
}
