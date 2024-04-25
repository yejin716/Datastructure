## 함수
class Node() :
    def __init__(self):
        self.data = None
        self.link = None
## 변수
## 메인

node1 = Node()
node1.data = '아현'

node2 = Node()
node2.data = '루카'
node1.link = node2

node3 = Node()
node3.data = '치키타'
node2.link = node3

node4 = Node()
node4.data = '파리타'
node3.link = node4

node5 = Node()
node5.data = '라미'
node4.link = node5

# #데이터 삽입
# newNode = Node()
# newNode.data = '예진'
# newNode.link = node2.link #링크 복사 
# node2.link = newNode #링크 연결 

#데이터 삭제 
node2.link = node3.link #쯔위 링크를 정연 링크로 복사
del(node3) #쯔위삭제 



#각 노드 데이터 출력
# print(node1.data, end=' ')
# print(node1.link.data, end=' ')
# print(node1.link.link.data, end=' ')
# print(node1.link.link.link.data, end=' ')
# print(node1.link.link.link.link.data, end=' ')

current = node1
print(current.data, end=' ') #다연
while (current.link != None): 
    current = current.link
    print(current.data , end = ' ')
print()