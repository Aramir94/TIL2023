// index.js 라우터 파일은 기본적으로 메인 페이지/사이트 공통 기능에 대한 사용자 요청과 응답을 처리한다
// **  모든 라우터 파일은 기초 주소 체계를 가지고 있습니다. **
// ** index.js 라우터 파일은 무조건 http://localhost:3000/ 주소로 시작합니다. **
// ** 모든 라우터 파일은 기초 주소 체계 정의는 app.js 파일 내에서 설정합니다.

var express = require("express");

// express 객체의 Router() 메소드 호출 사용자 요청과 응답을 처리할 라우터 객체 생성합니다.
var router = express.Router();

/* GET home page. */
//실질적 라우팅 메서드를 통해 실제로 사용자 요청에 대한 응답을 처리합니다.
router.get("/", function (req, res, next) {
  res.render("index");
});

// 웹사이트 공통 기능중 문의하기 웹페이지에 대한 요청과 응답을 처리하는 라우팅 메서드
// router.get('호출 경로', function(req, res, next) { ... });

router.get("/contact", function (req, res, next) {
  // http://localhost:3000/contact 주소로 접속하면 라우팅 메서드가 실행됩니다.
  // 실행될 콜백 함수의 기능을 정의합니다.

  // res 객체는 웹 서버에서 웹 브라우저로 전달할 기능을 정의합니다
  // res.render() 메소드는 viesw 폴더에 있는 지정된 뷰파일(.ejs)을 웹 브라우저로 전달합니다.
  res.render("index");
});

router.get("/test", function (req, res, next) {
  res.render("index.ejs");
});

router.get("/sample/test/test1", function (req, res, next) {
  res.render("index.ejs");
});

//라우터 파일은 해당 라우터 파일에 정의된 router를 외부로 반환합니다.
module.exports = router;
