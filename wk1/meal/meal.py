def main():
    user_time = input('What time is it? ').strip()
    time = convert(user_time)
    # print(time)

    if 7.00 <= time <= 8.00:
        print('breakfast time')
    elif 12.00 <= time <= 13.00:
        print('lunch time')
    elif 18.00 <= time <= 19.00:
        print('dinner time')

    return

def convert(time_str):
    hours, minutes = time_str.split(':')
    return  float(hours) + float(minutes) / 60

if __name__ == "__main__":
    main()