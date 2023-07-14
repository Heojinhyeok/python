def say_myself(name, old, man=True):
    print("이름은 %s 입니다." % name)
    print("나이는 %d 살입니다." % old)
    if man:
        print("남자입니다.\n")
    else:
        print("여자입니다.\n")

say_myself("chan", 13)
say_myself("chan", 13, True)
say_myself("chan", 13, False)
