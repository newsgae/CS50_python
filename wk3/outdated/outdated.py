def main():
    # define dictionary to store item and count
    month_lst = [
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
                ]

    while True:
        try:
            # month-day-year order: either 9/8/1636 or September 8, 1636
            user_date = input('Date: ').strip().title()
            # print(f'Input: {user_date}')

            # extract year, month, day
            # case 9/8/1636
            if '/' in user_date:
                mm, dd, yyyy = user_date.split('/')

                # check output format
                # print(f'month of {mm} is {int(mm):02}; day of {dd} is {int(dd):02}')

                #  # check month and day correctness, otherwise reprompt user
                # if int(mm) > 12 or  int(dd) > 31 or len(yyyy) != 4:
                #     raise ValueError
            # case: december 8, 1636
            elif ',' in user_date:
                month, dd, yyyy = user_date.replace(',', '').split(' ')
                mm = month_lst.index(month) + 1

                # check output format
                # print(f'{mm} {mm:02} {dd} {dd:02}')
            # case: december 8 1636, repromt user
            else:
                pass

            # check month and day correctness, otherwise reprompt user
            if int(mm) > 12 or  int(dd) > 31 or len(yyyy) != 4:
                raise ValueError

            # # print output if correct
            #     print(f'{int(yyyy)}-{int(mm):02}-{int(dd):02}')
            #     break

        #  detect invalid input and re-asks them our prompting question via pass
        except (AttributeError, ValueError, NameError, KeyError, UnboundLocalError):
            pass
        # control+d from user
        except EOFError:
            break
        # print date
        else:
            # print output if correct
            print(f'{yyyy}-{int(mm):02}-{int(dd):02}')
            break

if __name__ == '__main__':
    main()


# check50 cs50/problems/2022/python/outdated
# submit50 cs50/problems/2022/python/outdated
