import liblo 

class Pot:
  """
  this class defines a potentiometer behavior
  """
  def __init__(self, label: int=0, address: int=9000):
    self.label = label 
    self.address = liblo.Address(address)
    self.previous_value = 0 

  def check_value(self, value: int=0):
    if value != self.previous_value:
      #print(f"label:\t{self.label}\tvalue:{value}")
      self.send_value(value) 
      self.previous_value = value
    return None  

  def send_value(self, value: int=0):
    address = self.address
    label = self.label
    liblo.send(address, "/hw_controller", label, value) 
    return None