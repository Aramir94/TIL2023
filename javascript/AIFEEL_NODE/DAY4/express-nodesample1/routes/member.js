// 회원 정보 관리용 모든 웹페이지에 대한 요청 과 응답 처리하는 라우터 파일
var express = require("express");
var router = express.Router();

// 회원 신규 가입 웹페이지 요청 및 응답 처리 라우팅 메서드

router.get("/entry", function (req, res, next) {
  res.render("entry.ejs");
});

// 회원 로그인 웹페이지 요청 및 응답 처리 라우팅 메서드
router.get("/login", function (req, res, next) {
  res.render("login.ejs");
});

// 회원 프로파일 정보 웹페이지 요청 및 응답 라우팅 메서드
router.get("/profile", function (req, res, next) {
  res.render("profile.ejs");
});

module.exports = router;
