import os
helpmsg = """
Commands may be abbreviated.  Commands are:

!		    debug		mdir		sendport	site
$		    dir		    mget		put		    size
account		disconnect	mkdir		pwd		   status
append		exit		mls		    quit	   struct
delete		mdelete		proxy		send
"""


def error():
    print("?Invalid command")


def help():
    print(helpmsg)

def pwd():
    print(os.getcwd())

while True:
    cmd = input("ftp> ")

    if cmd == 'help':
        help()
    elif cmd == 'pwd':
        pwd()
    elif cmd is None:
        continue
    elif cmd == 'quit':
        break
    else:
        error()
