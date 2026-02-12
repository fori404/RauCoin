class Wallet:
    def __init__(self, private_key=None):
        self.private_key = private_key or self.generate_private_key()
        self.public_key = self.derive_public_key()
        self.address = self.derive_address()

    def generate_private_key(self):
        pass

    def derive_public_key(self):
        pass

    def derive_address(self):
        pass

    def sign_transaction(self, transaction_data):
        pass