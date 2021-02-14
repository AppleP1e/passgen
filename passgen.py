import random
import sys
import os
import signal
password = ""
upper = 0
lower = 0
number = 0
special = 0


def signal_handler(signal, frame):
    print("\nDetected CTRL-C. quitting")
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    '########:::::'###:::::'######:::'######::'##:::::'##:'########::
     ##.... ##:::'## ##:::'##... ##:'##... ##: ##:'##: ##: ##.... ##:
     ##:::: ##::'##:. ##:: ##:::..:: ##:::..:: ##: ##: ##: ##:::: ##:
     ########::'##:::. ##:. ######::. ######:: ##: ##: ##: ##:::: ##:
     ##.....::: #########::..... ##::..... ##: ##: ##: ##: ##:::: ##:
     ##:::::::: ##.... ##:'##::: ##:'##::: ##: ##: ##: ##: ##:::: ##:
     ##:::::::: ##:::: ##:. ######::. ######::. ###. ###:: ########::
    ..:::::::::..:::::..:::......::::......::::...::...:::........:::
    """)


def shuffle(string):
  temp = list(string)
  random.shuffle(temp)
  return ''.join(temp)


def generate(up, low, num, symb):
    global password
    for x in range(int(up)):
        password += chr(random.randint(65, 90))
    for x in range(int(low)):
        password += chr(random.randint(97,122))
    for x in range(int(num)):
        password += chr(random.randint(48,57))
    for x in range(int(symb)):
        password += chr(random.randint(33,152))


def init():
    logo()
    print("\n\nWelcome to the simple number generator! Select the mode you want, and hit ENTER.")
    print("In random mode, you specify length, and get a random ammount of everything.")
    print("In Normal mode, you specify the ammount of each characters!")
    print("\n\n[1]Random Mode\n[2]Normal mode")
    cmd = input("> ")
    if cmd == "1":
        rand()
    elif cmd == "2":
        normal()
    else:
        print("Unknown command... quitting!")
        sys.exit(0)


def rand():
    global upper
    global lower
    global number
    global special
    length = input("Type in the length of your password!> ")
    if not str.isdigit(length):
        if length == "back":
            init()
    tlength = int(length)
    tup = random.randrange(0, int(tlength))
    tlength -= int(tup)
    tlow = random.randrange(0, int(tlength))
    tlength -= int(tlow)
    tnum = random.randrange(0, int(tlength))
    tlength -= int(tnum)
    tspec = int(tlength)
    generate(tup, tlow, tnum, tspec)


def normal():
    global upper
    global lower
    global number
    global special
    upper = input("Uppercase letters> ")
    if upper == "back":
        init()
    lower = input("Lowercase letters> ")
    if lower == "back":
        init()
    number = input("Numbers> ")
    if number == "back":
        init()
    special = input("Special Characters> ")
    if special == "back":
        init()
    generate(upper, lower, number, special)


init()
print("Your password is:\n" + shuffle(password))
print("Enjoy!")
