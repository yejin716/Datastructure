##함수
def isQueueFull():
    global SIZE, queue,front,rear
    
    if ((rear+1) % SIZE == front):  
        return True
    else:
        return False



def enQueue(data):
    global SIZE, queue,front,rear
    if (isQueueFull()):
        print("Full Queue!")
        return
    rear =(rear + 1) % SIZE 
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
    front = (front + 1 ) % SIZE
    data = queue[front]
    queue[front] = None
    print('customer-->', data)

def peek():
    global SIZE, queue,front,rear
    if (isQueueEmpty()):
        print("Empty Queue")
        return
    return queue[(front+1) % SIZE]



##변수
SIZE = 5 
queue = [None for _ in range(SIZE)]
front = rear = 0 #초기화


##메인

enQueue('Jennie')
enQueue('Rosé')
enQueue('Lisa')
enQueue('Jisoo')

print('Exit <--', queue, '<--Entrance')

# enQueue('Rami') #full stack 
# print('Exit <--', queue, '<--Entrance')

retData = deQueue()
print('Come Customer:', retData)
print('Exit <--', queue, '<--Entrance')

retData = deQueue()
print('Come Customer:', retData)
print('Exit <--', queue, '<--Entrance')


# # print('Ready!:', peek())

# retData = deQueue()
# print('Come Customer:', retData)


# print('Exit <--', queue, '<--Entrance')

enQueue('Noa') #앞으로 땡기고 rear에 넣음 
print('Exit <--', queue, '<--Entrance')

enQueue('Yejin') #앞으로 땡기고 rear에 넣음 
print('Exit <--', queue, '<--Entrance')

enQueue('Hajun') #앞으로 땡기고 rear에 넣음 
print('Exit <--', queue, '<--Entrance')


