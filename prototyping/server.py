import socket
import pickle

from _thread import start_new_thread
from player import Player

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

players = [Player(0,0,50,50, (255,0,0)), Player(100,100, 50, 50, (0,255,0))]

def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data
            
            if not data:
                print("[-] Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print(f"[+] Received: {data}")
                print(f"[+] Sending: {reply}")

            conn.sendall(pickle.dumps(reply))

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
