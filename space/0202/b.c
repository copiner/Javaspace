#include <stdio.h>

int addArray( int *array, int n );

int main(){
  int data[] = {9,8,7,6,5,4,3,2,1,0};
  int size = sizeof(data) / sizeof(data[0]);

  printf("result: %d\n", addArray( data,size ));
		
  return 0;
}
int addArray( int *array, int n){
  int sum = 0;
  int i;

  printf("a: %d\n", array);
  
  for( i=0; i<n; i++ ){
    printf("r: %d\n", *array);
    sum += *array++;
  }
	
  return sum;
}
