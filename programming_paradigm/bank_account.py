class BankAccount:
    """A class representing a bank account with basic banking operations."""
    
    def __init__(self, initial_balance=0.0):
        """
        Initialize a BankAccount with an optional initial balance.
        
        Args:
            initial_balance (float): The starting balance (defaults to 0.0)
        """
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """
        Deposit a specified amount into the account.
        
        Args:
            amount (float): The amount to deposit
            
        Returns:
            None
        """
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account if sufficient funds exist.
        
        Args:
            amount (float): The amount to withdraw
            
        Returns:
            bool: True if withdrawal successful, False if insufficient funds
        """
        if amount > 0:
            if self.account_balance >= amount:
                self.account_balance -= amount
                return True
            else:
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False
    
    def display_balance(self):
        """
        Display the current account balance in a user-friendly format.
        
        Returns:
            None
        """
        print(f"Current Balance: ${self.account_balance:.2f}")
    
    def get_balance(self):
        """
        Get the current account balance.
        
        Returns:
            float: The current account balance
        """
        return self.account_balance