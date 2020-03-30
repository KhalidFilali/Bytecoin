
transaction1 = {
  'amount': '30',
  'sender': 'Khalid',
  'receiver': 'Steve'
  }
transaction2 = {
  'amount': '200',
  'sender': 'Steve',
  'receiver': 'Khalid'
  }
transaction3 = {
  'amount': '300',
  'sender': 'Khalid',
  'receiver': 'Timothy'
  }
transaction4 = {
  'amount': '300',
  'sender': 'Rob',
  'receiver': 'Tom'
  }
transaction5 = {
  'amount': '200',
  'sender': 'Tim',
  'receiver': 'Tom'
  }
transaction6 = {
  'amount': '400',
  'sender': 'Alice',
  'receiver': 'Xavier'
  }

mempool = [transaction1, transaction2, transaction3, transaction4, \
           transaction5, transaction6]

mytransaction = {
  'amount' : '200',
  'sender' : 'A',
  'receiver' : 'B'
}
mempool.append(mytransaction)

block_transactions = [transaction1, transaction3, transaction4]
