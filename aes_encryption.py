# ROHIT SINGH
# 2019135

import socket
import sys
import json

#Substitution Box for Encryption
S_Box_E=[0x9,0x4,0xa,0xb,0xd,0x1,0x8,0x5,0x6,0x2,0x0,0x3,0xc,0xe,0xf,0x7]

#Round Keys
w=[None]*6

#Function to multiply two polynomials in GF(2^4) i.e. x^4+x+1
def mult(p1,p2):
  p=0
  while p2:
    if p2 & 0b1:
      p^=p1
    p1<<=1
    if p1 & 0b10000:
      p1^= 0b11
    p2 >>=1
  return p & 0b1111


#Function to convert integer into state vector
def IntToVec(n):
  return [n>>12,(n>>4) & 0xf, (n>>8) & 0xf, n & 0xf]


#Function to convert state vector to integer
def VecToInt(n):
  return (n[0]<<12)+(n[2]<<8)+(n[1]<<4)+n[3]
 

#XORing state with Key in GF(2^4)
def AddRoundKey(s1,s2):
  return [i^j for i,j in zip(s1,s2)]


#Nibble Substitution
def SubNib(sbox,s):
  return [sbox[e] for e in s]


#Shift Rows of state
def ShiftRows(s):
  return [s[0],s[1],s[3],s[2]]


#Swapping each nibble (RotNib) and substituting it using s-box (SubNib)
def SubNibRotNib(b):
  return S_Box_E[b >>4]+(S_Box_E[b & 0x0f]<<4)


#Key Expansion
def KeyExp(key):
  Rcon1,Rcon2 = 0b10000000, 0b00110000
  w[0]=(key & 0xff00) >> 8
  w[1]=key & 0x00ff
  w[2]=w[0]^Rcon1^SubNibRotNib(w[1])
  w[3]=w[2]^w[1]
  w[4]=w[2]^Rcon2^SubNibRotNib(w[3])
  w[5]=w[4]^w[3]


#Mix Column For Encryption
def MixCol(s):
  return [s[0] ^ mult(4,s[2]), s[1] ^ mult(4,s[3]), s[2]^mult(4,s[0]),s[3]^ mult(4,s[1])]


#Function to Encrypt the Plaintext
def aes_encrypt(data,key):

  #Pre-Round Transformation

  #Generating Sub-Keys using given Key
  KeyExp(key)

  #Add Round Key i.e. Key0 XOR Plaintext
  state=((w[0]<<8)+w[1])^data

  print('After Pre-round Transformation:',state)
  print('Round Key K0:',(w[0]<<8)+w[1])

  state=IntToVec(state)


  #Round 1

  #Substitute Nibbles
  state=SubNib(S_Box_E,state)
  print('After Round 1 Substitute Nibbles:',state)
  #Shift Rows
  state=ShiftRows(state)
  print('After Round 1 Shift Rows:',state)
  #Mix Column
  state=MixCol(state)
  print('After Round 1 Mix Column:',state)
  #Add Round Key i.e. Key1 XOR state
  state=AddRoundKey(IntToVec((w[2]<< 8)+w[3]),state)
  print('After Round 1 Add Round Key',state)
  print('Round Key K1:',(w[2]<< 8)+w[3])

  #Round 2

  #Substitue Nibbles
  state=SubNib(S_Box_E,state)
  print('After Round 2 Subbstitue Nibbles:',state)
  #Shift Rows
  state=ShiftRows(state)
  print('After Round 2 Shift Rows:',state)
  #Add Round Key i.e. Key2 XOR state
  state=AddRoundKey(IntToVec( (w[4] << 8) + w[5]),state)
  print('After Round 2 Add Round Key:',state)
  print('Round Key K2:',(w[4] << 8) + w[5])

  return VecToInt(state)