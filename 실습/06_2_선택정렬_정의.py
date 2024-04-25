##함수
from random import randint #랜덤으로 

def findMinIndex(ary):
    minIdx = 0
    for i in range(1,len(ary)): #1~3까지 반복
        if (ary[minIdx] > ary[i]): # 55가 나머지 값보다 크면 
            minIdx = i 
    return minIdx  #숫자로 나옴


##변수
before = [randint(30,190) for _ in range(8)]
after = []


##메인 
print('Sort before -->',before)
for i in range(len(before)):
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del(before[minPos])

print('Sort after -->',after)
