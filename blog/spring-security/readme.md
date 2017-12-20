## Core 로직

### Authentication

#### Authentication

권한 정보를 저장하고 있는 객체

* getAuthorities : 가지고 있는 권한들
* getCredentials : PASSWORD
* getDetails : ID 주체에 대한 부가 정보들
* getPrincipal : ID
* isAuthenticated : 인증되었는지 여부 반환

#### GrantedAuthority

권한 정보


### UserDetails

#### UserDetailsService

username으로 부터 UserDetails 정보를 추출함

#### AuthenticationUserDetailsService

Authenticaiton으로 부터 UserDetails 추출

#### UserDetailsByNameServiceWrapper

UserDetailsService wrapper

#### JdbcDaoImpl

UserDetailsService의 jdbc 구현체
기본 Query를 사용하거나, 아니면 별도의 query 설정해줄 수 있음

**Default 설정**
users (username, password, enabled)
authorities (username, authority)
groups (id, group_name)
group_members (group_id, username)
group_authorities (group_id, authority)

### SecurityContext

#### SecurityContext

Authentication 객체를 저장하고, 불러오는 방법을 정의 (authentcation get,set)

#### SecurityContextHolder

SecurityContext를 저장하고 공유하는 기능을 담당하며, 저장 방법은 3가지로 구분된다.

* ThreadLocal (default) - ThreadLocalSecurityContextHolderStrategy
  동일 thread에서만 권한 정보를 공유함.
* InheritableThreadLocal - InheritableThreadLocalSecurityContextHolderStrategy
  동일 thread와 해당 thread에서 생성된 child thread까지도 권한 정보를 공유함.
* Global - GlobalSecurityContextHolderStrategy
  모든 thread에서 권한 정보를 공유함. Web 서비스가 아닌, client용 프로그램에 적합하다.

### ETC

#### CredentialsContainer

해당 인터페이스를 구현 시, 보안에 민감한 정보를 필요시 삭제해준다.

#### SpringSecurityMessageSource

Default MessageBundle 정의 : org.springframework.security.messages









## Authentication

### Authentication Implements

#### AbstractAuthenticationToken

Authentication 객체 구현 시 사용하는 base class
authorities, details, authenticated 정보를 가지고 있음

equils : authorities, details, credentials, principal 비교
Principal은 UserDetails(SpringSecurity), Pricipal(JavaSecurity) 둘 중에 하나를 가짐

#### AnonymousAuthenticationToken

* AbstractAuthenticationToken 구현체
* 인증되지 않음 user의 Authentication
* Int 형식의 hashkey를 가짐

#### AnonymousAuthenticationProvider

Provider에 제공된 key값을 가지지 않은 AnonymousAhtenticationToken 경우 BadCredentialsException 발생

#### RememberMeAuthenticationToken

* AbstractAuthenticationToken 구현체
* 식별된 user의 Authentication
* Int 형식의 hashkey를 가짐

#### RememberMeAuthenticationProvider

Provider에 제공된 key값을 가지지 않은 AnonymousAhtenticationToken 경우 BadCredentialsException 발생

#### UsernamePasswordAuthenticationToken

* Username(principal)과 password(credentials)를 이용한 초간단 authentication 구현체
* setAuthenticated을 호출할 수 없음
  username, password를 전달하는 용도로만 사용됨


#### AccountStatusUserDetailsChecker

UserDetail 상태값 확인 후 Exception 발생

#### AuthenticationTrustResolver

AuthenticationToken을 이용하여, 익명 여부, 저장 여부를 판단함

#### AuthenticationTrustResolverImpl

Authentcation이 AnonymouseAuthenticationToken인지 RememberMeAuthenticationToken인지 여부를 판단함

#### AuthenticationEventPublisher

Authentication 성공/실패 이벤트 발생기

#### DefaultAuthenticationEventPublisher

인증 실패 시, 전달받은 Exception과 매핑된 AuthenticationxxxEvent를 발생시킨다.

#### ProviderManager

* AuthenticationManager 구현체
* AuthenticationProvider list를 가지고 있음
* AuthenticationProvider를 하나씩 가져와 인증 진행
* 자신의 list가 모두 실패 시 parent로 인증 이관
* authentication 결과 값이 CredentialsContainer 구현체일 경우, eraseCredentials 실행
* 인증 진행 시 details 정보만 복사해서 가져옴

#### AbstractUserDetailsAuthenticationProvider

* UsernamePasswordAuthenticationToken에 응답하기 위해 디자인됨




### AuthenticatonManager



### AuthenticationProvider



### Etc

#### ApplicationEventPublisher
