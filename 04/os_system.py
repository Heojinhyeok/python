import os

# cmd = 'ls -l /nodir > /dev/null 2>&1'
cmd = 'ls -l /tmp >/dev/null 2>&1'
ret = os.system(cmd)
if ret == 0:
    print('[  OK  ] The command complete.')
else:
    print('[ FAIL ] The command not complete.')
