#include <iostream>

int main()
{
  int Arr[5] = {1,4,5,7,9};
  int *aP = Arr;
  
  std::cout<<"*aP : "<<*aP<<"\n";

  std::cout<<"*aP + 1 : " << *aP + 1<<"\n";

  std::cout<<"*(aP + 1) : "<<*(aP + 1)<<"\n";

  return 0;
}
