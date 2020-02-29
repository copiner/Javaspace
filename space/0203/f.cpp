#include <iostream>

int main()
{
  char answer;

  std::cout << "peek![Y/N]"<<"\n";
  std::cin >> answer;

  switch(answer){
  case 'Y':
  case 'y':
    std::cout << "confused: "<<"\n";
    break;
  case 'N':
  case 'n':
    std::cout<< "excellent"<<"\n";
    break;
  default:
    std::cout<<"something wrong"<<"\n";
    break;
  }
  
  std::cin.ignore(100,'\n');
  std::cout<<"input: bulk\n"<<std::endl;
  std::cin.get();
  return 0;
}
