import socket
from _thread import start_new_thread


server = "10.42.171.32"
port = 5555

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.bind((server, port))
except socket.error as err:
    print(f"[-] {err}")

sock.listen(2)
print("[+] Waiting for a connection...")
print("[+] Server Started...")


def read_pos(str):
    try:
        str = str.split(",")
        return int(str[0]), int(str[1])
    except Exception as err:
        print(str)
        print("[-] Error")

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


pos = [(0, 0), (100, 100)]


def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data
            
            if not data:
                print("[-] Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print(f"[+] Received: {data}")
                print(f"[+] Sending: {reply}")

            conn.sendall(str.encode(make_pos(reply)))

        except Exception as err:
            print(f"[-] {err}")
    print("[-] Connection lost...")
    conn.close()


currentPlayer = 0
while True:
    conn, addr = sock.accept()
    print(f"[+] Connected to: {addr}")

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
