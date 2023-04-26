#include <stdio.h>

int main() {
    int nums[5] = {1, 2, 3, 4, 5};  // 크기가 5인 정수형 배열 선언 및 초기화
    int *ptr = nums;               // 포인터 변수에 배열의 주소 저장
    int sum = 0;

    for (int i = 0; i < 5; i++) {
        sum += *(ptr + i);          // 포인터를 이용하여 배열의 값을 가져와서 합산
    }

    printf("배열의 합: %d\n", sum);

    return 0;
}
