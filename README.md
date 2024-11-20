# Chat Application - README.txt

## Descrição

Este é um aplicativo de chat simples em Python usando sockets e threads, permitindo comunicação em tempo real entre vários clientes. O servidor suporta mensagens públicas e privadas entre os participantes conectados.

## Funcionalidades

1. **Conexão com o servidor**:

   - Os clientes podem se conectar ao servidor através do endereço IP e porta especificados.
   - O cliente precisa escolher um apelido (nickname) único para se identificar no chat.

2. **Mensagens Públicas**:

   - Qualquer mensagem enviada por um cliente será exibida para todos os outros clientes conectados.
   - O formato da mensagem é: `nickname: mensagem`.

3. **Mensagens Privadas**:

   - Os clientes podem enviar mensagens privadas para outros usuários.
   - A sintaxe para enviar uma mensagem privada é: `/private: recipient_name mensagem`.
   - O destinatário e o remetente receberão a mensagem privada no formato:
     - `(private) sender_name: mensagem` para o destinatário.
     - `(private) You -> recipient_name: mensagem` para o remetente.

4. **Desconexão**:

   - Para sair do chat, o cliente pode digitar o comando `/sair`.
   - Ao desconectar, o servidor notificará os outros clientes sobre a saída do usuário.

5. **Mensagens de Erro**:
   - Se o destinatário de uma mensagem privada não for encontrado, o remetente será informado com a mensagem "User not found".
   - O servidor lida com erros de conexão e notifica o cliente sobre problemas ocorridos.

## Como Usar

### 1. Configuração do Servidor

- O servidor deve ser iniciado primeiro.
- O servidor escuta na porta 7976 (pode ser alterada se necessário).
- O servidor aceita múltiplos clientes e gerencia mensagens públicas e privadas.

### 2. Configuração do Cliente

- O cliente conecta-se ao servidor especificando o endereço IP e a porta.
- O cliente escolhe um apelido único na inicialização.
- Após a conexão, o cliente pode começar a enviar mensagens públicas e privadas, além de sair do chat.

## Requisitos Técnicos

- **Python 3.x**: O código foi desenvolvido para ser executado em Python 3.
- **Bibliotecas**:
  - `socket`: Para comunicação de rede via sockets.
  - `threading`: Para gerenciar múltiplas conexões de forma assíncrona.

## Como Rodar

### No Servidor:

1. Execute o script do servidor:
   ```
   python server.py
   ```
2. O servidor ficará aguardando conexões na porta 7976.

### No Cliente:

1. Execute o script do cliente:
   ```
   python client.py
   ```
2. O cliente irá pedir um apelido e, após a conexão, poderá começar a enviar mensagens.

## Notas

- Certifique-se de que o servidor e os clientes estão na mesma rede local ou que a máquina do servidor seja acessível pela rede.
- O servidor pode ser executado em um host específico, e o cliente deve se conectar a esse endereço IP.

## Possíveis Melhorias

- Implementar autenticação de usuários.
- Armazenar logs de mensagens.
- Suporte a comandos adicionais, como mudar de apelido.
