#include <iostream>

int main()
{
  const unsigned short ITEMS = 5;
  
  int intArray[ITEMS] = {2,4,6,8,1};
  char charArray[ITEMS] = {'K','a','s','j','c'};

  int *intPtr = intArray;
  char *charPtr = charArray;

  std::cout << "int array out: "<<"\n";
  for(int i=0; i<ITEMS;i++){

    std::cout<<*intPtr<<" at "
	     <<reinterpret_cast<unsigned long>(intPtr)<<"\n";
    intPtr++;//+4byte

  }

  std::cout << "char array out: "<<"\n";
  for(int i=0; i<ITEMS;i++){

    std::cout<<*charPtr<<" at "
	     <<reinterpret_cast<unsigned long>(charPtr)<<"\n";
    charPtr++;//+1byte

  }
  
  return 0;
}
