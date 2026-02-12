class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.accounts = {}
        self.validators = []
        self.create_genesis_block()

    def create_genesis_block(self):
        pass

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def create_block(self, validator):
        new_block = None

        self.chain.append(new_block)
        self.pending_transactions = []

    def get_balance(self, address):
        return self.accounts.get(address, {"balance": 0, "nonce": 0})["balance"]