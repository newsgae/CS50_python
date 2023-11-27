def main():
    expression = input('Expression: ').strip()

    x, y, z = expression.split(' ')
    if y == '+':
        answer = int(x) + int(z)
    elif y == '-':
        answer = int(x) - int(z)
    elif y == '*':
        answer = int(x) * int(z)
    elif y == '/' and int(z) != 0:
          answer = int(x) / int(z)
    else:
        print("invalide expression")

    print(f'{answer:.1f}')

main()