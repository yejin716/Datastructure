##함수
def isQueueFull():
    global SIZE, queue,front,rear
    
    if (rear != SIZE-1):  #case 1 : rear뒤에 여유가 있는 상태
        return False
    elif (rear == SIZE-1 and front == -1): #case 2 : 다 참 
        return True 
    elif (rear == SIZE-1 and front != -1): #case 3 : rear은 끝이지만 앞에 여유가 있음
        for i in range(front+1,SIZE, 1):
            queue[i-1] = queue[i]
            queue[i] = None 
        front -= 1 
        rear -= 1
        return False 



def enQueue(data):
    global SIZE, queue,front,rear
    if (isQueueFull()):
        print("Full Queue!")
        return
    rear += 1 
    queue[rear] = data   

def isQueueEmpty():
    global SIZE, queue,front,rear
    if (front == rear):
        return True
    else:
        return False 

def deQueue():
    global SIZE, queue,front,rear
    if (isQueueEmpty()):
        print("Empty Queue")
        return
    front += 1 
    data = queue[front]
    queue[front] = None
    print('customer-->', data)

def peek():
    global SIZE, queue,front,rear
    if (isQueueEmpty()):
        print("Empty Queue")
        return
    return queue[front+1]



##변수
SIZE = 5 
queue = [None for _ in range(SIZE)]
front = rear = -1 #초기화


##메인

enQueue('Jennie')
enQueue('Rosé')
enQueue('Lisa')
enQueue('Jisoo')
enQueue('Yejin')
print('Exit <--', queue, '<--Entrance')

# enQueue('Rami') #full stack 
# print('Exit <--', queue, '<--Entrance')

retData = deQueue()
print('Come Customer:', retData)

# print('Ready!:', peek())

retData = deQueue()
print('Come Customer:', retData)


print('Exit <--', queue, '<--Entrance')

enQueue('Noa') #앞으로 땡기고 rear에 넣음 
print('Exit <--', queue, '<--Entrance')


