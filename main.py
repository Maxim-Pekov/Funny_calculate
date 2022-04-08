msg_ = []
msg_.append("Enter an equation")
msg_.append("Do you even know what numbers are? Stay focused!")
msg_.append("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
msg_.append("Yeah... division by zero. Smart move...")
msg_.append("Do you want to store the result? (y / n):")
msg_.append("Do you want to continue calculations? (y / n):")
msg_.append(" ... lazy")
msg_.append(" ... very lazy")
msg_.append(" ... very, very lazy")
msg_.append("You are")
msg_.append("Are you sure? It is only one digit! (y / n)")
msg_.append("Don't be silly! It's just one number! Add to the memory? (y / n)")
msg_.append("Last chance! Do you really want to embarrass yourself? (y / n)")
memory = 0
i = 0
result = 0
oper = ""
x = 0
y = 0
while i == 0:
    print(msg_[0])
    calc = input().split()
    y = calc[2]
    x = calc[0]
    oper = calc[1]
    oper_good = "+-*/"
    if x == "M" or y == "M":
        if y == "M":
            y = memory
        if x == "M":
            x = memory
        i = 1
    elif x.isalpha() or y.isalpha():
        print(msg_[1])
    elif oper not in oper_good:
        print(msg_[2])

    msg = ""
    def is_one_digit(x):
        x = float(x)
        if x.is_integer() and x > -10 and x < 10:
            return True
        else:
            return False
    if is_one_digit(x) and is_one_digit(y):
        msg += msg_[6]
    if (x == "1" or y == "1") and (oper == "*"):
        msg += msg_[7]
    if (x == "0" or y == "0" or x == 0 or y == 0) and (oper == "*" or oper == "+" or oper == "-"):
        msg += msg_[8]
    if msg != "":
        msg = msg_[9] + msg
    print(msg)

    if oper == "+":
        result = float(x) + float(y)
        print(result)
        i = 1
    elif oper == "-":
        result = float(x) - float(y)
        print(result)
        i = 1
    elif oper == "*":
        result = float(x) * float(y)
        print(result)
        i = 1
    elif oper == "/":
        if y == "0" or y == 0:
            print(msg_[3])
            i = 0
        else:
            result = float(x) / float(y)
            print(result)
            i = 1
    while i == 1:
        print(msg_[4])
        ansver_safe = input()
        if ansver_safe == "n":
            i = 2
        elif is_one_digit(result):
            msg_index = 10
            while msg_index < 13:
                print(msg_[msg_index])
                ansver_safe = input()
                if ansver_safe == "y":
                    msg_index += 1
                if ansver_safe == "n":
                    msg_index = 13

        if ansver_safe == "y":
            memory = result
            i =2
        elif ansver_safe == "n":
            i = 2
    while i == 2:
        print(msg_[5])
        continue_ = input()
        if continue_ == "y":
            i = 0
        elif continue_ == "n":
            i = 3
