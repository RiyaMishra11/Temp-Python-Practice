# 112 Hashing & Secure Data Utilities
import hashlib
import hmac
import secrets
import base64

# 1 SHA-256
text="Python"
print("1",hashlib.sha256(text.encode()).hexdigest())

# 2 SHA-512
print("2",hashlib.sha512(text.encode()).hexdigest())

# 3 Legacy MD5 demonstration
print("3",hashlib.md5(text.encode()).hexdigest())

# 4 Hash a file
file="/mnt/data/hash_demo_112.txt"
with open(file,"w",encoding="utf-8") as f: f.write("Python practice file")
h=hashlib.sha256()
with open(file,"rb") as f:
    for chunk in iter(lambda:f.read(4096),b""): h.update(chunk)
print("4",h.hexdigest())

# 5 Compare hashes
def sha(x): return hashlib.sha256(x.encode()).hexdigest()
print("5",sha("hello")==sha("hello"),sha("hello")==sha("Hello"))

# 6 Secure token
print("6",secrets.token_hex(16))

# 7 URL-safe token
print("7",secrets.token_urlsafe(16))

# 8 Secure random number
print("8",secrets.randbelow(100))

# 9 HMAC
secret=b"my-secret-key"; message=b"important message"
sig=hmac.new(secret,message,hashlib.sha256).hexdigest()
print("9",sig)

# 10 Verify HMAC
valid=hmac.compare_digest(sig,hmac.new(secret,message,hashlib.sha256).hexdigest())
print("10",valid)

# 11 Base64 encode/decode
original="Python Security"
encoded=base64.b64encode(original.encode()).decode()
decoded=base64.b64decode(encoded).decode()
print("11",encoded,decoded)
