#
email=input("Enter your email address:")
word=email.split("@")
print(f"your username is {word[0]} and your domain name is {word[1]}")