import unittest
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        """Инициализация банковского счета."""
        self.account_holder = account_holder
        self.balance = initial_balance
    def deposit(self, amount):
        """Внесение денег на счет."""
        if amount <= 0:
            return "Сумма вклада должна быть положительной."
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        """Снятие денег со счета."""
        if amount <= 0:
            return "Сумма снятия должна быть положительной."
        if amount > self.balance:
            return "Недостаточно средств на счете."
        self.balance -= amount
        return self.balance
    def get_balance(self):
        """Получение текущего баланса."""
        return self.balance
class TestCase(unittest.TestCase):
    def test_account(self):
        account = BankAccount('Иван Петров', 450)
        self.assertEqual(account, "Иван Петров",  450)
    def test_deposit_neg(self):
        account = BankAccount('Иван Петров', 450)
        res = account.deposit(-500)
        self.assertEqual(res, "Сумма вклада должна быть положительной.")
    def test_deposit_pos(self):
        account = BankAccount('Иван Петров', 450)
        res = account.deposit(500)
        self.assertEqual(res, 950)
    def test_withdraw_neg(self):
        account = BankAccount('Иван Петров', 450)
        res = account.withdraw(-50)
        self.assertEqual(res, "Сумма снятия должна быть положительной.")
    def test_withdraw_notenough(self):
        account = BankAccount('Иван Петров', 450)
        res = account.withdraw(500)
        self.assertEqual(res, "Недостаточно средств на счете.")
    def test_withdraw(self):
        account = BankAccount('Иван Петров', 450)
        res = account.withdraw(50)
        self.assertEqual(res,400)
    def test_get_balance(self):
        account = BankAccount('Иван Петров', 450)
        res = account.get_balance()
        self.assertEqual(res,450)

