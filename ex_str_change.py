# ----------------------------------------------
# 문자열 str 데이터 타입
# - 인덱스와 슬라이싱 활용
# ----------------------------------------------
## [인덱스] 원소/요소 읽기/추출-------------------
msg="Pithon"
#    012345

print('msg'   , msg, id(msg))
print('msg[0]', msg[0], id(msg[0]))
print('msg[1]', msg[1], id(msg[1]))

## 1번 원소의 'i' ==> 'y' 변경 <= 불가기능능
# msg[1]='y'

## -> 문자열의 원소들을 분리해서 연결
print(msg[0])
print(msg[0]+'y')  # str+str => 연결
print(msg[0]+'y'+msg[2:])  # str+str+str => 연결

#   'P'+'y'+'thon'
msg=msg[0]+'y'+msg[2:]
print(msg)