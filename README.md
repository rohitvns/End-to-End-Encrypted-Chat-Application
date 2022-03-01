# NetworkSecurity
Create a client and server application to provide confidentiality, authentication and integrity using the concepts discussed in the course. To encrypt a message the client is using a simplified AES variant with 2 rounds. The client then sends ciphertext and key to
the server. Server on receiving the encrypted message decrypts the message. The process of encryption is explained in the attached AES variant file(AES_Variant). Two examples of this AES variant are given in attached files (Example_1 and Example_2).
Implement the RSA algorithm from scratch that will be used for secret key encryption and digital signature. For Message digest creation you may use any existing implementation of hash algorithm compatible with your program. Working of the secure system will be as follows:

https://github.com/rohitvns/NetworkSecurity/blob/4ff566ffd9a7caf8478078b592f22ad6dd12c59a/Untitled%20presentation-1.jpg

• Client inputs: Message, parameter for key generation (p, q, e) at Client end
• Server Inputs: parameter for key generation (p, q, e) at Server end.
• Message Flow:
o Client requests for public key of server.
o Server sends the public key.

o Client sends Ciphertext, Encrypted secret key, Client Signature, Client public
key.

• Client side computation:
o Create Client signature through RSA algorithm, taking Digest from Hash
algorithm and client private key as input.
o Create Ciphertext through the AES variant, taking Message and Secret key as
input.
o Encrypt Secret key with RSA algorithm, taking Secret key and Server Public
key as input.
• Server side Computation:
o Decrypt Secret key using RSA algorithm
o Decrypt ciphertext using AES variant
o Create message digest
o Verify Client Signature
