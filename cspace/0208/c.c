#include <stdio.h>

#define NAME_LEN 25

struct {
  int number;
  char name[NAME_LEN+1];
  int on_hand;
} part1 = {.number = 528, .name = "Disk drive", .on_hand = 10},
  part2 = {.on_hand = 16, .name = "Color", .number = 3};

int main()
{
  printf("Part Number: %d\n",part1.number);
  printf("Part name: %s\n",part1.name);
  printf("Quantity on hand: %d\n\n",part1.on_hand);

  part1.number= 258;
  part1.on_hand++;

  printf("Part Number: %d\n",part1.number);
  printf("Part name: %s\n",part1.name);
  printf("Quantity on hand: %d\n\n",part1.on_hand);

  printf("Part Number: %d\n",part2.number);
  printf("Part name: %s\n",part2.name);
  printf("Quantity on hand: %d\n\n",part2.on_hand);

  part2 = part1;

  printf("Part Number: %d\n",part2.number);
  printf("Part name: %s\n",part2.name);
  printf("Quantity on hand: %d\n\n",part2.on_hand);

  return 0;
}
