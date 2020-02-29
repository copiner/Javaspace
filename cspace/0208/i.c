
#include <stdio.h>

#define SENT_LEN 100

int main()
{
  char sentence[SENT_LEN+1];

  printf("Enter a sentence: \n");
  //  scanf("%s",sentence);

  //  printf("%s",sentence);

  gets(sentence);

  puts(sentence);

  return 0;
}
