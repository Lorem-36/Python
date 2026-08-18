#password checker
psw=input("Enter your password:")

if len(psw)>=8 and "@" in psw:
    print("your password contains @ and length is ok")
    for digit in psw:
        if digit.isdigit():
            print("your password is strong")
            break
    else:
            print("Psw must contain at least 1 digit")
else:
    print("Your password is weak, must contain @ and length should be 8")
