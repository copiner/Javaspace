#include <iostream>

int main()
{
  enum weekdays{Monday, Tuesday, Wednesday,Thursday, Friday};

  weekdays today;

  today = Monday;
  std::cout<<today<<"\n";

  today = Thursday;

  std::cout << today <<"\n";

  return 0;
}
