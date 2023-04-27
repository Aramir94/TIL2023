// base1.js 모듈을 참조
// 해당 모듈에서 다른 모듈을 불러 참조 할때 node import 예약어 보다 require() 함수를 사용한다.
const { odd, even, test } = require("./base1.js");
// import { odd, even, test } from "./base1.js";

// 숫자를 매개 변수로 전달 받아서 홀 짝 판단
function checkOddOrEven(num) {
  // 전달된 num 숫자를 2로 나눈 나머지 값 (num%2)
  // 2/2 => 0, 3/2 => 1
  //
  if (num % 2) {
    return odd;
  }
  return even;
}

console.log("테스트 결과 입니다", checkOddOrEven(2));
console.log("테스트 결과 입니다", checkOddOrEven(3));

module.exports = { checkOddOrEven };
