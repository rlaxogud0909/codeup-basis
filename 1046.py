a,b,c=input().split()
x=int(a)
y=int(b)
z=int(c)

print(x+y+z)
print('%.1f' % ((x+y+z)/3))

"""
정수 3개 입력
합과 평균을 줄을 바꿔 출력한다.
평균은 소수점 이하 둘째 자리에서 반올림해서 소수점 이하 첫째 자리까지 출력한다.

내풀이)
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
v = a+b+c
print(v)
print("%.1f" % (v/3))
"""
