import hashlib
import json
from datetime import datetime
from time import time
class Transaction():
    def __init__(self,from_address,to_address,amount):
        self.from_address=from_address
        self.to_address=to_address
        self.amount=amount
class Block():
    def __init__(self,tstamp,transactionsList,message,prevhash=''):
        self.nonce=0
        self.tstamp=tstamp
        self.transactionsList=transactionsList
        self.message=message
        self.prevhash=prevhash
        self.hash=self.calcHash()
        
    def calcHash(self):
        block_string=json.dumps({"nonce":self.nonce,"tstamp":str(self.tstamp),"transaciton":self.transactionsList[0].amount,"message":self.message,"prevhash":self.prevhash},sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    def mineBlock(self,diffic):
        while(self.hash[:diffic] != str('').zfill(diffic)):
            self.nonce += 1
            self.hash=self.calcHash()
        print("Block mined ", self.hash)
  
    def __str__(self):
        string="nonce: " + str(self.nonce) + "\n"
        string+= "tstamp: " + str(self.tstamp)+ "\n"
        string += "prevhas: " + str (self.prevhash)+ "\n"
        string += "hash: " + str (self.hash)+ "\n"
        string+="message"+str(self.message)
        return string

class BlockChain():
    def __init__(self):
        self.chain=[self.generateGenesisBlock(),]
        self.pendingTransations=[]
        self.mining_reward=100
        self.difficulty=4
        self.message=ms
       
    def generateGenesisBlock(self):
        return Block('01/01/2021',[Transaction(None,None,0),],ms)
    def getLastBlock(self):
        return self.chain[-1]
    def minePendingTransatin(self,mining_reward_address):
        block=Block(datetime.now(),self.pendingTransations,self.message)
        block.mineBlock(self.difficulty)
        print("Block is mined to got reward", self.mining_reward)
        self.chain.append(block)
        self.pendingTransations=[Transaction(None,mining_reward_address,self.mining_reward)]

    def createTransaction(self,T):
        self.pendingTransations.append(T)
    def getBalance(self,address):
        balance=0
        for b in self.chain:
            for t in b.transactionsList:
                if t.to_address == address:
                    balance += t.amount
                if t.from_address == address:
                    balance += t.amount
        return balance 

    def isChainValid(self):
        for i in range(1,len(self.chain)):
            prevb=self.chain[i-1]
            currb=self.chain[i]
            if(currb.hash != currb.calcHash()):
                print("invalid block")
                return False
            if(currb.prevhash != prevb.hash):
                print("invalid chain")
                return False
        return True
        

Coin=BlockChain()


Coin.createTransaction(Transaction('address1','address2',100))
Coin.createTransaction(Transaction('address2','address1',50))
print("Starting mining")
Coin.minePendingTransatin("address")
print(" balanace is ", Coin.getBalance("address"))

Coin.createTransaction(Transaction('address1','address2',200))
Coin.createTransaction(Transaction('address2','address1',150))
print("Starting mining again")
Coin.minePendingTransatin("aaddress")
print(" balanace is ", Coin.getBalance("address"))
