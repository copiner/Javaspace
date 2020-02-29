
#include <iostream>

#define FULL_GAS 85

class Car{

public:
  std::string color;
  std::string engine;
  unsigned int gas_tank;
  unsigned int wheel;

  void setColor(std::string c);
  void setEngine(std::string e);
  void setWheel(unsigned int w);
  void fillTank(unsigned int l);

  void warning(void);

  int running(void);
  
};

void Car::setColor(std::string c)
{
  color = c;
}

void Car::setEngine(std::string e)
{
  engine = e;
}

void Car::setWheel(unsigned int w)
{
  wheel = w;
}

void Car::fillTank(unsigned int l)
{
  gas_tank += l;
  std::cout<<"full gas tank: " << gas_tank<<"\n";;
}

int Car::running(void)
{
  std::cout << "running 120\n";
  gas_tank--;
  std::cout << "surplus gas: "<<100*gas_tank/FULL_GAS<<"% gas!\n";

  return gas_tank;
}

void Car::warning(void)
{
  std::cout << "warning surplus: "<<100*gas_tank/FULL_GAS<<"% gas!\n";
}

int main()
{
  char i;
  Car dcar, xcar;

  dcar.setColor("WHITE");
  dcar.setEngine("v8");
  dcar.setWheel(4);

  dcar.gas_tank = FULL_GAS;

  while(dcar.running())
  {
    if(dcar.gas_tank < 10)
    {
      dcar.warning();
      std::cout << "add gas ? Y/N \n";
      std::cin >> i;

      if('Y' == i || 'y' == i)
      {
	int t = FULL_GAS - dcar.gas_tank;
	dcar.fillTank(t);
      }
    }
  }
  return 0;
}
