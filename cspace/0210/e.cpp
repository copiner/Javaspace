/*
  public protected private
*/

#include <iostream>

class Base
{
private://...
  int b1;
protected:
  int b2;
  
  void fb2()
  {
    b1 = 2;
  }
public:
  int b3;
  void fb3()
  {
    b1 = 3;
  }
};

class Pri : private Base
{
public:
  void test()
  {
    b1 = 1;//error
    
    b2 = 1;
    b3 = 1;
    fb2();
    fb3();
  }
};

class FromPri : public Pri
{
public:
  void test()
  {
    b1 = 1;//err
    b2 = 1;//err
    b3 = 1;//err
    fb2();//err
    fb3();//err
  }
};

class Pro : protected Base
{

public:
  void test()
  {
    b1 = 1;//err
    b2 = 1;
    b3 = 1;
    fb2();
    fb3();
  }

};

class FromPro : public Base
{
public:
  void test()
  {
    b1 = 1;//err
    b2 = 1;
    b3 = 1;
    fb2();
    fb3();
  }

};

class Pub : public Base
{
public:
  void test()
  {
    b1 = 1;//err
    b2 = 1;
    b3 = 1;
    fb2();
    fb3();
  }

};

class FromPub : public Base
{
public:
  void test()
  {
    b1 = 1;//err
    b2 = 1;
    b3 = 1;
    fb2();
    fb3();
  }

};

int main()
{
  Pri priObj;

  priObj.b1 = 1;//err
  priObj.b2 = 1;//err
  priObj.b3 = 1;//err

  Pro proObj;

  proObj.b1 = 1;//err
  proObj.b2 = 1;//err
  proObj.b3 = 1;//err

  Pub pubObj;

  pubObj.b1 = 1;//err
  pubObj.b2 = 1;//err
  pubObj.b3 = 1;

  return 0;

}
