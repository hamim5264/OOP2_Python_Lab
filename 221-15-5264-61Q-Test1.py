def transfer_funds(sender_account_balance, amount_to_transfer):
    if amount_to_transfer <= 0:
        raise ValueError("Transfer amount must be a positive number.")

    if amount_to_transfer > sender_account_balance:
        raise ValueError("Sorry! Insufficient balance to transfer.")
    updated_balance = sender_account_balance - amount_to_transfer
    return updated_balance


try:
    print("Enter Your Balance: ")
    sender_balance = int(input())
    print("Enter the amount you want to transfer: ")
    amount = int(input())
    new_balance = transfer_funds(sender_balance, amount)
    print("Transfer successful.")
    print("Updated balance: ", new_balance)
except ValueError as e:
    print("Transfer failed: ", e)
