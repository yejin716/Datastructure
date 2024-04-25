##함수 선언부

##전역 선언부
katok = ['아현','라미','치키타','파리타','루카']



##메인 코드부 

#데이터 추가 (아사에게 1회 카톡)
#1단계 : 빈칸 추가 
katok.append(None)
#2단계 : 마지막 칸에 새 친구 입력
katok[5] = '아사'
print(katok)

#데이터 삽입 (로라에게 연속 40회 카톡 == 로라를 3등으로)
#1단계 : 빈칸 추가
katok.append(None)
#2단계 : 한칸씩 뒤로 이동
katok[6] = katok[5] #루카
katok[5] = None
katok[5] = katok[4] #파리타
katok[4] = None
katok[4] = katok[3] #치키타
katok[3] = None
#3단계 : 3등자리에 로라 입력
katok[3] = '로라'
print(katok)

#데이터 삭제(루카가 카톡 차단 == 4등을 삭제)
#1단계 : 데이터 지우기 
katok[4] = None
#2단계 : 한칸씩 앞으로 이동 (지운 다음 칸부터 마지막까지)
katok[4] = katok[5] 
katok[5] = None
katok[5] = katok[6] 
katok[6] = None
#3단계 : 마지막 칸을 제거
del(katok[6])
print(katok)

