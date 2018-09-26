#include<iostream>

class Base{
public:
  static int func1();
  int func2();
private:
  static const int _i;
};
const int Base::_i=10;
int (*pf1)() = &base::func1;
int (base::*pf2)() = &base::func2;
