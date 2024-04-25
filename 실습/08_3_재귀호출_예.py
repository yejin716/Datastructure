#숫자 합계 내기 ( 1~10까지 합계)
#반복문을 이용한 구현 
"""
sum = 0
for i in range(0,11):
    sum += i 
    
print("결과: ", sum)

#재귀 함수로 구현

def sumValue(n):
    if n <= 1 :
        return 1
    return n + sumValue(n-1)

print(sumValue(10))
"""

#-------------------------------------------------------

#우주선 발사 카운트 다운 
"""
def countdown(n):
    if n == 0 :
        print("발사!")
    else:
        print(n)
        countdown(n-1)

countdown(5)
"""

#-------------------------------------------------------
#별 모양 출력 
"""
def starcount(n):
    if n > 0 :
        starcount(n-1)
        print("*" * n)
starcount(5)
"""