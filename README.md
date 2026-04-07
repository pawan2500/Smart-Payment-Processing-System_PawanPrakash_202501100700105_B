# Smart-Payment-Processing-System_PawanPrakash_202501100700105_B
# Smart Payment Processing System

This project is a Python-based simulation of a Smart Payment Processing System. It demonstrates core Object-Oriented Programming (OOP) concepts by implementing a common interface for various payment methods.

## Overview

The system allows a user to make payments using different methods: Credit Card, UPI, PayPal, and a Digital Wallet. While all payment methods follow a standard interface, each implements its own specific business logic for computing the final payable amount (including fees, taxes, or cashbacks).

## Key OOP Concepts Demonstrated

* **Abstraction:** Utilizes Python's `abc` module to create an abstract base class (`Payment`) with an abstract method (`pay()`). This enforces a strict blueprint that all specific payment classes must follow.
* **Inheritance:** Specific payment methods (`CreditCardPayment`, `UPIPayment`, etc.) inherit from the base `Payment` class, reusing the `generate_receipt()` method and constructor logic.
* **Polymorphism:** A single `process_payment(payment, amount)` function accepts any payment object and dynamically calls the correct `pay()` method at runtime based on the object's type (Runtime Polymorphism/Duck Typing).

## Payment Methods & Logic

1.  **Credit Card Payment:** * Applies a **2%** gateway fee on the transaction amount.
    * Applies **18%** GST specifically on the gateway fee.
2.  **UPI Payment:** * Provides a flat cashback of **₹50** if the payment amount is strictly greater than 1000.
3.  **PayPal Payment:** * Applies a **3%** international transaction fee.
    * Adds an additional fixed currency conversion fee of **₹20**.
4.  **Digital Wallet Payment:** * Maintains a specific wallet balance.
    * Succeeds and deducts the amount if sufficient balance exists; otherwise, the transaction fails.

## Prerequisites

* Python 3.6 or higher installed on your system.

## How to Run

1.  Save the provided Python code into a file named `payment_system.py` (or similar).
2.  Open your terminal or command prompt.
3.  Navigate to the directory where the file is saved.
4.  Run the script using the following command:

    ```bash
    python payment_system.py
    ```

## Example Output

Running the script will process a series of predefined transactions and output receipts demonstrating the logic for each payment type, including successful and failed wallet transactions.
