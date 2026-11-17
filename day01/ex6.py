
name = input("Enter your full name:")
initals = [name[0].upper() for name in name.split()]
print(f"your initials are {''.join(initals)}")