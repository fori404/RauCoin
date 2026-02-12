from core.wallet import Wallet

class Transaction:
    def __init__(self, sender, receiver, amount, nonce, tx_type="TRANSFER", signature=None):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.nonce = nonce
        self.type = tx_type
        self.signature = signature
        self.tx_hash = self.calculate_hash()

    def calculate_hash():
        pass

    def sign(self, wallet: Wallet):
        pass

    def verify_signature(self):
        pass