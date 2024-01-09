#include <stdio.h>

int main(void) {
  char arr[5][15] = {
      0,
  };
  for (int i = 0; i < 5; i++) {
    scanf("%s", arr[i]);
  }
  for (int j = 0; j < 15; j++){
    for (int i = 0; i < 5; i++){
      if (arr[i][j] != NULL){
        printf("%c", arr[i][j]);
      }
    }
  }
}