def main():

    menu_dict = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }

    total = 0
    while True:
        try:
            # treat the user’s input case insensitively. Assume that every item on the menu will be titlecased.
            response = input('Item: ').strip().title()
            if response in menu_dict:
                total += menu_dict[response]
                # After each inputted item, display the total cost of all items inputted thus far,
                # prefixed with a dollar sign ($) and formatted to two decimal places.
                print(f'Total: ${total:.02f}')
        #  detect when the user has inputted control-d
        except EOFError:
            print()
            break
        #  ignore any input that isn’t an item.
        except KeyError:
            pass


if __name__ == '__main__':
    main()


# check50 cs50/problems/2022/python/taqueria
# submit50 cs50/problems/2022/python/taqueria
