from rdt_socket import rdt_recv_socket

# def recv_file():
  # pass

PORT_NUMBER = 8080
recv_socket = rdt_recv_socket('localhost', PORT_NUMBER)
print('Listening for message at port', PORT_NUMBER)
data, header_fields = recv_socket.recv()
print(header_fields)
print(data)