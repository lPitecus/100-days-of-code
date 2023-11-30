amount_left = 50
money_in_machine = 0
payment_complete = False
while not payment_complete:
    print(f"Amount Due: {amount_left}")
    payment = int(input("Insert Coin: "))
    if payment == 25 or payment == 10 or payment == 5:
        amount_left -= payment
    if amount_left <= 0:
        print(f"Change Owed: {(payment - amount_left)}")
        payment_complete = True