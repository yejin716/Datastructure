##함수 선언 부분
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

##전역 변수 선언
katok  =[]
select = -1 


##메인 

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

if __name__ == "__main__":

    while (select != 4):
        select = int(input("선택하세요(1:추가, 2:삽입, 3:삭제, 4:종료)-->"))

        if (select == 1):
            data = input("추가할 데이터 -->")
            add_data(data)
            print(katok)

        elif (select == 2):
            pos = int(input("삽입할 위치 -->"))
            insert_data(pos, data)
            print(katok)

        elif (select == 3):
            pos = int(input("삭제할 위치 -->"))
            delete_data(pos)
            print(katok)
        elif (select == 4):
            print(katok)

            exit

        else:
            print("1~4 중 하나를 입력하세요.")
            continue


            

