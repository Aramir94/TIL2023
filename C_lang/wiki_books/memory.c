int main() {
  int x = 1, y = 2;
  int *ptr;

  ptr = &x; // ptr에 x의 주소를 저장
  x = y;
  y = *ptr; // y에 ptr이 가리키는 값, 즉 x의 값 저장

  printf("x = %d, y = %d\n", x, y);
  return 0;
}
