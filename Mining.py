
#Mining

new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

# importing
from hashlib import sha256
# sets the amount of leading zeros that must be found in the hash produced by the nonce
difficulty = 2
nonce = 0

# creating the POW(proof of work)
data = str(nonce) + str(new_transactions)
proof = sha256(data.encode()).hexdigest()
# displaying proof
print(proof)

#Finding a proof with the required difficulty(in this case 2 zeros)
while proof[0: difficulty] != str('0' * difficulty) :
  nonce += 1
  data = str(nonce) + str(new_transactions)
  proof = sha256(data.encode()).hexdigest()
else :
  final_proof = proof

#printing found proof
print(final_proof)
