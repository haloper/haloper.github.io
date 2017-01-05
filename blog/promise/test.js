// 0. Promise 정의 방법
function timeAsync(sec, name, isFail) {

  console.log(name + " start");
  return new Promise(function(resolve, reject) {
    setTimeout(function() {
      console.log(name + " finish");
      !isFail ? resolve(name + " success") : reject(name + " fail");
    }, sec * 1000);
  });
}

// 1. 기본 사용법
function basic() {
  console.log("****************** basic ********************");
  return timeAsync(2, "A").then(function(result) {
    console.log(result);
  }, function(reason) {
    console.log(reason);
  });
}

// 2. chaining
function chaining() {
  console.log("****************** chaining ********************");
  return timeAsync(1, "A").then(function(result) {
    console.log(result);
    //then 함수 안에서 promise 객체를 또 리턴해주면 연속해서 비동기 함수 사용 가능
    return timeAsync(2, "B", true);
  }).then(function(result) {
    //success
    console.log(result);
  }, function(reason) {
    //fail
    console.log(reason);
  }).then(function() { //아무것도 리턴하지 않았을 경우에도 빈 Promise 객체를 리턴해 주기 때문에 chaining 사용 가능
    return timeAsync(3, "C");
  }).then(function(result) {
    console.log(result);
    return timeAsync(3, "D");
  }).then(function(result) {
    console.log("이제그만");
  });
}

// 3. all
// 하나라도 실패 시 바로 실패 처리
// 모두 성공 시 결과값을 배열로 전달
function all() {
  console.log("****************** all ********************");
  let a = timeAsync(2, "A");
  let b = timeAsync(3, "B");
  let c = timeAsync(4, "C");
  return Promise.all([a, b, c]).then(function(results) {
    console.log("모든 성공");
    console.log(results);
  }, function(reason) {
    console.log("작업 실패");
    console.log(reason);
  });
}

// 4. race
// 가장 빠른 결과값 처리
function race() {
  console.log("****************** race ********************");
  let a = timeAsync(4, "A");
  let b = timeAsync(3, "B");
  let c = timeAsync(2, "C");
  return Promise.race([a, b, c]).then(function(results) {
    console.log("첫번째 결과 도착");
    console.log(results);
  });
}

// 5. total test
// chaning, all 테스트 동시 진행 후 모두 완료되었을 때 basic 테스트 진행 후 이것도 완료되었을 때 race 테스트 진행 case
function total() {
  console.log("****************** total ********************");
  Promise.all([chaining(), all()]).then(function(result) {
    console.log("****************** chaining, all 완료 ********************");
    return basic();
  }).then(function(result) {
    console.log("****************** basic 완료 ********************");
    return race();
  }).then(function(result) {
    console.log("****************** race 완료 ********************");
  }).then(function(result) {
    console.log("****************** 모든 테스트 완료 완료 ********************");
  })
}
