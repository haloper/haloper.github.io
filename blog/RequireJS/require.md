### RequireJS

#### RequireJS란?
AMD(Asynchronous Module Definition) spec의 구현체

> AMD는 동적로딩, 의존성 관리, 모듈화를 구현하기 위한 API 디자인

**동적로딩**
HTML 페이지 상에서 script tag를 선언하여 script 파일을 로딩하는 전통적인 방식은 성능상의 문제가 있다. 브라우저는 script tag를 읽는 순간 script의 내용을 파싱해야 하고, 그동안 브라우저는 멈춰있게 된다. RequireJS는 페이지 랜덩링 이후에 script 태그를 동적으로 생성해서 삽입해 준다.

**의존성 관리**
Javascript는 의존성 관리가 되지 않는다. 가장 많이쓰이는 라이브러리를 위쪽에 배치하는 수 밖에....  
RequireJS는 의존성 관리를 명시적으로 선언하고, 명확하게 동작하도록 해준다.

**모듈화**
RequireJS는 불필요하게 Window namespace를 더럽히지 않고, 필요한 부분만 노출하며, 캡슐화가 가능하다.

#### 기본 사용법
파일 구조는 다음과 같다고 가정했을때...
* www/
  * index.html
  * js/
    * app/
      * sub.js
    * lib/
      * jquery.js
      * canvas.js
    * app.js
    * require.js

index.html 페이지에는 아래와 같은 script tag 하나만 선언해 주면 된다.
```
<script data-main="js/app.js" src="js/require.js"></script>
```
src에는 RequireJS 라이브러리를 선언해 주면 되고, data-main에는 모든 javascript 모듈의 시작점인 entry-point를 선언해 주면 된다.

app.js에는 기본적으로 다음과 같은 내용이 정의된다.
```
//RequireJS 설정
requirejs.config({
    // 모든 모듈들이 baseUrl 기준으로 상대경로로 표시된다.
    baseUrl: 'js/lib',
    // 자주 쓰는 경로는 paths로 미리 지정해 둘 수 있다.
    paths: {
        app: '../app'
    }
});

//Page 로딩 시 시작할 코드들
requirejs(['jquery', 'app/sub'], function ($, sub) {
    // jquery.js 및 sub.js가 모두 로딩되고 난 후에 여기있는 코드가 실행된다.
    // $, sub에는 jquery, sub 모듈이 주입된다.
});
```


#### Module 선언

의존성을 가지지 않고, 단순 객체를 돌려주는 경우
```
define({
    color: "black",
    size: "unisize"
});
```
그런데 초기화 작업이 필요할 경우
```
define(function () {
    //여기서 초기화 가능

    return {
        color: "black",
        size: "unisize"
    }
});
```
의존성이 필요한 경우
```
define(["cart", "inventory"], function(cart, inventory) {

        return {
            color: "blue",
            size: "large",
            addToCart: function() {
                inventory.decrement(this);
                cart.add(this);
            }
        }
    }
);
```
객체가 아니라, 함수를 돌려주는 것도 가능함. (리턴 가능한 모든 형식 사용 가능)
```
define(["my/cart", "my/inventory"],
    function(cart, inventory) {

        return function(title) {
            return title ? (window.title = title) :
                   inventory.storeName + ' ' + cart.name;
        }
    }
);
```

**Modue 선언 시 참고 사항**
* Module 선언 시 이름을 지정해 줄 수 있지만, 비추 (Module 이름은 파일명을 사용하도록 내버려 두는게 유연함)
* 하나의 파일에 하나의 모듈만 정의해야 함 (Optimizer가 여러 모듈을 하나의 파일로 모아주기는 함)
* Module의 경로는 Config의 baseUrl 기준으로 상대 경로를 나타내며, 필요시 절대 경로도 사용 가능
  확장자를 붙이거나, "/"로 시작하거나, 전체 url를 써주거나...

#### Configuration Options

