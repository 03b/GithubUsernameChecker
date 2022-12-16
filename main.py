#  github.com/03B | made with hate
#  12-15-22 // Please credit me if you use this in a program/product of yours, thanks
import ssl, socket, threading

THREAD_CAP = int(input("Max thread count:"))
usernameFile = open("usernames.txt").read().splitlines()
usernames = iter(usernameFile)

def checkName(username):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_sock = ssl.create_default_context().wrap_socket(s, server_hostname="github.com")
    ssl_sock.connect(("github.com", 443))
    ssl_sock.send(
        b"GET /"
        + username.encode()
        + b" HTTP/1.1\r\nHost: github.com\r\nConnection: close\r\n\r\n"
    )
    data = ssl_sock.recv(20)
    ssl_sock.close()
    if b"HTTP/1.1 404" in data:
        print("Available, ", username)
        open("out.txt", "a").write(f"\n{username}")
    else:
        print("Taken, ", username)


while 1:
    while threading.active_count() > THREAD_CAP:
        pass
    threading.Thread(target=checkName, args=(next(usernames), )).start()

