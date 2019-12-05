import random
import string  

class Utilities():
  def __init__(self):
    pass
  
  def randomString(self):
      letters = string.ascii_lowercase
      return ''.join(random.choice(letters) for i in range(15))