import uuid
import os
import string
import json
import hashlib
from time import time

class Chain:
    def generate_hash(hash):
        hash = hashlib.sha256("a".encode()).hexdigest()
    
    def verify_hash(last_hash, proof , last_proof):
        guess = f'{last_proof}{proof}{last_hash}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def add_block(self, block):
        if len(self.blocks) > 0:
            block.prev_hash = self.blocks[-1].hash
        block.seal()
        block.validate()
        self.blocks.append(block)
        
    def get_blocks(self):
        string_block = "{}{}{}{}{}".format(self.index, self.proof_number, self.previous_hash, self.data, self.timestamp)

        return hashlib.sha256(string_block.encode()).hexdigest()

    def add_transaction(self):
        