**baseUrl**: module id를 찾기 위한 기본 경로. baseUrl를 기준으로 상대경로로 표시함. 예외 ("/"로 시작, "http"로 시작, ".js"로 종료)
**path**: baseUrl로 부터의 특정 경로를 하나의 값으로 설정할 수 있음
**shim**: 모듈화 되지 않은 javascript 라이브러리들을 사용할 수 있게 해줌
```
requirejs.config({
    shim: {
      'backbone': { // `/js/lib/backbone.js`를 로드해 모듈을 정의하고 `window.backbone`을 리턴한다.
        exports: 'backbone'
      },
      'jquery': {
        exports: '$'
      },
      'underscore': {
        exports: '_'
      },
      'jquery-scroll': [ 'jquery' ]
    }
});
```  
* **bundles**: 여러 module들을 하나의 script로 묶여저 있는 상태의 파일을 가져다 쓸 때 사용
* **map**: 여러개의 모듈을 하나의 id에 매핑할 수 있고, 매핑된 id를 가져다 쓰는 곳에 따라 실제 어떤 모듈을 사용하게 되는지 설정할 수 있음
```
requirejs.config({
    map: {
        '*': { // some/oldmodule을 제외한 모든 모듈에서는 foo1.2 사용
            'foo': 'foo1.2'
        },
        'some/oldmodule': { // some/oldmodule에서는 foo1.0 module 사용
            'foo': 'foo1.0'
        }
    }
});
```
* **config**: 모듈 내부에서 사용할 수 있는 설정값들을 정의함
```
requirejs.config({
    config: {
        'bar': {
            size: 'large'
        },
        'baz': {
            color: 'blue'
        }
    }
});
define(['module'], function (module) {
    //Will be the value 'blue'
    //modue은 해당 module의 기본 정보와 config 정보를 가지고 있는 dependency
    var color = module.config().color;
});
```
* **waitSeconds**: 모듈 로딩시 timeout 설정
* **enforceDefine**: 모든 모듈들이 define으로 정의되어야만 하도록 강제함. 아닐 시 오류 발생
* **urlArgs**: 이 설정값을 이용하면 브라우저 캐쉬로 인해 수정된 script 파일이 적용되지 않는 문제를 해결할 수 있음.  
scriptfilename.js?urlArgs <- 이런식으로 스크립트 파일을 호출함.  
urlArgs에 빌드 시간을 넣어주게 되면 굉장히 효율적일듯...
```
urlArgs: "bust=" +  (new Date()).getTime()
```

#### Optimizer

* 의존성이 정의된 여러 js 모듈들을 하나의 js 파일로 통합해줌
* node가 설치되어 있어야 함.
* css 파일도 통합이 가능함. import로 의존성이 정의되어 있어야 함

**기본 사용법**
build.js 파일 생성
```
({
    baseUrl: ".",
    paths: {
        jquery: "some/other/jquery"
    },
    name: "main", // 파일 통합의 시작점
    out: "main-built.js" // 최종 output 파일
})
```
optimizer 실행
```
node r.js -o build.js
```
RequireJS의 설정파일을 공유할 수 있음
```
mainConfigFile: 'path/to/main.js'
```

**CSS 파일 통합 방법**
css 파일 경로로 이동 후 아래 cmd 실행
```
node ../../r.js -o cssIn=main.css out=main-built.css
```

#### Plugin
* Specify a Text File Dependency  
Static 파일을 읽어와 String 형식으로 사용 가능
```
require(["some/module", "text!some/module.html", "text!some/module.css"],
    function(module, html, css) {
        //the html variable will be the text
        //of the some/module.html file
        //the css variable will be the text
        //of the some/module.css file.
    }
);
```
* Define an I18N Bundle  
다국어 처리를 지원함
```
//Contents of my/nls/colors.js
define({
    "root": {
        "red": "red",
        "blue": "blue",
        "green": "green"
    },
    "fr-fr": true
});
```
```
//Contents of my/nls/fr-fr/colors.js
define({
    "red": "rouge",
    "blue": "bleu",
    "green": "vert"
});
```
```
define(["i18n!my/nls/colors"], function(colors) {
    return {
        testMessage: "The name for red in this locale is: " + colors.red
    }
});
```

#### 참고 사이트
* http://d2.naver.com/helloworld/591319
* http://requirejs.org/docs/api.html
* https://github.com/requirejs/example-multipage-shim
