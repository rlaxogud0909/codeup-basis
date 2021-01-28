a,b=input().split()

x=int(a)
y=int(b)
b1=bool(x)
b2=bool(y)
z=int((not b1) and (not b2))

print(z)
"""
둘 다 거짓일 경우에만 1을 출력하고, 그 외의 경우에는 0을 출력한다.
내풀이)
a,b = input().split()
a = int(a)
b = int(b)

if a==0 and b==0:
    print("1")
else:
    print("0")
"""
