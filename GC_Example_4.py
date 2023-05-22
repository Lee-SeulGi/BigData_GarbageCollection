# 오브젝트가 현재 참조중인 목록 알아내기

import gc

def test():
    class A:
        pass

    class B:
        def __init__(self, obj): 
            self.obj = obj

    a = A()
    b = B(a)

    gc.collect() # make sure all garbage cleared before collecting referrers.    
    print( gc.get_referents(b))

test()

# 실행결과 => [{'obj': <__main__.A object at 0x7fa49038e630>}, <class '__main__.B'>]
# b라는 변수는 현재 'obj'라는 멤버변수를 가지고 있고, B라는 클래스로부터 만들어졌으므로 위와 같이 출력된다.
