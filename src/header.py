NUM_FIELDS = 2

def make_header(mode=0,packet_num=1):
  '''
  Generate header for the data
  '''

  header = f"{mode},{packet_num};"
  header = bytearray(header, encoding='utf-8')
  return header

def decode_header(header):
  '''
  Parse and return all fields of the header
  '''

  comma_index = header.find(",")
  mode = int(header[:comma_index])
  packet_num = int(header[comma_index + 1:])
  return {
    'mode': mode,
    'packet_num': packet_num
  }