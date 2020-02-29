#include <iostream>

class ClxBase
{
public:
  ClxBase()
  {
  };

  virtual ~ClxBase()//...
  {
  };

  virtual void doSth()
  {
    std::cout<<"Do sth in class ClxBase!\n";
  };
};

class ClxDerived : public ClxBase
{
public:
  ClxDerived()
  {
  };

  ~ClxDerived()
  {
    std::cout<<"destructor of class ClxDerived\n";
  };

  void doSth()
  {
    std::cout<<"do sth in class ClxDerived!\n";
  };
};

int main()
{
  ClxBase *pd = new ClxDerived();

  pd -> doSth();

  delete pd;
  return 0;
}
