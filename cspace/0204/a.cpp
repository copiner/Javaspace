/*
  overloading features
*/


#include <iostream>

void convertTemperature(double temperIn, char typeIn);
void convertTemperature(int temperIn, char typeIn);

int main()
{

  double temperInDouble;
  char typeIn;
  
  int temperInInt;

  std::cout<<"example:xx.x C OR xx.x F \n"<<std::endl;
  std::cin >> temperInDouble >> typeIn;
  std::cin.ignore(100,'\n');

  std::cout << "\n";

  convertTemperature(temperInDouble, typeIn);

  std::cout<<"example:xx C OR xx F \n"<<std::endl;
  std::cin >> temperInInt >> typeIn;
  std::cin.ignore(100,'\n');

  std::cout << "\n";

  convertTemperature(temperInInt, typeIn);

  return 0;
}

void
convertTemperature(double temperIn, char typeIn)
{
  const unsigned short ADD_SUBTRACT = 32;
  const double RADIO = 9.0 / 5.0;

  double temperOut;
  char typeOut;


  switch(typeIn){
  case 'C':
  case 'c':
    temperOut = temperIn * RADIO + ADD_SUBTRACT;
    typeOut = 'F';
    typeIn = 'C';
    break;
  case 'F':
  case 'f':
    temperOut = (temperIn - ADD_SUBTRACT)/RADIO;
    typeOut = 'C';
    typeIn = 'F';
    break;
  default:
    typeOut = 'E';
    break;
  }

  if(typeOut != 'E'){
    std::cout << temperIn << typeIn
	      << " = " << temperOut << typeOut<<"\n";
  } else {
    std::cout<<"input err\n"<<std::endl;
  }

  std::cout<<"any char over\n"<<std::endl;
  std::cin.get();

}

void
convertTemperature(int temperIn, char typeIn)
{
  const unsigned short ADD_SUBTRACT = 32;
  const double RADIO = 9.0 / 5.0;

  int temperOut;
  char typeOut;


  switch(typeIn){
  case 'C':
  case 'c':
    temperOut = temperIn * RADIO + ADD_SUBTRACT;
    typeOut = 'F';
    typeIn = 'C';
    break;
  case 'F':
  case 'f':
    temperOut = (temperIn - ADD_SUBTRACT)/RADIO;
    typeOut = 'C';
    typeIn = 'F';
    break;
  default:
    typeOut = 'E';
    break;
  }

  if(typeOut != 'E'){
    std::cout << temperIn << typeIn
	      << " = " << temperOut << typeOut<<"\n";
  } else {
    std::cout<<"input err\n"<<std::endl;
  }

  std::cout<<"any char over\n"<<std::endl;
  std::cin.get();

}
