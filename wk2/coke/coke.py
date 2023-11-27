def main():

    due = 50
    total_paid = 0

    while True:
        print('Amount Due:', str(due))
        paid = int(input('Insert Coin: '))
         # Update price and total_paid for every valid transaction if coins in these denominations: 25 cents, 10 cents, and 5 cents
        if paid in [25, 10, 5]:
            due = due - paid
            total_paid += paid

            if due > 0:
                continue
            else:
                print('Change Owed:', str(total_paid-50))
                break


main()
