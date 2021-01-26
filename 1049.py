a,b=input().split()

x=int(a)
y=int(b)
z=int(x>y)

print(z)

"""
a가 b보다 큰 경우 1을, 그렇지 않은 경우 0을 출력한다.

모범 답안)
z=int(x>y) x>y일 경우 1, 그 외는 0이 z에 담기게 함

내풀이)
a,b = input().split()
a = int(a)
b = int(b)

if(a>b):
    print("1")
else:
    print("0")
"""
