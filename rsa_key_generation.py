# ROHIT SINGH
# 2019135

from phi_value import phi
from inverse import inv

def generate_key(e,n):
    phin=phi(n)
    d=inv(e,phin)
    return d