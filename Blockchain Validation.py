#Validation

#importing
from block import Block

class Blockchain:
  def __init__(self):
    self.chain = []
    self.all_transactions = []
    self.genesis_block()

  def genesis_block(self):
    transactions = {}
    genesis_block = Block(transactions, "0")
    self.chain.append(genesis_block)
    return self.chain

  # prints contents of blockchain
  def print_blocks(self):
    for i in range(len(self.chain)):
      current_block = self.chain[i]
      print("Block {} {}".format(i, current_block))
      current_block.print_contents()

  # add block to chain
  def add_block(self, transactions):
    previous_block_hash = self.chain[len(self.chain)-1].hash
    new_block = Block(transactions, previous_block_hash)
    self.chain.append(new_block)

  #blockchain validation
  def validate_chain(self):
    for i in range(1, len(self.chain)) :
        #Declaring variable to store block
      current = self.chain[i]
      #Declaring variable to store the previous block
      previous = self.chain[i-1]
      if current.hash != Block.generate_hash(current) :
        return False
      if previous.hash != Block.generate_hash(previous) :
        return False
    else :
      return True
