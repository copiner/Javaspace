#include <iostream>

int main()
{
  int int1 = 5;
  int &rInt = int1;
  
  std::cout<<"&int1: " << &int1 << " int1: "<<int1<<std::endl;
  std::cout<<"&rInt: " << &rInt << " rInt: "<<rInt<<std::endl;

  int int2 = 8;
  rInt = int2;

  std::cout<<"&rInt: " << &rInt << " rInt: "<<rInt<<std::endl;
}
