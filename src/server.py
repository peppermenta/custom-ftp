from rdt_socket import rdt_send_socket
import os

DATA_SIZE = 128
data_file = open('data.txt', 'r')
text = data_file.read()
data_file.close()
bytes_remaining = len(text)
# def send_file():
  # pass
PORT_NUMBER = 8080
send_socket = rdt_send_socket()
while bytes_remaining > 0:
  chunk_size = min(DATA_SIZE, bytes_remaining)
  data = text[:chunk_size]
  text = text[chunk_size:]
  bytes_remaining -= chunk_size
  send_socket.send(data, 'localhost', PORT_NUMBER)
  print('Data sent')
send_socket.send('\n', 'localhost', PORT_NUMBER)