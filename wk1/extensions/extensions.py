def main():
    file_name_lst = input('File name: ').strip().lower().split('.')

    if file_name_lst[-1] in ['gif', 'png']:
        print(f'image/{file_name_lst[-1]}')
    elif file_name_lst[-1] == 'jpg' or file_name_lst[-1] == 'jpeg':
        print(f'image/jpeg')
    elif file_name_lst[-1] in ['pdf', 'zip']:
        print(f'application/{file_name_lst[-1]}')
    elif file_name_lst[-1] == 'txt':
        print(f'text/plain')
    else:
        print('application/octet-stream')


main()