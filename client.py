import socket
import threading

nickname = input("choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#SOCK_STREAM connects through TCP

client.connect(("127.0.0.1", 9999))
#yeah this is the ip and port you connect here 

def receive():
    while True:
        try:
            message = client.recv(1024).decode("ascii")
            if message == "NICK":
                client.send(nickname.encode("ascii"))
                pass
            else:
                print(message)
        except:
            print("[Disconnected from server!]")
            client.close()
            break

def write():
    while True:
        message = f"{nickname}: {input("")}"
        client.send(message.encode("ascii"))

recieve_thread = threading.Thread(target=receive)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

print("Press enter")