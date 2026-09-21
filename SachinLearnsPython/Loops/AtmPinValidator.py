#Simulate ATM login. Give 3 attempts. lock account if all 3 fail. Correct PIN = 1234
PIN = 1234
attempts = 0
success = False

while attempts < 3:
    guess = int(input(f"Attempt {attempts + 1}: "))
    attempts += 1
    if guess == PIN:
        success = True
        break
if success:
    print("Access granted")
else:
    print("Account locked")