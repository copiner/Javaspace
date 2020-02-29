#include <stdio.h>
#include <stdlib.h>

void main(){

  int i;
  int sum = 0;
  char ch;

  printf("intergite blankspace any: ");

  while( scanf("%d", &i) == 1 ){

    sum += i;

    while( (ch=getchar()) == ' ' );

    if (ch == '\n'){
      break;
    }

    ungetc(ch, stdin);
  }

  printf("result : %d" , sum);
  printf("\n");
  system("pause");
  
}
