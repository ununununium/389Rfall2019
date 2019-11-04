#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define PASS_SIZE 16

int main(){
  char *password;
  int i;

  sleep(0.0039);
  sleep(2);
  srand(time(0));
  password = calloc(1, PASS_SIZE+1);
  for (i = 0; i < PASS_SIZE; i++) {
      password[i] = rand() % ('z'-' ') + ' ';
  }
  password[PASS_SIZE] = 0;

  printf("%s\n",password);
  return 0;
}
