##함수
def findMinIndex(ary):
    minIdx = 0
    for i in range(1,len(ary)): #1~3까지 반복
        if (ary[minIdx] > ary[i]): # 55가 나머지 값보다 크면 
            minIdx = i 
    return minIdx





##변수
testAry = [55,88,33,77]




##메인
minPos = findMinIndex(testAry)
print('min-->',testAry[minPos])