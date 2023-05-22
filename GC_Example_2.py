# 참조중인 객체 del 실행하기

class A:
    def __del__(self):
        print("deleted")

a = A()
b = a

del(a)

# 실행결과 => delete라는 메시지를 출력하지 않는다.
# b라는 변수에서 a를 참조중이기 때문에 a라는 객체가 메모리에서 지워지지 않았다.
