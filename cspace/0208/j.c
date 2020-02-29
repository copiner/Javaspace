
#include <stdio.h>

#define SENT_LEN 100

int read_line(char str[], int n);

int count_spaces_a(const char s[]);
int count_spaces_p(const char *s);

int main()
{
  char str[SENT_LEN+1];
  int len;

  printf("Enter a sentence: \n");
  read_line(str, SENT_LEN);
  

  printf("Sentence: %s\n", str);

  len = count_spaces_a(str);

  printf("len: %d\n", len);

  return 0;
}

int read_line(char str[], int n)
{
  int ch, i = 0;

  while((ch = getchar())!='\n'){
    if(i<n){
      str[i++] = ch;
    }
  }
 
  str[i] = '\0';
  return i;

}

int count_spaces_a(const char s[])
{
  int count = 0, i;

  for(i = 0; s[i] != '\0'; i++){
    if(s[i] == ' ')
      count++;
  }
  
  return count;
}
int count_spaces_p(const char *s)
{
  int count = 0;
  for(; *s != '\0'; s++){
    if(*s == ' ')
      count++;
  }
  return count;
}
