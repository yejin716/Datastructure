##함수
class Node() :
    def __init__(self):
        self.data = None
        self.link = None
#데이터 출력 
def printNodes(start):
    current = start
    print(current.data, end=' ') 
    while (current.link != None): 
        current = current.link
        print(current.data , end = ' ')
    print()

#데이터 삽입
def insertNode(findData, insertData):
    global memory, head, pre, current
    #case 1 : 헤드 앞에 삽입  (다현, 화사)
    if (findData == head.data):
        node = Node()
        node.data = insertData #빈노드에 화사입력
        node.link = head #화사링크와 헤드연결 
        head = node #헤드노드를 새노드로 지정 
        return 
    
    #case 2 : 중간 노드 앞에 삽입 (사나, 솔라)
    current = head 
    while (current.link != None):
        pre = current #현재노드를 이전노드로 지정 
        current = current.link #현재노드는 다음 노드로 이동 
        if (current.data == findData):
            node = Node()
            node.data = insertData #솔라 삽입 
            node.link = current #솔라링크를 현재노드에 연결
            pre.link = node #이전노드와 솔라노드 연결 
            return
        
    #case 3 : 마지막 노드에 삽입(없는 노드앞에 삽입) ('나연','문별)
    node = Node()
    node.data = insertData
    current.link = node 
    return 

#데이터 삭제
def deleteNode(delData):
    global memory, head, pre, current
    #case 1 : head를 삭제 (다현 삭제)
    if (delData == head.data):
        current = head
        head = head.link #헤드는 다음 헤드노드로 이동 
        del(current)
        return
    
    #case 2 : 중간 노드 삭제 (쯔위 삭제)
    current = head 
    while (current.link != None):
        pre = current
        current = current.link
        if (current.data == delData):
            pre.link = current.link 
            del(current)
            return
        
    #case 3 : 없는 노드를 삭제 (예진)
    return 

#데이터 찾기
def findNode(findData):
    global memory, head, pre, current
    current = head
    if (findData == current.data):
        return current
    while (current.link != None):
        current = current.link #현재노드는 다음 노드로 이동 
        if(findData == current.data):
            return current
    return Node()

##변수
memory = []
head, current, pre = None,None,None
dataArray = ['아현','라미','치키타','파리타','루카'] #데이터! 



##메인
#첫번째 노드 정보 입력 
node = Node()
node.data = dataArray[0] #아현 
head = node
memory.append(node) #(생략가능)

#두번째 노드 이후 코드~ 
for data in dataArray[1:]: #[]'라미','치키타',...]
    pre = node
    node = Node() #빈 노드 생성 
    node.data = data #데이터를 생성된 빈 노드에 삽입 
    pre.link = node #노드를 전의 노드와 링크연결 
    # memory.append(node) 

printNodes(head)

#헤드앞에 삽입
# insertNode('아현','화사')
# printNodes(head)

#중간 노드 삽입 
# insertNode('치키타','솔라')
# printNodes(head)

#마지막 노드 삽입
# insertNode('로라','문별')
# printNodes(head)

#헤드 삭제
# deleteNode('아현')
# printNodes(head)

#첫번째 외 노드삭제
# deleteNode('루카')
# printNodes(head)

#노드 검색 
retNode = findNode('치키타')
print(retNode.data, "의 뮤비가 플레이 됩니다.")




