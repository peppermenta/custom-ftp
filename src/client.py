from rdt_socket import rdt_socket

# def recv_file():
  # pass



REC_PORT_NUMBER = 8083
SER_PORT_NUMBER = 8084
data = 'dummy'
count = 0
recv_socket = rdt_socket('localhost', REC_PORT_NUMBER, 2.0)
# print('Listening for message at port', REC_PORT_NUMBER)
# while data != '\n':
#   try:
#     data, header_fields = recv_socket.recv()
#   except:
#     count += 1
#     if count == 10:
#       break
#     print('No data')
#     continue
#   count = 0
#   print(header_fields)
#   print(data)
# recv_socket.udp_socket.close()
total_packets = 0
transmission_rate = 0

while True:
  recv_socket.send('\n', 'localhost', SER_PORT_NUMBER, 0)
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
  # return interval indices start and end inclusive, comma separated in a string
  interval = f""
  for i in range(transmission_rate):
    if not packet_trackers[i]+1==packet_trackers[i+1]:
      interval += f"{packet_trackers[i]},{packet_trackers[i]}"
    else:
      interval += f",{packet_trackers[i]}"
      while i<transmission_rate:
        if packet_trackers[i+1]+1==packet_trackers[i+2]:
          i += 1
        else:
          break
      interval += f",{packet_trackers[i+1]}"

  return interval

def process_data(data, packet_num):
  # delete packet_num element from packet_trackers and update data_received with data
  packet_trackers.remove(packet_num)
  data_received[packet_num] = data
  return

while len(packet_trackers) > 0:
  interval_data = get_interval()
  recv_socket.send(interval_data, 'localhost', SER_PORT_NUMBER, 1)
  while True:
    try:
      data, header_fields = recv_socket.recv()
      if(header_fields['mode'] == 0):
        continue
      packet_number = header_fields['packet_num']
      process_data(data,packet_number)
    except:
      break

recv_socket.udp_socket.close()