##함수
def isStackFull(): #스택이 가득 찼는가 (오버플로우)
    global SIZE, stack, top
    if (top == SIZE-1): #맨 끝에 있는가 
        return True
    else:
        return False



def push(data):
    global SIZE, stack, top #전역변수
    if (isStackFull()):
        print('full stack')
    else:
        top += 1 
        stack[top] = data

def isStackEmpty(): #스택이 비어있는가
    global SIZE, stack, top
    if (top == -1):
        return True
    else:
        return False

def pop():
    global SIZE, stack, top
    if (isStackEmpty()):
        print("Empty stack!")
        return 
    else:
        data = stack[top]  #honeytea
        stack[top] = None
        top -= 1 
        return data
    
def peek(): #다음에 나올 데이터 확인
    global SIZE, stack, top
    if (isStackEmpty()):
        print("Empty stack!")
        return
    return stack[top]



##변수
SIZE = 5 # 스택크기
stack = [None for _ in range(SIZE)] #비어있는 스택 생성
top = - 1 


##메인
push('coffee')
push('greentea')
push('honeytea')
# push('cola')
# push('fanta')
print('floor:', stack)
# push('milktea')
# print('floor:', stack)

retData = pop()
print('pop -->',retData)

print('Next time-->', peek())

retData = pop()
print('pop -->',retData)

retData = pop()
print('pop -->',retData)
print('floor:', stack)
