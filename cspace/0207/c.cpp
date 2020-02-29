#include <iostream>

void swap(int *x, int *y);

int main()
{
  int x, y;
  
  std::cout << "two diff int : ";
  std::cin >> x >> y;

  swap(&x, &y);

  std::cout <<"swap and result: " << x << ' ' << y << "\n";

  return 0;
}

void swap(int *x, int *y)
{
  int temp;
  temp = *x;
  *x = *y;
  *y = temp;
}

void swap2(int *x, int *y)
{
  *x ^= *y;
  *y ^= *x;
  *x ^= *y;
}


