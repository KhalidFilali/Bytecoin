
#Testing the SHA256 hash function
# importing
from hashlib import sha256
#I'll be creating a hash from my string text
text = 'My name is Khalid Filali!'
hash_result = sha256(text.encode())
#Displaying hash
print(hash_result.hexdigest())
