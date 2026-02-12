from utils.helpers import current_timestamp

class Block:
    def __init__(self, index, transactions, previous_hash, validator):
        self.index = index,
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.validator = validator
        self.timestamp = current_timestamp()
        self.hash = self.calculate_hash()

    def calculate_hash():
        pass

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.hash = self.calculate_hash()