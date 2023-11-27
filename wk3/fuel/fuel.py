def main():
    response = input('Fraction: ')
    fraction = get_fraction(response)
    print(fraction)

def get_fraction(str):

    while True:
        try:
            x, y = str.strip().split('/')
            answer = int(x)/int(y)*100
            if 1 < answer < 99:
                return f'{answer:.0f}%'
            elif 99 <= answer <= 100:
                return 'F'
            elif 0 <= answer <= 1:
                return 'E'
        except (ValueError, ZeroDivisionError):
            main()


if __name__ == '__main__':
    main()

# check50 cs50/problems/2022/python/fuel
# submit50 cs50/problems/2022/python/fuel