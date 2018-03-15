#Jake Hayes
from random import randint
def countdown2(n):
    while n > 0:
        print n
        n -= 1
    print 'DONE!'

def countdown3(n):
    for i in range(n, 0, -1):
        print i
    print 'DONE!'

def pick3():
    """
    This randomly generates a number between [1, 10]
    and gives the user 3 attempts to guess the
    correct answer.

    Input

        n   value between [1, 10]

    Output

        str  prompt whether the answer was correct or incorrect

    Usage

        >>> pick3()
        Enter a number between 1 and 10: 8
        You got it!

    """
    x = randint(1, 10)
    for i in range(3):
        j = input("Enter a number between 1 and 10: ")
        if(j == x):
            print('You got it!')
            return
    print('Too bad!')
    print('The number was ' + str(x))
    return

countdown2(10)
countdown3(10)
pick3()
