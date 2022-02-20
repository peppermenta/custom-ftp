import header
import socket

class TimeoutError(Exception):
  pass

class rdt_socket:
  def __init__(self,src_ip,src_port,timeout):
    self.udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    self.udp_socket.bind((src_ip,src_port))
    self.udp_socket.settimeout(timeout)
  
  def change_timeout(self,timeout):
    self.udp_socket.settimeout(timeout)

  def send(self,data,dest_ip,dest_port,mode,packet_num=1):
    packet = header.make_header(mode,packet_num)
    if type(data)==str:
      packet.extend(bytearray(data, encoding='utf-8'))
    else:
      packet.extend(bytearray(data))
    self.udp_socket.sendto(packet,(dest_ip,dest_port))

  def recv(self,recv_bytes=70000):
    try:
      packet,_ = self.udp_socket.recvfrom(recv_bytes)
      packet = packet.decode()

      semicolon_index = packet.find(";")

      header_section = packet[:semicolon_index]
      header_fields = header.decode_header(header_section)
      data = packet[semicolon_index + 1:]
      return data, header_fields
    except socket.timeout:
      raise TimeoutError
