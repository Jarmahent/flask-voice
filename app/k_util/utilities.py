import random
import string  

class Utilities():
  def __init__(self):
    pass
  
  def randomString(stringLength=10):
      """Generate a random string of fixed length """
      letters = string.ascii_lowercase
      return ''.join(random.choice(letters) for i in range(stringLength))