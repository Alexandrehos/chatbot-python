#Coded by Yashraj Singh Chouhan
import socket, threading
nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      #socket initialization
client.connect(('192.168.0.101', 7977))                             #connecting client to server

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            else:
                if message.startswith("(private)"):
                    print(f"Private message received: {message}")
                else:
                    print(message)
        except:
            print("An error occurred!")
            client.close()
            break

def write():
    while True:
        message = input('')
        if message.lower() == '/sair':
            client.send(message.encode('ascii'))
            break
        elif message.lower().startswith('/private:'):
            client.send(message.encode('ascii'))
        else:
            message = f'{nickname}: {message}'
            client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)               #receiving multiple messages
receive_thread.start()
write_thread = threading.Thread(target=write)                   #sending messages 
write_thread.start()