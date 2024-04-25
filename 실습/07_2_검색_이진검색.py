#함수
from random import randint, choice #랜덤으로 
def binSearch(ary,fdata):
    global count
    pos = -1
    start = 0 
    end = len(ary) -1 # 9 

    while (start <= end):
        count += 1 
        mid = (start+end) // 2 #몫
        if (ary[mid] == fdata):
            pos = mid
            break

        elif (ary[mid] < fdata):
            start = mid + 1 
        else:   
            end = mid - 1 

    return pos
    

##변수
count = 0
dataAry = [randint(0,100000) for _ in range(100000)]
dataAry.sort()
findData = choice(dataAry) 
# findData = 77 #77은 없어요

##메인 
print('Arry-->', dataAry[:20])
position = binSearch(dataAry,findData)
if(position != -1):
    print(findData,'is in',position,'count:',count)
else:
    print('Not here',findData)