#Generating block hash
#importing
from datetime import datetime
from hashlib import sha256
class Block:
    #Initializing block
  def __init__(self, transactions, previous_hash, nonce = 0):
    self.timestamp = datetime.now()
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.nonce = nonce
    #hash generation of self block
    self.hash = self.generate_hash()

    #Displaying/printing block
  def print_block(self):
    # prints block contents
    print("timestamp:", self.timestamp)
    print("transactions:", self.transactions)
    print("current hash:", self.generate_hash())

    #Generating hash for block
  def generate_hash(self):
    #block contents stores information of block
    block_contents = str(self.timestamp) + str(self.transactions) + \
    str(self.nonce) + str(self.previous_hash)
    #block_hash stores hash of the block
    block_hash = sha256(block_contents.encode())
    #extracting hash value
    return block_hash.hexdigest()
