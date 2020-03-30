#Adding new block to the block chain
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

  # printing contents
  def print_blocks(self):
    for i in range(len(self.chain)):
      current_block = self.chain[i]
      print("Block {} {}".format(i, current_block))
      current_block.print_contents()

  # adding block to chain
  def add_block(self, transactions):
      #transaction data+ previous block hash added

    self.previous_block_hash = self.chain[len(self.chain)-1].hash
    new_block = Block(transactions, self.previous_block_hash)
    self.chain.append(new_block)
    return self.chain
