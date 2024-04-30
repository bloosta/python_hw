class Wallet:
    payment_system = "Почта Банк"

    def __init__(self, name: str, currency: str):
        self.name = name
        self.currency = currency
        self._balance = 0

    def deposit(self, amount: float):
        self._balance += amount
        print(f"Баланс кошелька {self.name} пополнен на {amount} {self.currency}")

    def withdraw(self, amount: float):
        if amount > self._balance:
            print("Недостаточно средств на балансе")
        else:
            self._balance -= amount
            print(f"С баланса кошелька {self.name} списано {amount} {self.currency}")

    def balance_info(self):
        print(f"Баланс кошелька {self.name}: {self._balance} {self.currency}")

    def delete_account(self):
        del self

class CryptoWallet(Wallet):
    BTC_PRICE = 72000
    ETH_PRICE = 3500

    def __init__(self, name: str, currency: str, coin: str):
        super().__init__(name, currency)
        self.coin = coin

    def balance_info(self):
        print(f"Баланс кошелька {self.name}: {self._balance} {self.coin}")

    def balance_in_usd(self):
        if self.coin == "BTC":
            usd_balance = self._balance * self.BTC_PRICE
        elif self.coin == "ETH":
            usd_balance = self._balance * self.ETH_PRICE
        else:
            print("Неподдерживаемая криптовалюта")
            return
        print(f"Баланс кошелька {self.name} в долларах: ${usd_balance:.2f}")

wallet1 = Wallet("Почта Кошель", "USD")
wallet1.deposit(8968)
wallet1.balance_info()
wallet1.withdraw(575)
wallet1.balance_info()
crypto_wallet = CryptoWallet("Почта Крипта", "BTC", "BTC")
crypto_wallet.deposit(0.0675987)
crypto_wallet.balance_info()
crypto_wallet.balance_in_usd()
crypto_wallet.withdraw(1.74535)
