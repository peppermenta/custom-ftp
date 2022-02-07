from rdt_socket import rdt_send_socket

# def send_file():
  # pass
PORT_NUMBER = 8080
send_socket = rdt_send_socket()
data = 'hello'
send_socket.send(data, 'localhost', PORT_NUMBER)
print('Data sent')