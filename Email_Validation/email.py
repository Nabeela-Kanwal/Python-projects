email = input("Enter your email : ")

if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") or (email[-3] == "."):
                if " " not in email:
                    if email.islower():
                        print("Valid email")
                    else:
                        print("Email should not contain uppercase letters")
                else:
                    print("Email should not contain spaces")
            else:
                print("Email must contain a dot near the end, like .com or .pk")
        else:
            print("Email must contain exactly one @")
    else:
        print("First character must be a letter")
else:
    print("Email must be at least 6 characters long")