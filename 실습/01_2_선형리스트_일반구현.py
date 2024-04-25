##함수부
#데이터 추가 함수
def add_data(friend):
    katok.append(None)
    #1단계 : 빈칸 추가

    # 선형 리스트의 길이를 파악! 
    kLen = len(katok)
    #2단계 : 마지막 칸에 데이터 입력
    katok[kLen-1] = friend

#데이터 삽입 함수
def insert_data(position, friend):
    #1단계 : 빈칸 추가 
    katok.append(None)
    kLen = len(katok)
    #2단계 : 마지막 친구부터 삽입할 위치까지 한칸씩 뒤로 이동
    for i in range(kLen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    #3단계 : 위치에 친구 입력 
    katok[position] = friend

#데이터 삭제 함수
def delete_data(position):
    #1단계 : 데이터 삭제
    katok[position] = None
    kLen = len(katok)
    #2단계 : 한칸씩 앞으로 
    for i in range(position+1, kLen, 1):
        katok[i-1] = katok[i]
        katok[i] = None
    #3단계 : 마지막 칸을 제거
    del(katok[kLen-1])


##변수부
katok = []

##메인부 
add_data('아현')
add_data('루카')
add_data('치키타')
add_data('파리타')
add_data('라미')
print(katok)
add_data('로라')
print(katok)

insert_data(3, '아사')
print(katok)

delete_data(4)
print(katok)
