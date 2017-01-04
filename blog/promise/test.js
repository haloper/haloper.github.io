
function timeAsync(sec, name, success) {

  console.log(name + " start");
  return new Promise(function(resolve, reject) {
    setTimeout(function() {
      console.log(name + " finish");
      success ? resolve(name + " success") : reject(name + " fail");
    }, sec * 1000);
  });
}

function basic() {
  // 1. 기본 사용법
  timeAsync(2, "A").then(function(result) {
    console.log(result);
  }, function(reason) {
    console.log(reason);
  });
}

function chaining() {
// 2. chaining
  timeAsync(2, "A").then(function(result) {
    console.log(result);
    //then 함수 안에서 promise 객체를 또 리턴해주면 연속해서 비동기 함수 사용 가능
    return timeAsync(3, "B", true);
  }, function(reason) {
    console.log(reason);
    return timeAsync(3, "B", true);
  }).then(function(result) {
    console.log(result);
    return timeAsync(3, "C", true);
  }).then(function(result) {
    console.log("이제그만");
  });
}

// 3. all
