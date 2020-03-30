#Creating/declaring chain and genesis block

#importing
from block import Block

class Blockchain:
    #Initializing chain
    def __init__(self):
        #verified transactions list
      self.chain = []
      #unverified transaction list
      self.all_transactions = []
      #genesis block
      self.genesis_block()
    #Genesis block creation
    def genesis_block(self):
      self.transactions = []
      self.previous_hash = 0
      Block(self.transactions, self.previous_hash)
      self.chain.append(Block)
