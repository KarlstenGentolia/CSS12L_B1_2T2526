while True:
    email = input("Enter your email address :\n").strip()
    if "@" not in email:
        print("Invalid email: missing '@' symbol.")
    elif email.count("@") > 1:
        print("Invalid email: more than one '@' symbol.")
    elif " " in email:
        print("Invalid email: email should not contain spaces.")
    else:
        username, domain = email.split("@")
        if not (domain.endswith(".com") or domain.endswith(".edu") or domain.endswith(".ph")):
            print("Invalid email: domain must end with .com, .edu, or .ph.")
        else:
            username_formatted = username.lower().replace("_", " ").replace(".", " ")
            print(f"Username: {username_formatted} | Domain: {domain}")