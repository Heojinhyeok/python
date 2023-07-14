import time

love = 'too many'

content = f'''
Hello World!!
I love python {love}.
Everyone loves python.
'''
# 파일 생성
file = 'text.txt'
fd = open(file, 'wt')
fd.write(content)
fd.close()

# 파일 읽기
fd2 = open(file)
print(fd2)
