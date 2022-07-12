# NetworkSecurity
A client and server application to provide confidentiality, authentication and integritys. To encrypt a message the client is using a simplified AES variant with 2 rounds. The client then sends ciphertext and key to
the server. Server on receiving the encrypted message decrypts the message.
Implemention of RSA algorithm from scratch that will be used for secret key encryption and digital signature. For Message digest creation "MD5" has been used for the implementation of hash algorithm . Working of the secure system is as follows:

![alt text](https://github.com/rohitvns/NetworkSecurity/blob/4ff566ffd9a7caf8478078b592f22ad6dd12c59a/Untitled%20presentation-1.jpg)

• Client inputs: Message, parameter for key generation (p, q, e) at Client end
• Server Inputs: parameter for key generation (p, q, e) at Server end.
• Message Flow:
o Client requests for public key of server.
o Server sends the public key.

o Client sends Ciphertext, Encrypted secret key, Client Signature, Client public
key.

• Client side computation:
Creation of Client signature through RSA algorithm, taking Digest from Hash
algorithm and client private key as input.
Creation of Ciphertext through the AES variant, taking Message and Secret key as
input.
Encryption of the Secret key with RSA algorithm, taking Secret key and Server Public
key as input.
• Server side Computation:
Decryption of Secret key using RSA algorithm
Decrypttion of ciphertext using AES variant
Creation of message digest
Verification of Client Signature
