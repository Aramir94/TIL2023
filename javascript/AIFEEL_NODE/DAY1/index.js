// 프로젝트에서 node package를 참조합니다
// if you want to use node package use require command
const moment = require("moment");

console.log("터미널 창에 로그 정보 기록합니다");

console.log("현재 날짜 시간 정보를 출력합니다", Date.now());

console.log(
  "현재 날짜 시간 정보를 출력합니다",
  moment(Date.now()).format("YYYY-MM-DD HH:mm:ss")
);

/*
npm install moment dotenv
npm install (npm i)
npm install nodemon --save-dev
npm install -global <package> (npm i -g <package>)
whereis npm 
npm: /Users/flycode77/.nvm/versions/node/v16.16.0/bin/npm : 여기에 설치됨 
*/
