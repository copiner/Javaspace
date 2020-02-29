
#include <stdio.h>
#include <string.h>

#define NAME_LEN 25

struct part{
  int number;
  char name[NAME_LEN+1];
  int on_hand;
};

void print_part(struct part p);

int main()
{
  struct part inventory[100];
  
  strcpy(inventory[99].name, "Tim");

  print_part(inventory[99]);
  
  return 0;
}

void print_part(struct part p)
{
  printf("Part number: %d\n",p.number);
  printf("Part name: %s\n",p.name);
  printf("Quantity on hand: %d\n",p.on_hand);
  
}
