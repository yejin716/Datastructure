##함수
from random import randint #랜덤으로 
def selectSort(ary):
    n = len(ary) #전체 데이터 개수 6개
    for i in range(0,n-1): #사이클(큰 회전)
        minIdx = i
        for j in range(i+1,n):
            if (ary[minIdx]> ary[j]):
                minIdx = j 
        ary[i], ary[minIdx] = ary[minIdx],ary[i] #서로 자리 바꿈 
    return ary



##변수
dataAry = [randint(30,190) for _ in range(6)]


##메인 
print('Sort before -->',dataAry)
dataAry = selectSort(dataAry)


print('Sort after -->',dataAry)
