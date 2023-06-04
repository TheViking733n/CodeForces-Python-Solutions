from gzip import compress, decompress

f = open('D_Another_Problem_About_Dividing_Numbers.py', 'r')

code = f.read().encode('ascii')
f.close()

code = compress(code)

target = '''kwargs.pop("end", "
"))'''
ok = '''kwargs.pop("end", "\n"))'''

# exec(decompress(code).decode('ascii'))

from pyperclip import copy

copy(f"from gzip import decompress; exec(decompress({code}).decode('ascii'))")