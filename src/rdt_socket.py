import header
import socket

class TimeoutError(Exception):
  pass

# class rdt_send_socket:
#   def __init__(self):
#     self.udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#   def send(self,data,dest_ip,dest_port,mode,packet_num=1):
#     packet = header.make_header(mode,packet_num)
#     packet.extend(bytearray(data, encoding='utf-8'))
#     self.udp_socket.sendto(packet,(dest_ip,dest_port))

class rdt_socket:
  def __init__(self,src_ip,src_port,timeout):
    self.udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    self.udp_socket.bind((src_ip,src_port))
    self.udp_socket.settimeout(timeout)
  
  def change_timeout(self,timeout):
    self.udp_socket.settimeout(timeout)

  def send(self,data,dest_ip,dest_port,mode,packet_num=1):
    packet = header.make_header(mode,packet_num)
    packet.extend(bytearray(data, encoding='utf-8'))
    # packet.extend(data)
    self.udp_socket.sendto(packet,(dest_ip,dest_port))


  def recv(self,recv_bytes=1024):
    try:
      packet,_ = self.udp_socket.recvfrom(recv_bytes)
      header_bytes = packet[:header.NUM_FIELDS]
      header_fields = header.decode_header(header_bytes)
      data = packet[header.NUM_FIELDS:]
      data = data.decode()
      return data,header_fields
    except socket.timeout:
      raise TimeoutError