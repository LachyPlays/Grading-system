from cryptography.fernet import Fernet
import base64

inp = input("Enter a password: ")
t = Fernet(base64.urlsafe_b64encode(str.encode(inp.zfill(32))))
enc = t.encrypt(inp.encode())
dec = t.decrypt(enc)
print(enc.decode())
print(dec.decode())