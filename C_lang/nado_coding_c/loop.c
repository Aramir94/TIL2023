#include<stdio.h>

int main(void){
    printf("Hello world\n");
    // ++ 
    int a = 10;

    printf("%d\n", ++a); // ++ 동작을 수행하고 실행
    printf("%d\n", a++); // ++ 동작을 코드 수행하고 실행
    printf("%d\n", a);

    return 0;
}