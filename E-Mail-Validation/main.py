email = input("Enter your Email: ")
k, j, d = 0, 0, 0

if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4:] == ".com") or (email[-3:] == ".in"):
                for i in email:
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i.isupper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i in ["_", ".", "@"]:
                        continue
                    else:
                        d = 1

                if k == 1 or j == 1 or d == 1:
                    print("Wrong Email 5")  # Invalid character, space, or capital letter
                else:
                    print("Valid Email ✅")
            else:
                print("Wrong Email 4")  # Invalid domain ending
        else:
            print("Wrong Email 3")  # More than one '@' or missing '@'
    else:
        print("Wrong Email 2")  # First character not a letter
else:
    print("Wrong Email 1")  # Length too short
