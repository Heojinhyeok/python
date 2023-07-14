jjang = '09'
jjang = 'handsome guy'

def ban(n):
    global jjang
    jjang = '07'
    print('%d 반 짱: %s' % (n, jjang))

ban(3)
print('전체장:', jjang)