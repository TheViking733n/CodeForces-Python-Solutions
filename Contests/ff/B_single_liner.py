[print((lambda l,s:int('1'*(l+1))-int(s) if s[0]=='9' else int('9'*l)-int(s))(int(input()),input())) for i in range(int(input()))]