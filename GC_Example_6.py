# 현재 자신을 참조중인 오브젝트를 찾아내어 강제로 자신을 지우기

import sys, gc

def delete_me(obj):
    referrers = gc.get_referrers(obj)
    for referrer in referrers:
        if type(referrer) == dict:
            for key, value in referrer.items():
                if value is obj:
                    referrer[key] = None

def test():            
    class A:
        def __del__(self):
                print("deleted")

    class B:
        def __init__(self, obj): 
            self.obj = obj

    a = A()
    b = B(a)

    print("before : ", b.__dict__)
    delete_me(a)
    print("after : ", b.__dict__)
    print("ref count : ", sys.getrefcount(a))
    gc.collect()
    print("ref count : ", sys.getrefcount(a))
    del(a)

test()

# 실행결과 =>
'''
before :  {'obj': <__main__.test.<locals>.A object at 0x7fa4902f02b0>}
after :  {'obj': None}
ref count :  4
ref count :  2
deletedbefore :  {'obj': <__main__.test.<locals>.A object at 0x7fa4903c0940>}
after :  {'obj': None}
'''

# a객체는 원래 b객체의 'obj'라는 멤버 변수에서 참조 중이었지만, delete_me 함수로 a를 참조중인 객체들을 추적하여 None을 대입한 결과 b객체의 'obj'에는 None이 대입

# a의 레퍼런스 카운트 확인
# reference count 4가 출력된 이유 : Gabage Collection이 아직 불필요한 오브젝트를 지우는 작업을 수행하지 못했기 때문이다.
# gc.collect() 명령으로 그 작업을 수행 => reference count는 2가 되었음을 확인 => del(a)명령으로 a객체를 지울 수 있다.
