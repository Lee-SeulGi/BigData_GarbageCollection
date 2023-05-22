# del 객체 지워보기
# a라는 객체를 만들고 del(a)를 하면 객체가 메모리에서 지워짐과 동시에 delete라는 메시지를 출력

class A:
    def __del__(self):
        print("deleted")

a = A()
del(a)

# 실행결과 => deleted
