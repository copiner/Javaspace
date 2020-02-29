/*
  A simple server in the internet domain using tcp
  The port number is passed as an argument
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

void
error(const char *msg)
{
  perror(msg);
  exit(1);
}

int
main(int argc, char *argv[])
{
  if(argc < 2){
    fprintf(stderr, "Port No not provided, Program terminated\n");
    exit(1);
  }

  int sockfd, newsockfd, portno, n;
  char buffer[255];

  struct sockaddr_in serv_addr, cli_addr;
  socklen_t clilen;
  
  //socket
  sockfd = socket(AF_INET, SOCK_STREAM, 0);
  if(sockfd < 0){
    error("Error opening Socket.");
  }

  bzero((char *) & serv_addr, sizeof(serv_addr));
  portno = atoi(argv[1]);

  serv_addr.sin_family = AF_INET;
  serv_addr.sin_addr.s_addr = INADDR_ANY;
  serv_addr.sin_port = htons(portno);

  //bind
  if(bind(sockfd,(struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0){
    error("Binding Failed.");
  }

  //listen
  listen(sockfd, 5);
  clilen = sizeof(cli_addr);

  //accept
  newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);

  if(newsockfd < 0){
    error("Error on accept.");
  }

  int num1, num2, answer, choice;
  //write
  n = write(newsockfd, "Enter Number 1: " strlen("Enter Number 1")); //ask no 1
  if(n<0)  error("Error writing to socket.")
  read(newsockfd, &num1, sizeof(int));                               //read no 1
  printf("Client - Number 1 is: %d\n", num1);

  int num1, num2, answer, choice;
  //write
  n = write(newsockfd, "Enter Number 2: " strlen("Enter Number 2"));//ask no 2
  if(n<0) error("Error writing to socket.")
  read(newsockfd, &num2, sizeof(int));                   //read no 2
  printf("Client - Number 2 is: %d\n", num2);  

  n = write(newsockfd, "Enter your choice: \n
                       1.Addition\n
                       2.Subtraction\n
                       3.Multiplcation\n
                       4.Division\n
                       5.Exit\n",
	    strlen("Enter your choice: \n
                       1.Addition\n
                       2.Subtraction\n
                       3.Multiplcation\n
                       4.Division\n
                       5.Exit\n"));
  if(n < 0) error("error writing to socket");
  read(newsockfd, &choice, sizeof(int));
  printf("Client - Choice is : %d\n", choice);

  switch(choice){
  case 1:
    ans = num1 + num2;
    break;
  case 2:
    ans = num1 - num2;
    break;
  case 3:
    ans = num1*num2;
    break;
  case 4:
    ans = num1/num2;
    break;
  case 5:
    goto Q;
    break;
  }
  //close
  close(newsockfd);
  close(sockfd);
  return 0;
  
}


