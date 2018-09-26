#include<iostream>
#include "string.h"
using namespace std;

class Student{
  friend void display(Student);
public:
  Student(int a, int b):age(a),height(b){
    cout<<a<<" "<<b<<endl;
  }
private:
  int height;
  int age;
};

void display(Student s){
  cout<<"height: "<<s.height<<endl;
  cout<<"age: "<<s.age<<endl;
};

int main(){
  Student stu(5,175);
  display(stu);
  return 0;
}
