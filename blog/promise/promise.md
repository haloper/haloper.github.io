### Promise의 기초

#### Promise의 장점
Promise는 비동기 작업을 좀 더 편하게 구현할 수 있게 해준다. (콜백지옥에서 해방)  
단순히 ajax를 하나만 사용한다면 Promise는 오히려 불편하게 느껴질수도 있다.  
하지만, 여러개의 ajax를 직,병렬로 사용하게 된다면???  

> 예) 프론트 메인 페이지
메인 페이지 접근 시, 메인 화면 로딩과 회원정보 조회를 동시에 진행함.  
회원 정보 조회 완료 시 (메인화면 로딩과  상관없이) 이벤트 정보 로딩하여 노출  
위 모든 작업이 완료된 후에 버튼 이벤트 등록 (하나라도 미완료된 상태에서는 버튼 이벤트 등록하면 안됨)

#### 기본 구조

```
new Promise(function(resolve, reject) {
  // 비동기 작업 완료 시 reslove 호출
  // 비동기 작업 실패 시 reject 호출
});
```

#### Pomise 상태 값

  * **대기중**(pending): 초기 상태, 이행 또는 거부되지 않은. - 아무것도 호출되지 않은 상태
  * **이행됨**(fulfilled): 연산이 성공리에 완료되었음을 뜻합니다. - resolve 호출
  * **거부됨**(rejected): 연산이 실패했음을 뜻합니다. - reject 호출

#### Prototype

  * **then**
    Promise가 결정된 상태에서 호출됨. (이행 혹은 거부 상태)

#### Method

  * **all**
    배열로 전달된 모든 Promise가 성공 했을 경우 성공 처리  
    하나라도 실패했을 경우 전체 실패 처리
  * **race**
    배열로 전달된 Promise 중에서 가장 빠르게 결정된 Promise 결과에 따름

### Promise 실습

**Promise 정의 방법**  
내부적으로 비동기 로직이 동작해야 하는 함수일 경우, Promise를 리턴하게 구현해 놓으면 이후 사용하기가 편리하다.
```
function timeAsync(sec, name, isFail) {

  console.log(name + " start");
  return new Promise(function(resolve, reject) {
    setTimeout(function() {
      console.log(name + " finish");
      !isFail ? resolve(name + " success") : reject(name + " fail");
    }, sec * 1000);
  });
}
```

**기본 사용 방법**
```
// 2초 후에 결과값 노출
function basic() {
  console.log("****************** basic ********************");
  return timeAsync(2, "A").then(function(result) {
    console.log(result); //성공 시 노출
  }, function(reason) {
    console.log(reason); //실패 시 노출
  });
}
```

**Chaining 사용 방법**
```
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
```

**All 사용 방법**  
하나라도 실패 시 바로 실패 처리하고, 모두 성공 시에는 결과값을 모아서 배열로 전달
```
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
```

**Race 사용 방법**  
가장 빠른 결과값 처리
```
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
```

**여러 작업의 복합 사용 방법**  
chaning, all 테스트 동시 진행 후 모두 완료되었을 때 basic 테스트 진행 후 이것도 완료되었을 때 race 테스트 진행 case
```
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
```


### 참고
  * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise
