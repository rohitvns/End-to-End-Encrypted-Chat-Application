# ROHIT SINGH
# 2019135

import hashlib

#Function to calculate the digest formed by md5 hash algorithm
def digest(message):
  m=hashlib.md5(str(message).encode())
  return m.hexdigest()