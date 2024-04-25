##함수
def openBox():
    global count
    print('Open box ~~')
    count -= 1 
    if (count==0):
        print('**Put the box **')
        return #처음 호출한 곳으로 돌아감 ! 
    openBox()
    print('Close box###')

##메인
count = 10 
openBox()