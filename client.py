# ROHIT SINGH
# 2019135

import socket
import json
from aes_encryption import aes_encrypt
from rsa_algo import rsa
from hash import digest
from rsa_key_generation import generate_key

#Function for Client
def client_fun(s):
  print('Input:')
  #Ask for Message
  message=int(input('Message: '),2)

  #Ask for Secret Key
  secret_key=int(input('Secret Key: '),2)

  #Ask for RSA Key Generation Parameters
  p_client_public,q_client_public,e_client_public=map(int,input("Public Key Parameters: ").split())
  n_client_public=p_client_public*q_client_public

  #Generate Client Private Key Using Client Public Key Parameters
  d_client_private=generate_key(e_client_public,n_client_public)
  
  #Ask for Server Public Key || TODO>> Request not made yet.
  ch=input('Enter \' yes \' to request server for it \'s public key: ')
  s.send(ch.encode())

  #Receiving and Storing Server Public Key
  keys=json.loads(s.recv(12345).decode())
  e_server_public=keys['e_server_public']
  n_server_public=keys['n_server_public']
  print('Public Key Received!')

  print('Output:')
  #Encrypt Client Secret Key using Server Public Key in RSA Algorithm to get Encrypted Secret Key
  encrypted_secret_key=rsa(secret_key,e_server_public,n_server_public)
  print('Encrypted Secret Key: ', encrypted_secret_key)

  #Encrypt Message with Secret Key using AES Encryption Algorithm to get Ciphertext
  print('Ciphertext Intermediate Computation Process:')
  ciphertext=aes_encrypt(message,secret_key)
  print('Ciphertext: ',ciphertext)

  #Use Message in Hash ALgorithm to create Digest
  hash_digest=digest(message)
  print('Digest: ',hash_digest)

  #Use Digest, Client Private Key in RSA Algorithm to create Client Signature

  client_signature=rsa(int(hash_digest,16),d_client_private,n_client_public)
  print('Digital Signature: ',client_signature)

  #Arranging the data in dictionary and Sending it to Server

  data={'ciphertext':ciphertext,'encrypted_secret_key':encrypted_secret_key,'client_signature':client_signature,'e_client_public' : e_client_public,'n_client_public':n_client_public}
  s.send(json.dumps(data).encode())


  #Closing the Connection

  s.close()



s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#port 
port=12345
s.connect((socket.gethostname(),port))
print("Client And Server are Connected")
client_fun(s)

print('\nROHIT SINGH 2019135\n')