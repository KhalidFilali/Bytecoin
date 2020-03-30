
# impporting
from blockchain import Blockchain

block_one_transactions = {"sender":"Satoshi", "receiver": "Bob", "amount":"50"}
block_two_transactions = {"sender": "Bob", "receiver":"Alic", "amount":"25"}
block_three_transactions = {"sender":"Elon Musk", "receiver":"Alice, "amount":"35"}
fake_transactions = {"sender": "Khalid", "receiver":"Cole, Alice", "amount":"25"}

local_blockchain = Blockchain()
local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(fake_transactions)
local_blockchain.add_block(block_three_transactions)

local_blockchain.print_blocks()
print(local_blockchain.validate_chain())
