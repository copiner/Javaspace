/*
  char string
*/
#include <stdio.h>
#include <string.h>

int main()
{
  char date[] = "Febur 8";
  char *p;
  p = date;
  
  int a[5] = {3,4,7,8,1};
  int *d;

  d = a;

  printf("date1: %s\n", date);  
  printf("date2: %s\n", p);  
  printf("a: %d\n", *d);  
  puts(date);

  
  return 0;
}
