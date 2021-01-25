a,b,c=input().split('.')

print('%04d' % int(a), end='.')
print('%02d' % int(b), end='.')
print('%02d' % int(c))

"""
입력받은 연, 월, 일을 yyyy.mm.dd 형식으로 출력한다.
(%02d를 사용하면 2칸을 사용해 출력하는데, 한 자리 수인 경우 앞에 0을 붙여 출력한다.)
"""
