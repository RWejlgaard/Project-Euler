#include <stdio.h>

int main(int argc, char const *argv[]) {
  int x = 1;
  int y = 2;
  int z = 0;
  int s = 2;
  while (x < 4000000 && y < 4000000) {
    if (z == 0) {
      x = x+y;
      if ((x % 2) == 0) {
        s += x;
      }
      z = 1;
    }
    if (z == 1) {
      y = x+y;
      if ((y % 2) == 0) {
        s += y;
      }
      z = 0;
    }
  }

  printf("%d\n", s);

  return 0;
}
