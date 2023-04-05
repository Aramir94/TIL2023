# include <stdio.h>

/* 안녕하셈 */
// 반갑셈
int main(void)
{
    // 변수 -> 변경 가능한수 
    // 정수형
    int age = 12;
    printf("%d\n", age);

    age = 13;
    printf("%d\n", age);

    // 실수형
    float f = 46.5f;
    printf("%f\n", f);
    printf("%.2f\n", f);
    
    double d = 4.526;
    printf("%f\n", d);
    printf("%.2f\n", d);

    // 상수 : 변하지 않는 수 
    const int YEAR = 2000;

    // 연산
    int add = 3 + 8;
    printf("3 + 8 = %d\n", add);
    printf("%d + %d = %d\n", 3, 5, 3+5);


    // scanf 
    // 키보드 입력을 받아서 저장 
    int a;
    printf("값을 입력하세요 : ");
    scanf("%d", &a);
    printf("입력값은 %d 입니다\n", a);

    return 0;
}