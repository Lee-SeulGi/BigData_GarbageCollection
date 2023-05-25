# 2. 가비지 컬렉션 (Garbage Collection)

## 📌 가비지 컬렉션이란?
프로그램을 개발하다 보면 유효하지 않은 메모리인 가바지 (Garbage)가 발생한다. C언어의 경우 개발자가 malloc() ,free()라는 함수를 통해 직접 메모리를 해제해주어야 한다. 가비지 컬렉션 (Garbage Collection)이란 프로그램이 동적으로 할당했던 메모리 영역 중에서 필요없게 된 영역(Garbage)을 해제하는 기능이다.

## 📌 GC (Garbage Collection)의 장점?
1. 유효하지 않은 포인터 접근 방지 : 이미 해제가 된 메모리 영역에 접근하는 것을 방지
2. 이중 해제 방지 : 이미 해제된 메모리를 다시 해제하는 버그 방지
3. 메모리 누수 방지 : 더 이상 필요하지 않은 메모리가 해제되지 않고 계속 메모리에 남아있는 버그 방지 (이 현상이 심해지면 메모리 고갈로 프로그램 강제 종료 가능)

## 📌 GC (Garbage Collection)의 단점?
1. 어떤 메모리를 해제하고 언제 해제할지 결정해야 하고 이에 대한 메모리가 소요된다.
2. GC를 언제 실행시킬지 예측이 어렵다.
3. 당된 메모리가 해제되는 시점을 알 수 없다.

## 📌 Python에서의 GC (Garbage Collection)란?
파이썬에선 기본적으로 참조 횟수가 0이 된 객체를 메모리에서 해제하는 레퍼런스 카운팅 방식을 사용한다. 하지만 참조 횟수가 0은 아니지만 도달할 수 없지만, 상태인 reference cycles(순환 참조)가 발생했을 때는 별도의 알고리즘을 통해 상황을 해결한다.

### 1. 레퍼런스 카운팅
- 모든 객체는 참조 당할 때 레퍼런스 카운터를 증가시키고 참조가 없어질 때 카운터를 감소시킨다. 이 카운터가 0이 되면 객체가 메모리에서 해제한다. 어떤 객체의 레퍼런스 카운트를 보고 싶다면 sys.getrefcount()로 확인할 수 있다.
<pre><code>>>> import sys
>>> a = 'inha'
>>> sys.getrefcount(a)
2
</code></pre>
>참조 횟수가 2인 이유 : 첫 번째는 variable을 생성하는 것이고, 두 번째는 변수 a를 sys.getrefcount() 함수에 전달할 때 카운트된다.

- 리스트와 딕셔너리에 객체를 추가하는 경우
<pre><code>>>> import sys
>>> a = 'inha'
>>> b = [a]
>>> c = { 'key': a }
>>> sys.getrefcount(a)
4
</code></pre>

### 2. 순환 참조
- 자기 자신을 참조하는 경우
<pre><code>>>> a = []
>>> a.append(a)
>>> del a
</code></pre>
>a의 참조 횟수는 1이지만 이 객체는 더 이상 접근할 수 없으며, 레퍼런스 카운팅 방식으로는 메모리에서 해제될 수 없다.

- 서로를 참조하는 경우
<pre><code>>>> a = Foo()   # 0x60
>>> b = Foo()   # 0xa8
>>> a.x = b   # 0x60의 x는 0xa8를 가리킨다.
>>> b.x = a   # 0xa8의 x는 0x60를 가리킨다.
# 이 시점에서 0x60의 레퍼런스 카운터는 a와 b.x로 2
# 0xa8의 레퍼런스 카운터는 b와 a.x로 2다.
>>> del a   # 0x60은 1로 감소한다. 0xa8은 b와 0x60.x로 2다.
>>> del b   # 0xa8도 1로 감소한다.
</code></pre>
>이 상태에서 0x60.x와 0xa8.x가 서로를 참조하고 있기 때문에 레퍼런스 카운트는 둘 다 1이지만 도달할 수 없는 가비지가 된다.