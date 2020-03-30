
#blockchain hack
from blockchain import Blockchain
new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

#new blockchain
my_blockchain = Blockchain()

#adding block
my_blockchain.add_block(new_transactions)

#displaying blockchain
my_blockchain.print_blocks()

#Changing the data of block 1
my_blockchain.chain[1].transactions = "fake_transactions"

#Validating blockchain
my_blockchain.validate_chain()
