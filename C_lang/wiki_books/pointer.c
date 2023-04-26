#include <stdio.h>

int main() {
    int num = 10;
    int *ptr = &num;

    printf("num의 값: %d\n", num);
    printf("num의 주소: %p\n", &num);
    printf("ptr이 가리키는 값: %d\n", *ptr);
    printf("ptr의 값: %p\n", ptr);

    return 0;
}
