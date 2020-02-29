#include <iostream>
#include <string>

int main()
{
  std::string str;
  std::cout<<"input any string: ";
  
  std::getline(std::cin, str);

  std::cout << str<<"\n";
  return 0;
}
