#함수
from random import randint, choice #랜덤으로 
def seqSearch(ary,fdata):
    pos = -1
    for i in range(len(ary)):
        if ary[i] == fdata:
            pos = i
            break
    return pos #숫자로 나옴 

##변수
dataAry = [randint(30,190) for _ in range(6)]
findData = choice(dataAry) 

##메인 
print('Arry-->', dataAry)
position = seqSearch(dataAry,findData)
if(position != -1):
    print(findData,'is in',position)
else:
    print('Not here',findData)