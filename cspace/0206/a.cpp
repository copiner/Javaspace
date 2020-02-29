/*
  data type
*/

#include <iostream>

int main()
{
  const unsigned short ITEM = 10;
  int num[ITEM];
  
  std::cout << "input ITEM int num!\n";

  for(int i = 0; i < ITEM; i++){
    std::cout<<"input the " << i+1 << "num: ";
    while( !(std::cin >> num[i]) ){

      std::cin.clear();
      std::cin.ignore(100,'\n');
      std::cout<<"input error";

    }
    
  }

  int total = 0;
  for(int j=0;j<ITEM;j++){
    total += num[j];
  }

  std::cout << "The total: "<<total<<"\n";
  std::cout << "The averal: "<<(float)total/ITEM;
  std::cout << "\n"<<std::endl;
  return 0;
}
