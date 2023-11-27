def main():
    
    # define dictionary to store item and count
    grocery = {}

    while True:
        try:
            # treat the user’s input case insensitively. output the user’s grocery list in all uppercase
            item = input().strip().upper()
            # not add item, just add count
            if item in grocery:
                grocery[item] += 1
            # add item and count as 1
            else:
                grocery[item] = 1

        #  detect when the user has inputted control-d
        except EOFError:
            # sorted alphabetically by item, prefixing each line with the number of times the user inputted that item
            for item in sorted(grocery):
                print(f'{grocery[item]:.0f} {item}')
            break


if __name__ == '__main__':
    main()


# check50 cs50/problems/2022/python/grocery
# submit50 cs50/problems/2022/python/grocery
