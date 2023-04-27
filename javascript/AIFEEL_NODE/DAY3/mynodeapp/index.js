import { odd, even, test } from "./base1.js";
const { checkOddOrEven } = require("./base2.js");

// 문자열을 매개 변수로 전달 받아서 문자열 길이 판단 후 홀 짝 판단
function checkStringOddOrEven(str) {
  // 전달된 str 문자열의 길이를 2로 나눈 나머지 값 (str.length%2)
  // 2/2 => 0, 3/2 => 1
  if (str.length % 2) {
    return odd; // 홀수 입니당~
  }
  return even; // 짝수 입니당~
}

// 최종 소비처 모듈
// 기능 노출 안 함
console.log("숫자 홀짝 여부 판단", checkOddOrEven(2));
console.log("문자 길이 홀짝 여부 판단", checkStringOddOrEven("hello"));

module.export(checkStringOddOrEven);
