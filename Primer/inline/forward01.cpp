#include<iostream>
#include<string>
using namespace std;

class Person{
public:
  void display();
  inline void show();

  string name;
  int height;
};

void Person::display(){
  cout<<"name: "<<name<<endl;
};

inline void Person::show(){
  cout<<"height: "<<height<<endl;
};



int main(){
  Person P;
  P.name = "Luna";
  P.height = 180;
  P.display();
  P.show();
  return 0;
}
