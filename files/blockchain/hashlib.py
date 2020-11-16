from hashlib import sha256
data = input('data to be hashed goes here')
output = sha256(data.encode('utf-8'))
print(output)
