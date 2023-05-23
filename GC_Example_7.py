# Reference Cycle를 생성하고 수동으로 GC를 실행

import sys, gc

def make_cycle():
    l = {}
    l[0] = l

def main():
    collected = gc.collect()
    print(collected)

    for i in range(10):
        make_cycle()

    collected = gc.collect()

    print(collected)


if __name__ == "__main__":
    ret = main()
    sys.exit(ret)
    
# 수동으로 GC를 수행하는 방법 : Time-based, Event-based
# ① Time-based : Time-based GC는 단순, 고정된 시간 간격으로 GC가 실행
# ② Event-based : Event-based GC는 event 발생시 GC가 호출
