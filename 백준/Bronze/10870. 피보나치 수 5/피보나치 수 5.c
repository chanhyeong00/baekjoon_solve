#include <stdio.h>
int fibonach(int n){
    if (n == 0) return 0;
    else if (n == 1) return 1;
    
    return fibonach(n - 1) + fibonach(n - 2);
    
}

int main(void){
    int n;
    int answer;
    scanf("%d", &n);
    printf("%d\n", fibonach(n));
}