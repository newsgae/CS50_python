def main():
    user_input = input('Please enter your message and emoji:  ')
    result = convert(user_input)
    print(result)

def convert(str):
   return str.replace(':)', '\U0001F642') .replace(':(', '\U0001F641')

main()