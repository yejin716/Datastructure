
#재귀함수 호출횟수와 결과 값
##함수 
def addNumber(num, count=0):
    if num == 1:
        return 1 , count +1 
    result, count = addNumber(num-1, count+1)
    return num + result, count


#변수
result, count = addNumber(100)
print("재귀함수 호출 횟수:", count)
print("결과:", result)

### 함수
# def addNumber(num) :
#     if (num == 1) :
#         return 1
#     return num + addNumber(num-1)

# ## 변수
# print(addNumber(100))