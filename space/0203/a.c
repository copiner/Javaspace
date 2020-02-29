#include <stdio.h>
#include <stdlib.h>

int main( int argc, char* argv[] ){

  FILE *in, *out;
  int ch;

  if( argc != 3 ){
    fprintf(stderr, "input example: a sourcefile targetfile \n");
    exit( EXIT_FAILURE );
  }

  if((in = fopen(argv[1], "rb")) == NULL){
    fprintf(stderr, "can't open 1: %s \n", argv[1]);
    exit( EXIT_FAILURE );
  }

  if((out = fopen(argv[2], "wb")) == NULL){
    fprintf(stderr, "can't open 2: %s \n", argv[2]);
    fclose(in);
    exit( EXIT_FAILURE );
  }

  while((ch = getc(in) != EOF)){// EOF(-1) == end of file
    if(putc(ch,out)==EOF){
      break;
    }
  }

  if(ferror(in)){
    printf("read file  %s fail!\n", argv[1]);
  }

  if(ferror(out)){
    printf("write file  %s fail!\n", argv[2]);
  }

  printf("copy 1 file suc!\n");

  fclose(in);
  fclose(out);

  return 0;
}
