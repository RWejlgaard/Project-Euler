#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* revStr(char *str)
{
    char temp;
    size_t len = strlen(str) - 1;
    size_t stop = len/2;
    size_t i,k;

    for(i = 0, k = len; i < stop; i++, k--)
    {
    	temp = str[k];
    	str[k] = str[i];
    	str[i] = temp;
    }
    return str;
}

int main(int argc, char const *argv[]) {
  for (int x = 100; x < 1000; x++) {
    for (int y = 100; y < 1000; y++) {
      int z = x * y;
      char *zStr;
      sprintf(zStr, "%d", z);
      char *zRev = revStr(zStr);
      int zRevInt = atoi(zRev);
      if (z == zRevInt) {
        printf("%d\n", zRevInt);
      }
    }
  }

  return 0;
}
