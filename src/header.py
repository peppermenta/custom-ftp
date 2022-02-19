NUM_FIELDS = 2

def make_header(mode=0,packet_num=1):
  '''
  Generate header for the data
  '''

  # fields = []
  # fields.append(mode)
  # fields.append(packet_num)
  # assert len(fields) == NUM_FIELDS
  # header = bytearray(fields)

  header = f"{mode},{packet_num};"
  header = bytearray(header, encoding='utf-8')
  return header

def decode_header(header):
  '''
  Parse and return all fields of the header
  '''
  # fields = list(header)
  
  # assert len(fields) == NUM_FIELDS
  # return {
  #   'mode': fields[0],
  #   'packet_num': fields[1]
  # }

  comma_index = header.find(",")
  mode = int(header[:comma_index])
  packet_num = int(header[comma_index + 1:])
  return {
    'mode': mode,
    'packet_num': packet_num
  }