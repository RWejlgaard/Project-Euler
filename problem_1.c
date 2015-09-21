#include <stdio.h>

int main(int argc, char const *argv[]) {
  int total = 0;

  for (int i = 0; i <= 1000; i+=3) {
    total += i;
  }

  for (int i = 0; i <= 1000; i+=5) {
    total += i;
  }

  printf("%d\n", total);

  return 0;
}
