/*
operator+ - * /
*/
#include <iostream>

class Complex
{
public:
  Complex();
  Complex(double r, double i);
  friend Complex operator+(Complex &c, Complex &d);

  void print();

private:
  double real;
  double imag;
};

Complex::Complex()
{
  real = 0;
  imag = 0;
}

Complex::Complex(double r, double i)
{
  real = r;
  imag = i;
}

//friend
Complex operator+(Complex &c, Complex &d)
{
  return Complex(c.real+d.real, c.imag+d.imag);
};

void Complex::print()
{
  std::cout << "(" << real<<", "<<imag<<"i)\n";
};



int main()
{
  Complex c1(3,4), c2(5, -10), c3;

  c3 = c1 + c2;

  c1.print();

  c2.print();

  c3.print();

  return 0;
}
