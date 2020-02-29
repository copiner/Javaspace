
#include <stdio.h>

#define NAME_LEN 25

typedef struct{
  int number;
  char name[NAME_LEN+1];
  int on_hand;
} Part;

int main()
{
  Part part1 = {199,"Gold", 20};
  Part part2;

  part2 = part1;

  printf("Part number: %d\n",part2.number);
  printf("Part name: %s\n",part2.name);
  printf("on hand: %d\n",part2.on_hand);
  
  return 0;
}
