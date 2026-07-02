import hashlib
import random
import requests
import ssl

from Crypto.Cipher import AES, DES


password = "admin123"

# Weak Hash
hash1 = hashlib.md5(password.encode()).hexdigest()

# Weak Hash
hash2 = hashlib.sha1(password.encode()).hexdigest()

# Weak Random
token = str(random.random())

# SSL Verification Disabled
requests.get(
    "https://example.com",
    verify=False
)

# Weak TLS
context = ssl.SSLContext(
    ssl.PROTOCOL_TLSv1
)

# ECB Mode
cipher = AES.new(
    b"1234567890123456",
    AES.MODE_ECB
)

# DES
cipher2 = DES.new(
    b"12345678",
    DES.MODE_ECB
)

# Hardcoded Key
SECRET_KEY = "1234567890123456"
