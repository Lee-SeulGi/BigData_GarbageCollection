# 오브젝트를 참조중인 목록 알아내기

import gc

def test():
    class A:
        pass

    class B:
        def __init__(self, obj): 
            self.obj = obj

    a = A()
    b = B(a)

    gc.collect()
    print( gc.get_referrers(a) )

test()

# 실행결과 => [<frame object at 0x7fa4903f9e10>, {'obj': <__main__.test.<locals>.A object at 0x7fa4902dd588>}]
# a를 참조하고 있는 목록이 리스트로 출력
