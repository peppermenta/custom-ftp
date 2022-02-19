from rdt_socket import rdt_socket
import os

HOME_DIR = os.path.join(os.path.dirname(__file__),'../')

REC_PORT_NUMBER = 8113
SER_PORT_NUMBER = 8114

DATA_SIZE = 128
data_file = open(os.path.join(HOME_DIR,'data','data.txt'), 'rb')
text = data_file.read()
data_file.close()
bytes_remaining = len(text)
transmission_rate = 5
total_packets = int(bytes_remaining/DATA_SIZE) + 1

send_socket = rdt_socket('localhost', SER_PORT_NUMBER, 5.0)
_,header_fields = send_socket.recv()
mode = header_fields["mode"]

print("MODE = ", mode)

if(mode == 0):
  data = str(total_packets) + "," + str(transmission_rate)
  send_socket.send(data, 'localhost', REC_PORT_NUMBER, 0, 0)


packet_tracker = []
while True:
  interval, header_file = send_socket.recv()
  # print(interval)
  interval = interval.split(',')
  if(interval[0] == ''):
    interval.pop(0)
  # print(type(interval))
  # print(interval)
  for packet_num in interval:
    
    chunk_size = min(DATA_SIZE, bytes_remaining)
    packet_num = int(packet_num)
    if packet_tracker.count(packet_num) == 0:
      packet_tracker.append(packet_tracker)
      bytes_remaining -= chunk_size

    # data = text[:chunk_size]
    # text = text[chunk_size:]
    data = text[packet_num * chunk_size : (packet_num + 1) * chunk_size ]

    send_socket.send(data, 'localhost', REC_PORT_NUMBER, 1, packet_num)
    print(bytes_remaining)
  if bytes_remaining == 0:
    break
  print('Data sent')
  # print(bytes_remaining)
send_socket.send('\n', 'localhost', REC_PORT_NUMBER, 0, 0)
send_socket.udp_socket.close()