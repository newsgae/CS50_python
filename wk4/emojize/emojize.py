import emoji

def main():
    user_input = input('Input: ').strip().lower()
    print('Output: ', emoji.emojize(user_input))
    # print("Emoji with grinning faces: ", emoji.emojize(":grinning_face_with_big_eyes:"))

if __name__ == '__main__':
    main()


# check50 cs50/problems/2022/python/emojize
# submit50 cs50/problems/2022/python/emojize
# pip install emoji
# emojis overview: https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias
# emoji py: https://pypi.org/project/emoji/
# Type: python emojize.py
# Enter:thumbsup Output of check50 cs50/problems/2022/python/emojize
