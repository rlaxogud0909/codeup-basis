a=input()

x=int(a)
b=bool(x)
x=int(not b)

print(x)

"""
입력된 값이 0이면 1, 1이면 0을 출력한다.

bool() 함수을 이용하여 자료형의 참과 거짓을 식별할 수 있다
bool(x)
1. x가 빈문자열이면 false
   x가 빈문자열이 아니면 true
2. x가 0이면 false
   x가 0이 아니면 true

not은 논리NOT연산으로서 논리 상태를 반전
"""
