y,m,d=input().split('.')

print('%02d' % int(d), end='-')
print('%02d' % int(m), end='-')
print('%04d' % int(y))

"""
년월일을 일월년으로 바꾸어 '-'(대쉬, 마이너스)로 구분해 출력한다.

내풀이:
y,m,d = input().split('.')
print(d+"-"+m+"-"+y)
"""
