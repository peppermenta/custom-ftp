import header
import socket

class rdt_send_socket:
  def __init__(self):
    self.udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

  def send(self,data,dest_ip,dest_port):
    packet = header.make_header(data)
    packet.extend(bytearray(data))
    self.udp_socket.sendto(packet,(dest_ip,dest_port))

class rdt_recv_socket:
  def __init__(self,src_ip,src_port):
    self.udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    self.udp_socket.bind((src_ip,src_port))

  def recv(self):
    packet,_ = self.udp_socket.recvfrom(1024)
    header_bytes = packet[:header.NUM_FIELDS]
    header_fields = header.decode_header(header_bytes)
    data = packet[header.NUM_FIELDS:]

    return data,header_fields