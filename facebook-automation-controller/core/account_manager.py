class AccountManager:
    def __init__(self, accounts):
        self.accounts = accounts

    def enabled_accounts(self):
        return [a for a in self.accounts if a.get("enabled", True)]
