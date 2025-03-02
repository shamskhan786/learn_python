import random;

charecters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

user_input = int(input("Enter your Number:"))

pasword = ""

for _ in range(user_input):
   pasword += random.choice(charecters)
print("\nGenerated password:", pasword)
