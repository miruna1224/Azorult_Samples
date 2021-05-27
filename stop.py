import socket
import tqdm
from os import *
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import io

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step
PATH = "/mnt/e/Licenta/BD/"

keyPair = RSA.generate(3072)

pubKey = keyPair.publickey()
print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))


f = []
for (dirpath, dirnames, filenames) in walk(PATH):
    for i in filenames :
        f.append(PATH + i)
        print (PATH + i)
        sizeToRead = int (path.getsize(PATH + i) / 100)
        print (sizeToRead, path.getsize(PATH + i))
        with io.open(PATH + i, "rb") as func:
            msg = func.read(sizeToRead)
            encryptor = PKCS1_OAEP.new(pubKey)
            encrypted = encryptor.encrypt(msg)
            print("Encrypted:", binascii.hexlify(encrypted))
        func.close()
    break


	
#filename = "/mnt/e/Licenta/cod/stop.py"
#filesize = path.getsize(f)

host = socket.gethostname()  
port = 9999                   # The same port as used by the server


for filename in f:
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s = socket.socket()
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")
    filesize = path.getsize(filename)
    # s.sendall(b'Hello, world')
    s.send(f"{filename}{SEPARATOR}{filesize}".encode()
	
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with io.open(filename, "rb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in 
            # busy networks
            s.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))
            #data = s.recv(BUFFER_SIZE)
            #print('Received', repr(data))
    f.close()	
    s.close()