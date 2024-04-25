##함수

##변수
stack = [None,None,None,None,None]
top = -1

##메인


##push
top += 1 
stack[top] = 'coffee'

top +=1
stack[top] ='greentea'

top += 1 
stack[top] = 'honeytea'

print('floor: ',stack)

#pop
data = stack[top]  #honeytea
stack[top] = None
top -= 1 
print("pop -->", data)

data = stack[top] #greentea
stack[top] = None
top -= 1 
print("pop -->", data)

data = stack[top] #coffee
stack[top] = None
top -= 1 
print("pop -->", data)
