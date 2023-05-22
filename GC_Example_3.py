# 참조된 횟수 알아내기 (레퍼런스 카운트)

import sys

class A:
    pass

a = A()
b = a

print(sys.getrefcount(a))

# 실행결과 => 3
# 기본적으로 오브젝트가 생성이 되었을때 getrefcount로 알아보면 2개가 기본이다.
