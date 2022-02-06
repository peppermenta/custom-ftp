NUM_FIELDS = 1

def make_header(data):
  '''
  Generate header for the data
  '''

  fields = []

  temp_field = 5
  fields.append(temp_field)
  
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
    'temp_field': fields[0]
  }