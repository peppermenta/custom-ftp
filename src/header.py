NUM_FIELDS = 2

def make_header(data,mode,packet_num):
  '''
  Generate header for the data
  '''

  fields = []
  fields.append(mode)
  fields.append(packet_num)
  
  assert len(fields) == NUM_FIELDS
  header = bytearray(fields)
  return header

def decode_header(header):
  '''
  Parse and return all fields of the header
  '''
  fields = list(header)
  
  assert len(fields) == NUM_FIELDS
  return {
    'mode': fields[0],
    'packet_num': fields[1]
  }