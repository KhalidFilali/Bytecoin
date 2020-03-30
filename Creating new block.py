
#Creating a block Class

# importing
from datetime import datetime
# print timestamp
print(datetime.now())

class Block:
# default constructor for block class
  def __init__(self, transactions, previous_hash):
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.nonce = 0
    self.timestamp = datetime.now()
