#Pawan Prakash_202501100700105 
from abc import ABC, abstractmethod

# 1. Abstraction: Creating an abstract base class
class Payment(ABC):
    def __init__(self, user_name):
        self.user_name = user_name
        self.original_amount = 0
        self.final_amount = 0

    # Abstract method to be implemented by child classes
    @abstractmethod
    def pay(self, amount):
        pass

    # Concrete method shared by all child classes
    def generate_receipt(self):
        print(f"--- Receipt for {self.user_name} ---")
        print(f"Original Amount: ₹{self.original_amount:.2f}")
        print(f"Final Amount Paid: ₹{self.final_amount:.2f}")
        print("-" * 30 + "\n")


# 2. Inheritance: Child classes inheriting from Payment base class

class CreditCardPayment(Payment):
    def pay(self, amount):
        self.original_amount = amount
        # 2% gateway fee
        gateway_fee = amount * 0.02
        # 18% GST on the gateway fee
        gst = gateway_fee * 0.18
        
        self.final_amount = amount + gateway_fee + gst
        print(f"Processing Credit Card transaction...")
        self.generate_receipt()


class UPIPayment(Payment):
    def pay(self, amount):
        self.original_amount = amount
        # Cashback of ₹50 if amount > 1000
        cashback = 50 if amount > 1000 else 0
        
        self.final_amount = amount - cashback
        print(f"Processing UPI transaction...")
        if cashback > 0:
            print(f"** Cashback of ₹{cashback} applied! **")
        self.generate_receipt()


class PayPalPayment(Payment):
    def pay(self, amount):
        self.original_amount = amount
        # 3% international transaction fee
        intl_fee = amount * 0.03
        # Fixed currency conversion fee
        conversion_fee = 20
        
        self.final_amount = amount + intl_fee + conversion_fee
        print(f"Processing PayPal transaction...")
        self.generate_receipt()


class WalletPayment(Payment):
    def __init__(self, user_name, initial_balance):
        super().__init__(user_name)
        self.balance = initial_balance

    def pay(self, amount):
        self.original_amount = amount
        print(f"Processing Wallet transaction...")
        
        # Check wallet balance
        if amount > self.balance:
            print(f"Transaction Failed: Insufficient balance. Attempted: ₹{amount}, Available: ₹{self.balance}\n")
        else:
            self.balance -= amount
            self.final_amount = amount
            print(f"Transaction Successful. Remaining Wallet Balance: ₹{self.balance:.2f}")
            self.generate_receipt()


# 3. Polymorphism: A single function that handles any Payment object
def process_payment(payment, amount):
    # The appropriate pay() method is called based on the object type passed at runtime
    payment.pay(amount)


# --- Demonstration ---
if __name__ == "__main__":
    # Create objects of all payment classes
    cc_user = CreditCardPayment("Alice")
    upi_user = UPIPayment("Bob")
    paypal_user = PayPalPayment("Charlie")
    wallet_user = WalletPayment("David", 1000) # Initialize with ₹1000 balance

    print("=== Processing Payments ===\n")

    # Demonstrate runtime polymorphism
    process_payment(cc_user, 5000)     # Credit Card: Adds 2% fee + 18% GST on the fee
    
    process_payment(upi_user, 1200)    # UPI: Gets ₹50 cashback (amount > 1000)
    process_payment(upi_user, 800)     # UPI: No cashback (amount < 1000)
    
    process_payment(paypal_user, 2000) # PayPal: Adds 3% fee + ₹20
    
    process_payment(wallet_user, 400)  # Wallet: Succeeds, balance drops to 600
    process_payment(wallet_user, 800)  # Wallet: Fails, insufficient balance
