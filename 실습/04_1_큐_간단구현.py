##함수










##변수
SIZE = 5 
queue = [None for _ in range(SIZE)]
front = rear = -1 #초기화



##메인

#neQueue() :데이터 삽입
rear += 1 
queue[rear] = 'Jennie'

rear += 1 
queue[rear] = 'Rosé'

rear += 1 
queue[rear] = 'Lisa'

print('Exit <--', queue, '<--Entrance')

##dequeue() :데이터 추출
front += 1 
data = queue[front]
queue[front] = None
print('customer-->', data)


front += 1 
data = queue[front]
queue[front] = None
print('customer-->', data)

front += 1 
data = queue[front]
queue[front] = None
print('customer-->', data)