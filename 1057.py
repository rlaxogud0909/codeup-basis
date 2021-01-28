a,b=input().split()
x=int(a)
y=int(b)
b1=bool(x)
b2=bool(y)
z=int(b1 == b2)

print(z)
"""
참/거짓이 서로 같을 때에만 1을 출력하고, 그 외의 경우에는 0을 출력한다.
내풀이)
a, b = input().split()
a = int(a)
b = int(b)

if a==b:
    print("1")
else:
    print("0")
"""
