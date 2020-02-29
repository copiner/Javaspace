
#include <iostream>

class Student
{
  static int number = 0;
  std::string name;

public:
  void set(std::string str)
  {
    name = str;
    ++number;
  }

  static int printNumber()
  {
    std::cout<<number<<" total numbers\n";
  }

  void print()
  {
    std::cout<<name<<" students are "<<number<<" numbers\n";
  }
};

int Student::number = 0;

void fn()
{
  Student s1;
  s1.set("Jenny");
  
  Student s2;
  s2.set("Randy");

  s1.print();
}

int main()
{
  Student s;
  s.set("Smith");
  //fn();
  {
    Student s1;
    s1.set("Jenny");
  
    Student s2;
    s2.set("Randy");

    s1.print();
  }
  Student::printNumber();
  s.print();

  return 0;
}
