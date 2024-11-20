import socket, threading

host = '192.168.0.101'
port = 7977

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def private_message(sender, recipient_name, message):
    try:
        index = nicknames.index(recipient_name)
        recipient = clients[index]
        private_message = f"(private) {sender}: {message}"
        recipient.send(private_message.encode('ascii'))
    except ValueError:
        sender.send("User not found.".encode('ascii'))

def handle(client):
    while True:
        try:
            message = client.recv(1024).decode('ascii')  # Receive message from client
            if message.lower() == '/sair':  # Check if the message is "/sair"
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                broadcast(f'{nickname} left!'.encode('ascii'))  # Notify others
                nicknames.remove(nickname)
                break
            elif message.lower().startswith('/private:'):
                parts = message.split(" ", 2)
                if len(parts) == 3:
                    recipient_name = parts[1]
                    private_message(client, recipient_name, parts[2])  # Send private message
                else:
                    client.send("Incorrect private message format.".encode('ascii'))
            else:
                broadcast(message.encode('ascii'))  # Broadcast regular message
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left due to an error!'.encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")
        client.send('NICKNAME'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        print(f"Nickname is {nickname}")
        broadcast(f"{nickname} joined!".encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
