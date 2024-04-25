##함수
def isQueueFull():
    global SIZE, queue,front,rear
    if (rear == SIZE - 1):
        return True
    else:
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

enQueue('Rami') #full stack 
print('Exit <--', queue, '<--Entrance')

retData = deQueue()
print('Come Customer:', retData)

print('Ready!:', peek())

retData = deQueue()
print('Come Customer:', retData)


print('Exit <--', queue, '<--Entrance')

retData = deQueue()
print('Come Customer:', retData)

enQueue('Noa') #rear이 맨 뒤에 있어서 

