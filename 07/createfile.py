import os
import sys

# variable definition
basedir = '/test'
#file = basedir + 'test.txt'
file = 'test.txt'
filename = basedir + '/' + file
data = """
반갑습니다. 
파이썬 개발자 여러분 6월부터 만으로 나이를 계산합니다.
올 한해는 행복한 가득한 한해가 되었으면 합니다.
"""
def makedir(dir):
    # input: str(basedir)
    # output:
    # functions
    # * 디렉토리가 없으면 생성한다.

    if not os.path.isdir(dir):
        os.mkdir(dir)
        print(f"[ OK ] {dir} 디렉토리가 생성 되었습니다.")

def createfile(file, c):
    # input: file(file), str(cont)
    # output:
    # functions:
    # * ....
    with open(file, 'w') as fd:
        fd.write(c)
    print(f"[ OK ] {file} 파일이 생성되었습니다.")

def readfile(file):
    # input: file(file)
    # output:
    # functions:
    print(open(file).read())

def removefile(file):
    # input: file(file)
    # output:
    # functions:
    if os.path.exists(file):
        os.remove(file)
        print('[ OK ] The file removed')
    else:
        sys.exit("[ FAIL ] Error Message below ... \nThe file does not exists. \nThen ...\nThe file can't removed.")

# main function
def main():
    # 1)디렉토리 생성
    makedir(basedir)

    # 2)파일 생성 - /test/test.txt
    createfile(filename, data)

    # 3)파일 내용 확인
    readfile(filename)

    # 4)파일 삭제
    removefile(filename)

if __name__ == '__main__':
    main()