
#include <stdio.h>

#define NAME_LEN 25
struct part {
  int number;
  char name[NAME_LEN+1];
  int on_hand;
};

int main()
{
  struct part part1,part2;
  struct part part3 = {199,"Gold", 20};

  part2 = part3;

  printf("Part number: %d\n",part2.number);
  printf("Part name: %s\n",part2.name);
  printf("on hand: %d\n",part2.on_hand);
  
  return 0;
}
