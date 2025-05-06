# 문자열 사용하기
# 작은 따옴표 사용
hello = 'Hello, world!'
print(hello)

hello = '안녕하세요'
print(hello)

# 큰 따옴표 사용
hello = "Hello, world!"
print(hello)

# 작은 따옴표 3개로 묶거나 큰 따옴표 3개로 묶기
hello = '''Hello, Python!'''
print(hello)

python = """Python Programming"""
print(python)

# 여러 줄로 된 문자열 사용하기
hello='''Hello, world!
안녕하세요.
Python입니다.'''
print(hello)

# 문자열 안에 작은따옴표나 큰따옴표 포함하기
s = "Python isn't difficult"
print(s)

# 문자열 안에 큰따옴표를 넣고 싶을 때 문자열을 작은따옴표로 묶기
s = 'He said "Python is easy"'
print(s)

single_quote= '''"안녕하세요.
'파이썬'입니다.'''

double_quote1 = """"Hello"
'Python'""" 

double_quote2 = """Hello, 'Python'""" # 한 줄로 작성

print(single_quote)
print(double_quote1)
print(double_quote2)

# 문자열에 따옴표를 포함하는 다른 방법 (역슬래시 \ 사용)
print('Python isn\'t difficult')
print("He said \"Python is easy\"")

# 따옴표 세 개로 묶지 않고 여러 줄로 된 문자열 사용하기
print('Hello\nPython')

print('''Hello
Python''')

print('Hello, world!')

# 9.3) 연습문제: 여러 줄로 된 문자열 사용하기
s = '''Python is a programming language that lets you work quickly
and
integrate systems more effectively.'''
print(s)

s = """Python is a programming language that lets you work quickly
and
integrate systems more effectively."""
print(s)

# 9.4) 심사문제: 여러 줄로 된 문자열 사용하기

s = '''\'Python' is a \"programming language"
that lets you work quickly
and
integrate systems more effectively.'''

print(s)

s = ''''Python' is a "programming language"
that lets you work quickly
and
integrate systems more effectively.'''

print(s)

s = """\'Python' is a \"programming language"
that lets you work quickly
and
integrate systems more effectively."""

print(s)

s = """'Python' is a "programming language"
that lets you work quickly
and
integrate systems more effectively."""

print(s)