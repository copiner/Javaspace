/*
gcc getop.c gccemo.c -o output.out
*/

#include <stdio.h>
#include <stdlib.h>
#include "getop.h"

int main()
{
  int a = 9;
  int b = getch(a);
  int c = getop(a);
  int d = ungetch(a);

  printf("a+b+c+d = %d", a+b+c+d);

  return 0;
}
