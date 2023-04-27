// 모듈 파일 안에 변수와 기능 등을 구현합니다.

const odd = "홀수입니다.";
const even = "짝수입니다.";

function test() {
  console.log("test");
}

// 모듈 파일의 정의된 변수/상수/함수를 외부에서 사용할 수 있도록 내보냅니다.
//module.export = {} 를 이용해 모듈내 기능과 변수를 노출해줘야 합니다.
// 외부 노출하는 방법은 객체의 속성과 함수로 노출 할 수 있다

module.exports = {
  odd,
  even,
  test,
};
