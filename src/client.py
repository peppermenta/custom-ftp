from struct import pack
from rdt_socket import rdt_socket
import os
import time

HOME_DIR = os.path.join(os.path.dirname(__file__),'../')
received_file = open(os.path.join(HOME_DIR,'data','received_binary_custom'), 'wb')

REC_PORT_NUMBER = 8119
SER_PORT_NUMBER = 8120
data = 'dummy'
count = 0

CLIENT_IP = '10.0.0.254'
SERVER_IP = '10.0.0.253'

recv_socket = rdt_socket(CLIENT_IP, REC_PORT_NUMBER, 0.3)
total_packets = 0
transmission_rate = 0

while True:
  recv_socket.send('\n', SERVER_IP, SER_PORT_NUMBER, 0)
  try:
    # confirmation from sender should have data: <total bytes,transmission rate>
    data, header_fields = recv_socket.recv()
    args = data.split(',')
    total_packets = int(args[0])
    transmission_rate = int(args[1])
  except:
    continue
  break

packet_trackers = [i for i in range(total_packets)]
data_received = ['' for i in range(total_packets)]

def get_interval():
  temp =  [str(element) for element in packet_trackers]
  if len(packet_trackers) < transmission_rate:
    return ",".join(temp)
  return ",".join(temp[0:transmission_rate])


def process_data(data, packet_num):
  # delete packet_num element from packet_trackers and update data_received with data
  packet_trackers.remove(packet_num)
  data_received[packet_num] = data
  return

start = time.time()
while len(packet_trackers) > 0:
  print(f'Progress: {1-(len(packet_trackers)/total_packets)}',end='\r')
  interval_data = get_interval()
  recv_socket.send(interval_data, SERVER_IP, SER_PORT_NUMBER, 1)
  while True:
    try:
      data, header_fields = recv_socket.recv()
      if(header_fields['mode'] == 0):
        continue
      packet_number = header_fields['packet_num']
      process_data(data, packet_number)
    except:
      #Timeout
      break
end = time.time()
print('Time taken:',end-start)
recv_socket.udp_socket.close()

data_received = "".join(data_received)

#Writing to the output file
received_file.write(str.encode(data_received))
received_file.close()
