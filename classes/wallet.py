import uuid
import os
import string
import json
import hashlib
from time import time

class Wallet (object):
    unique_id = string
    balance = int
    history = []

    def generate_unique_id(self):
        id_unique = uuid.uuid4()

    def __init__(self, solder):
        self.solder = float(solder)

    def add_balance(self, somme):
        self.solder += somme
        return self.solder

    def sub_balance(self, somme):
        self.solder -= somme
        return self.solder

    def send(self, sender, receiver, amount):
        self.data.append({

            'sender': sender,

            'receiver': receiver,

            'amount': amount

        })

        return True

    def save(self):
        try:
            with open('wallets.txt',mode='w') as f:
                savable_chain = [block.__dict__ for block in [Block(blok.index,blok.previous_hash,[tx.__dict__ for tx in blok.transactions],blok.proof,blok.timestamp) for blok in self.__chain]]
                f.write(json.dumps(savable_chain))
                f.write('\n')
                savable_tx = [tx.__dict__ for tx in self.__open_transaction]
                f.write(json.dumps(savable_tx))
                f.write('\n')
                f.write(json.dumps(self.__peer_nodes))
        except:
            print('Saving Failed')

    def load(self):
        try:
            with open('wallets.txt',mode='r') as f:
                file_content = f.readlines()
            blockchain = json.loads(file_content[0][:-1])
            updated_blockchain = []
            for block in blockchain:
                converted_tx = [updated_transactions(tx['sender'],tx['recipent'],tx['signature'],tx['amount']) for tx in block['transactions']]
                updated_block = Block(block['index'],block['previous_hash'],converted_tx,block['proof'],block['timestamp'])
                updated_blockchain.append(updated_block)
            self.chain=updated_blockchain
            open_transaction = json.loads(file_content[1][:-1])
            updated_transactions = []
            for tx in open_transaction:
                updated_transaction = updated_transactions(tx['sender'],tx['recipent'],tx['signature'],tx['amount'])
                updated_transactions.append(updated_transaction)
            self.__open_transaction=updated_transactions
            peer_nodes = json.loads(file_content[2])
            self.__peer_nodes = set(peer_nodes)
        except (IOError,IndexError):
            pass