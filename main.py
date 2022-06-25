print("Hi! I am a program written by Artem Ivanov from the 0305 group."
      " I am checking the correctness of the following statement for the entered bracket sequence:")
print("A correct bracket entry with two kinds of brackets : ' [ ] (  ) '.")
print("There should always be a square one after the round bracket, and a round one after the square one.")
print("Examples of correct sequences: \n()[]()\n(()[])\n[([()])]\n[(()[])](()[()])")

errors = 0
i = -1


def read():
    global i
    i += 1
    if i == len(s):
        return 0
    else:
        return s[i]


def error():
    global errors
    errors = 1


def first(symbol):
    if symbol == '[':
        symbol = read()
        symbol = first(symbol)
        if symbol == ']':
            symbol = read()
        else:
            error()
        symbol = round(symbol)
    elif symbol == '(':
        symbol = read()
        symbol = first(symbol)
        if symbol == ')':
            symbol = read()
        else:
            error()
        symbol = square(symbol)
    return symbol


def square(symbol):
    if symbol == '[':
        symbol = read()
        symbol = first(symbol)
        if symbol == ']':
            symbol = read()
        else:
            errors()
        symbol = round(symbol)
    return symbol


def round(symbol):
    if symbol == '(':
        symbol = read()
        symbol = first(symbol)
        if symbol == ')':
            symbol = read()
        else:
            errors()
        symbol = square(symbol)
    return symbol


flag = True

while flag:
    print("Please enter a line and press ''Enter'' when finished")
    s = input()
    if len(s) % 2 == 1:
        print("ERROR!")
    else:
        symbol = read()
        symbol = first(symbol)
        if symbol == 0 and errors == 0:
            print("Everything is right!")
        else:
            print("ERROR!")
        print("Do you want to try again? 1 - Yes, 0 - End program execution")
        flag = -1
        while flag not in [True, False]:
            f = input()
            if len(f) == 1:
                flag = bool(int(f))
                if flag not in [True, False]:
                    print("You entered an incorrect answer. Try again")
            else:
                print("You entered an incorrect answer. Try again")
        if not flag:
            break
        i = -1
        errors = 0
