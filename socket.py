# Module
import socket

# Variable

# Function

def main():
    s = socket.socket()
    s.connect(('192.168.10.10', 7979))
    s.send(b'hello world\n')
    data = s.recv(1024)
    print(f"Received {data!r}")


if __name__ == '__main__':
    main()