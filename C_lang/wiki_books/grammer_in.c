#include <stdio.h>

int main() {
    int num = 10;   // 정수형 변수 선언 및 초기화
    int *ptr;       // 포인터 변수 선언

    ptr = &num;     // 포인터 변수에 변수 num의 주소 저장

    printf("num의 값: %d\n", num);      // 변수 num의 값 출력
    printf("num의 주소: %p\n", &num);  // 변수 num의 주소 출력
    printf("ptr의 값: %p\n", ptr);     // 포인터 변수 ptr의 값(주소) 출력
    printf("ptr가 가리키는 값: %d\n", *ptr);  // 포인터 변수 ptr가 가리키는 변수의 값 출력

    return 0;
}
