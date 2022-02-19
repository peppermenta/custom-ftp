from rdt_socket import rdt_socket
import os

HOME_DIR = os.path.join(os.path.dirname(__file__),'../')

REC_PORT_NUMBER = 8117
SER_PORT_NUMBER = 8118

DATA_SIZE = 128
data_file = open(os.path.join(HOME_DIR,'data','CS3543_10MB'), 'rb')
text = data_file.read()
text = str(text)
data_file.close()
bytes_remaining = len(text)
transmission_rate = 5
total_packets = int(bytes_remaining/DATA_SIZE) + 1

last_packet_size = bytes_remaining - (total_packets - 1) * DATA_SIZE

send_socket = rdt_socket('localhost', SER_PORT_NUMBER, 5.0)
_,header_fields = send_socket.recv()
mode = header_fields["mode"]


if(mode == 0):
  data = str(total_packets) + "," + str(transmission_rate)
  send_socket.send(data, 'localhost', REC_PORT_NUMBER, 0, 0)


while True:
  try: 
    interval, header_file = send_socket.recv()
    interval = interval.split(',')
    if(interval[0] == ''):
      interval.pop(0)

    for packet_num in interval:
      
      packet_num = int(packet_num)

      if packet_num == total_packets - 1:
        data = text[-last_packet_size:]
      else:
        data = text[packet_num * DATA_SIZE : (packet_num + 1) * DATA_SIZE ]

      send_socket.send(data, 'localhost', REC_PORT_NUMBER, 1, packet_num)

  except:
    break
send_socket.send('\n', 'localhost', REC_PORT_NUMBER, 0, 0)
send_socket.udp_socket.close()
