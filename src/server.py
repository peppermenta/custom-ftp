from rdt_socket import rdt_socket
import os

HOME_DIR = os.path.join(os.path.dirname(__file__),'../')

REC_PORT_NUMBER = 8083
SER_PORT_NUMBER = 8084

DATA_SIZE = 128
data_file = open(os.path.join(HOME_DIR,'data','data.txt'), 'r')
text = data_file.read()
data_file.close()
bytes_remaining = len(text)
# def send_file():
  # pass
send_socket = rdt_socket('localhost', SER_PORT_NUMBER, 2.0)
while bytes_remaining > 0:
  chunk_size = min(DATA_SIZE, bytes_remaining)
  data = text[:chunk_size]
  text = text[chunk_size:]
  bytes_remaining -= chunk_size
  send_socket.send(data, 'localhost', REC_PORT_NUMBER, 0, 0)
  print('Data sent')
send_socket.send('\n', 'localhost', REC_PORT_NUMBER, 1, 0)
send_socket.udp_socket.close()