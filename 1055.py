a,b=input().split()

x=int(a)
y=int(b)
b1=bool(x)
b2=bool(y)
z=int(b1 or b2)

print(z)

"""
하나라도 참일 경우 1을 출력하고, 그 외의 경우에는 0을 출력한다.
내풀이)
a,b = input().split()
a = int(a)
b = int(b)
z = int(a|b)
print(z)
"""
