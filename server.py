# ROHIT SINGH 
# 2019135

import socket
import json
from rsa_algo import rsa
from hash import digest
from aes_decryption import aes_decrypt
from rsa_key_generation import generate_key

#Function for Server
def server_fun(conn):

  #Request from Client for Server Public Key
  val=conn.recv(12345).decode() 
  if val =='yes':

    print('Input:')
  #Ask For RSA Key Generation Parameters
    p_server_public,q_server_public,e_server_public=map(int, input('Public Key Parameters: ').split())
    n_server_public=p_server_public*q_server_public
    d_server_private=generate_key(e_server_public,n_server_public)

  #Arranging the data in dictionary and Sending it to Client on requesting
    keys = {"e_server_public":e_server_public, "n_server_public":n_server_public}
    conn.send(json.dumps(keys).encode())

  #Receiving the data from Client
  data = json.loads(conn.recv(12345).decode())
  ciphertext=data['ciphertext']
  encrypted_secret_key=data['encrypted_secret_key']
  client_signature=data['client_signature']
  e_client_public=data['e_client_public']
  n_client_public=data['n_client_public']

  print('Output:')
  #Decrypt Encrypted Secret Key using Server Private Key using RSA Algorithm and get Secret Key
  secret_key=rsa(encrypted_secret_key,d_server_private,n_server_public)
  print('Decrypted Secret Key: ',bin(secret_key))

  #Decrypt Ciphertext using Secret Key in AES Decryption Algorithm to get Message
  print('Decrypted Intermediate Process:')
  message=aes_decrypt(ciphertext,secret_key)
  print('Decrypted Plaintext: ',bin(message))

  #Use Message in Hash Algorithm to make Digest
  hash_digest_server=digest(message)
  print('Message Digest: ',hash_digest_server)

  #Use Client Signature, Client Public Key to create Signature
  signature=rsa(client_signature,e_client_public,n_client_public)
  print('Intermediate Verification Code: ',signature)

  #Verifying Signature with created Signature
  if signature == int(hash_digest_server,16)%n_client_public:
    print('Signature Verified')
  else:
    print('Signature Not Verified')

  # Closing the connection
  conn.close()


s=socket.socket()
#port
port=12345
s.bind((socket.gethostname() ,port))
#server in listening mode
s.listen(5)

conn,addr=s.accept()

server_fun(conn)

print('\nROHIT SINGH 2019135\n')