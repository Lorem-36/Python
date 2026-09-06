#Mini-Project 3 — Password Strength Checker
password=input("Enter your password:")
def check_password_strength(password):
    num="0123456789"
    psw=False
    for i in password:
        if i in num:
            psw=True
    if len(password)>=8 and psw==True:
        return "strong"
    else:
        return "weak"

result = check_password_strength(password)
print("Password strength:", result)