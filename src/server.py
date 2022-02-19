from rdt_socket import rdt_socket
import os

# import sys

HOME_DIR = os.path.join(os.path.dirname(__file__),'../')

REC_PORT_NUMBER = 8119
SER_PORT_NUMBER = 8120

DATA_SIZE = 10000
# data_file = open(os.path.join(HOME_DIR,'data','data.txt'), 'r')
data_file = open(os.path.join(HOME_DIR,'data','CS3543_100MB'), 'rb')
text = data_file.read()
text = str(text)
print(type(text))
length = int(len(text) / 20)
print(length)
text = text[:length]

# print(text[:1000])
# text = text[:10000]

# received_file = open(os.path.join(HOME_DIR,'data','CS3543_5k'), 'wb')
# received_file.write(str.encode(text))
# received_file.close()


# print(text)
data_file.close()
bytes_remaining = len(text)
transmission_rate = 50
total_packets = int(bytes_remaining/DATA_SIZE) + 1

last_packet_size = bytes_remaining - (total_packets - 1) * DATA_SIZE

send_socket = rdt_socket('localhost', SER_PORT_NUMBER, 0.1)
_,header_fields = send_socket.recv()
mode = header_fields["mode"]


if(mode == 0):
  data = str(total_packets) + "," + str(transmission_rate)
  send_socket.send(data, 'localhost', REC_PORT_NUMBER, 0, 0)


while True:
  try: 
    
    interval, header_file = send_socket.recv()
    interval = interval.split(',')
    
    print(interval)
    
    if(interval[0] == ''):
      interval.pop(0)
    
    for packet_num in interval:
      packet_num = int(packet_num)

      if packet_num == total_packets - 1:
        data = text[-last_packet_size:]
      else:
        data = text[packet_num * DATA_SIZE : (packet_num + 1) * DATA_SIZE ]

      send_socket.send(data, 'localhost', REC_PORT_NUMBER, 1, packet_num)

  # except TimeoutError:
  except:
    break
send_socket.send('\n', 'localhost', REC_PORT_NUMBER, 0, 0)
send_socket.udp_socket.close()
