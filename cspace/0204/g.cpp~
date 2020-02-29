#include <iostream>

int main()
{
  //h = c*9.0/5.0 +32
  const unsigned short ADD_SUBTRACT = 32;
  const double RADIO = 9.0 / 5.0;

  double temperIn, temperOut;
  char typeIn, typeOut;

  std::cout<<"example:xx.x C OR xx.x F \n"<<std::endl;
  std::cin >> temperIn >> typeIn;
  std::cin.ignore(100,'\n');

  std::cout << "\n";

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
  
  return 0;
}
