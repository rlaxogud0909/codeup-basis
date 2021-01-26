a = ord(input())
a = a+1
a = chr(a)
print(a)

"""
영문자 1개를 입력하면 다음 문자가 출력된다.

풀이)
ord()함수로 문자를 아스키 코드 값으로 변경하고 +1해준 다음
chr()함수로 다시 아스키 코드 값을 문자로 바꿔준다.

모범답안)
a=input()
n=ord(a)
c=chr(n+1)
print(c)
"""
