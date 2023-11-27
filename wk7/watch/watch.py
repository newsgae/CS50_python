import re
import sys


'''
In a file called watch.py,
    implement a function called parse that
        expects a str of HTML as input,
        extracts any YouTube URL that’s the value of a src attribute of an iframe element therein, .
        and returns its shorter, shareable youtu.be equivalent as a str

    example:
        input: <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
        return: https://youtu.be/xvFZjo5PgG0

        input: <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer;
        return: https://youtu.be/xvFZjo5PgG0

        input: <iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>
        return: None

Expect that any such URL will be in one of the formats below.
Assume that the value of src will be surrounded by double quotes.
Assume that the input will contain no more than one such URL.
If the input does not contain any such URL at all, return None.

http://youtube.com/embed/xvFZjo5PgG0
https://youtube.com/embed/xvFZjo5PgG0
https://www.youtube.com/embed/xvFZjo5PgG0

first must known:
   [\w]+ many words or letter
    ^   start of a string
    $   end of a string
    .   any character
    \.  match "."
    a|b match a or b
    *   match to its left 0 or more times
    +   match to its left 1 or more times
    ?   match to its left 0 or 1 times, with or without
    {n} repeact n times
    {p, q} repeact p times, up to q times
    \w  match a-zA-Z0-9 and _
    \W  not of \w
    \d  match 0-9
    \D  not \d, no digit
    \s  match white space, \t, \n and \r
    \S  not \s
    \b  match start and end of a word, boundary
    ()  group
    (?:)

hint:
    re.search
    re special characters
    Note that * and + are “greedy,” insofar as “they match as much text as possible,”
        per docs.python.org/3/library/re.html#regular-expression-syntax.
    Adding ? immediately after either, a la *? or +?, “makes it perform the match in non-greedy or minimal fashion;
        as few characters as possible will be matched.”

'''


def main():

    if len(sys.argv)>2 :
        print('too many input')
    elif len(sys.argv)<1:
        print('too few input')
    else:
        print(parse(input("HTML: ")))
        # s = str(<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>)
        # print(s)
        # print(parse(s))

# method 1
def parse(s):
    match = re.search(r"^<iframe.*? src=\"(?:https?)://(?:w+\.)?youtube\.com/embed/([\w*]+)\".*?", s)

    if match:
        return f"https://youtu.be/{match.group(1)}"
    else:
        return None


if __name__ == "__main__":
    main()


# check50 cs50/problems/2022/python/watch
# submit50 cs50/problems/2022/python/watch
