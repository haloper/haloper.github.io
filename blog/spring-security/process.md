### AbstractSecurityInterceptor - FilterSecurityInterceptor

#### Dependency
* ApplicationEventPublisher
* AccessDecisionManager
* AfterInvocationManager
* AuthenticationManager
* RunAsManager

#### abstract
* getSecureObjectClass()
* obtainSecurityMetadataSource();

#### Child
* FilterSecurityInterceptor

#### Use
* SecurityMetadataSource

#### Process
beforeInvocation -> doFilter -> finalInvocation -> afterInvocation

##### beforeInvocation
1. authenticateIfRequired 실행
  authenticatino이 false이거나, alwaysReauthenticate가 true이면 실행
  실행 후 SecuretyContextHolder 갱신
1. accessDecisionManager.decide 실행
  접근 가능 여부 확인
1. SecuirytyContext에 EmptyContext 생성
1. InterceptorStatusToken 반환

##### finalInvocation
InterceptorStatusToken의 contextHolderRefreshRequired가 false로 설정되어 있을 경우, SecuirtyContext update (RunAs가 null일 경우...)

##### afterInvocation
