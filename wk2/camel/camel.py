def main():
    camel_case = input('camelCase: ' ).strip()
    snake_case = str()
    for c in camel_case:
        if c.isupper():
            c = '_' + c.lower()
        snake_case = snake_case + c
    print(f'snake_case: {snake_case}')

main()

'''
# method-2:

camel = input("camelCase: ")
print("snake_case: ", end="")

for c in camel:
    if c.islower():
        print(c, end="")
    if c.isupper():
        print("_", c.lower(), end="", sep="")

print()
'''
