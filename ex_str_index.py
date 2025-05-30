## ---------------------------------------------------------
## 문자열 str 타입 - 인덱스(Index)
## - 인덱스(Index)
##   문자열을 구성하는 문자 한 개 한 개를 식별하기 위한 번호
##   파이썬에서 자동으로 부여함 ==> 인덱싱
## - 종류
##   * 왼(앞) => 오(끝) : 0, 1, 2, ...
##   * 오(끝) => 왼(앞) :-1,-2,-3, ...
## - 특징
##   문자 한 개 원소는 2개의 인덱스를 가짐!
## ---------------------------------------------------------

msg="오늘은 좋은 날!!"
#    0 1 2 34 56789
#    - - - -- -----
#    10 9 8 76 54321

## - 전체 메시지 출력
print(msg, len(msg))

##- '날'만 출력 =>
print(msg[7], msg[-3])

##- '은'만 출력 =>
print(msg[2], msg[-8])

##- '좋'과 '!'출력 =>
print(msg[4], msg[8], msg[9])
print(msg[-6], msg[-2], msg[-1])

msg2='Happy New Year 2025! Merry Christmas~♥'
#     0         1         2         3
#     01234567890123456789012345678901234567
#            -3        -2        -1        -
#     87654321098765432109876543210987654321

# 전체 문자열 출력
print(msg2)

# '5'만 출력 => 18, -20
print(msg2[18], msg2[-20])

# '2025'만 출력 => 15, 16, 17, 18
print(msg2[15], msg2[16], msg2[17], msg2[18], sep='')
print(msg2[-23], msg2[-22], msg2[-21], msg2[-20], sep='')

# 'Christmas'만 출력 => 27, 28, 29, 30, 31, 32, 33, 34, 35
#                      27부터 35까지 27 ~ 35
print(msg2[27], msg2[28], msg2[29], msg2[30], msg2[31], msg2[32], msg2[33], msg2[34], msg2[35], sep='')