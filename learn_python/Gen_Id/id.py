import random;

name = input("Enter your Name:")

employee_number = random.randint(1000,9999)

employee_id = name[:4].upper() + name[:2].lower() + str(employee_number)

print(f"{name} \nID:{employee_id}")